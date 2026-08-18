#!/usr/bin/env python3
"""Compare a generated or audited structure.md with a truth document."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path


STATUS_RE = re.compile(
    r"^### \[(?P<status>\?|Met|Unmet|N/A)\] \[(?:MUST|SHOULD)\]$",
    re.IGNORECASE,
)
HEADING_RE = re.compile(r"^#{1,3} ")
ID_RE = re.compile(r"\[([a-z][a-z0-9_]*)\]")
DEP_RE = re.compile(r"^\[dependancy\]:\s*\S", re.IGNORECASE)


@dataclass
class Block:
    status: str
    criterion_id: str | None
    text: str
    has_dependency: bool


def normalize(value: str) -> str:
    value = re.sub(r"\[[a-z][a-z0-9_]*\]", "", value)
    value = re.sub(r"\s+", " ", value).strip().lower()
    return value


def extract_blocks(path: Path) -> list[Block]:
    lines = path.read_text(encoding="utf-8").splitlines()
    blocks: list[Block] = []
    for index, line in enumerate(lines):
        match = STATUS_RE.match(line)
        if match is None:
            continue
        end = len(lines)
        for cursor in range(index + 1, len(lines)):
            if HEADING_RE.match(lines[cursor]):
                end = cursor
                break
        body = lines[index + 1 : end]
        ids = []
        for item in body:
            ids.extend(value for value in ID_RE.findall(item) if value != "dependancy")
        criterion_text = next(
            (item.strip() for item in body if item.strip() and not item.startswith("[")),
            "",
        )
        status_raw = match.group("status")
        status = status_raw.upper() if status_raw.upper() == "N/A" else status_raw.title()
        blocks.append(
            Block(
                status=status,
                criterion_id=ids[0] if ids else None,
                text=normalize(criterion_text),
                has_dependency=any(DEP_RE.match(item) for item in body),
            )
        )
    return blocks


def _best_match(truth: Block, candidates: list[Block], used: set[int]) -> tuple[int, float]:
    if truth.criterion_id:
        for index, candidate in enumerate(candidates):
            if index not in used and candidate.criterion_id == truth.criterion_id:
                return index, 1.0
    best_index, best_score = -1, 0.0
    for index, candidate in enumerate(candidates):
        if index in used:
            continue
        score = SequenceMatcher(None, truth.text, candidate.text).ratio()
        if score > best_score:
            best_index, best_score = index, score
    return best_index, best_score


def evaluate(candidate_path: Path, truth_path: Path) -> dict:
    candidate = extract_blocks(candidate_path)
    truth = extract_blocks(truth_path)
    used: set[int] = set()
    matches: list[tuple[Block, Block]] = []
    for truth_block in truth:
        index, score = _best_match(truth_block, candidate, used)
        if index >= 0 and score >= 0.90:
            used.add(index)
            matches.append((truth_block, candidate[index]))
    structural_recall = len(matches) / len(truth) if truth else 0.0
    comparable = [
        pair
        for pair in matches
        if pair[0].status != "?" and pair[1].status != "?"
    ]
    truth_decided = [block for block in truth if block.status != "?"]
    decision_recall = (
        len(comparable) / len(truth_decided) if truth_decided else 1.0
    )
    status_agreement = (
        sum(left.status == right.status for left, right in comparable) / len(comparable)
        if comparable
        else None
    )
    decided = [block for block in candidate if block.status != "?"]
    dependency_coverage = (
        sum(block.has_dependency for block in decided) / len(decided) if decided else 1.0
    )
    return {
        "truth_criteria": len(truth),
        "candidate_criteria": len(candidate),
        "matched_criteria": len(matches),
        "structural_recall": round(structural_recall, 4),
        "comparable_statuses": len(comparable),
        "truth_decided_criteria": len(truth_decided),
        "decision_recall": round(decision_recall, 4),
        "status_agreement": (
            round(status_agreement, 4) if status_agreement is not None else None
        ),
        "decided_criteria": len(decided),
        "dependency_coverage": round(dependency_coverage, 4),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", required=True, type=Path)
    parser.add_argument("--truth", required=True, type=Path)
    parser.add_argument("--min-structural-recall", type=float, default=0.95)
    parser.add_argument("--min-status-agreement", type=float, default=0.90)
    parser.add_argument("--min-decision-recall", type=float, default=0.80)
    parser.add_argument("--min-dependency-coverage", type=float, default=1.0)
    parser.add_argument(
        "--skeleton",
        action="store_true",
        help="Evaluate structure only; do not require status agreement",
    )
    args = parser.parse_args()
    metrics = evaluate(args.candidate, args.truth)
    print(json.dumps(metrics, ensure_ascii=False, indent=2))
    passed = (
        metrics["structural_recall"] >= args.min_structural_recall
        and metrics["dependency_coverage"] >= args.min_dependency_coverage
    )
    if not args.skeleton:
        agreement = metrics["status_agreement"]
        passed = (
            passed
            and metrics["decision_recall"] >= args.min_decision_recall
            and agreement is not None
            and agreement >= args.min_status_agreement
        )
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
