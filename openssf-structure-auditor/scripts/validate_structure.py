#!/usr/bin/env python3
"""Validate structure.md status headings and dependency evidence rules."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


STATUS_RE = re.compile(
    r"^### \[(?P<status>\?|Met|Unmet|N/A)\] "
    r"\[(?P<level>MUST|SHOULD)\]$",
    re.IGNORECASE,
)
HEADING_RE = re.compile(r"^#{1,3} ")
DEPENDENCY_RE = re.compile(r"^\[dependancy\]:\s*(?P<value>.*)$", re.IGNORECASE)
CRITERION_ID_RE = re.compile(r"\[([a-z][a-z0-9_]*)\]")


@dataclass
class Finding:
    severity: str
    line: int
    message: str


@dataclass
class Report:
    path: str
    criteria: int
    decided: int
    unknown: int
    dependencies: int
    findings: list[Finding]

    @property
    def errors(self) -> int:
        return sum(item.severity == "error" for item in self.findings)

    @property
    def warnings(self) -> int:
        return sum(item.severity == "warning" for item in self.findings)


def _block_end(lines: list[str], start: int) -> int:
    for index in range(start + 1, len(lines)):
        if HEADING_RE.match(lines[index]):
            return index
    return len(lines)


def validate(path: Path) -> Report:
    lines = path.read_text(encoding="utf-8").splitlines()
    findings: list[Finding] = []
    criteria = decided = unknown = dependencies = 0
    seen_ids: dict[str, int] = {}
    for index, line in enumerate(lines):
        if not line.startswith("### ["):
            continue
        match = STATUS_RE.match(line)
        if match is None:
            findings.append(
                Finding("error", index + 1, f"Invalid criterion heading: {line}")
            )
            continue
        criteria += 1
        raw_status = match.group("status")
        status = raw_status.upper() if raw_status.upper() == "N/A" else raw_status.title()
        if raw_status != "?" and raw_status not in {"Met", "Unmet", "N/A"}:
            findings.append(
                Finding(
                    "warning",
                    index + 1,
                    f"Use canonical status capitalization instead of {raw_status}",
                )
            )
        end = _block_end(lines, index)
        block = lines[index + 1 : end]
        dep_lines = [DEPENDENCY_RE.match(item) for item in block]
        dep_matches = [item for item in dep_lines if item is not None]
        dependencies += len(dep_matches)
        if status == "?":
            unknown += 1
        else:
            decided += 1
            if not dep_matches:
                findings.append(
                    Finding(
                        "error",
                        index + 1,
                        "Decided criterion is missing a [dependancy]: line",
                    )
                )
            elif not dep_matches[-1].group("value").strip():
                findings.append(
                    Finding("error", index + 1, "Dependency evidence is empty")
                )
        ids = []
        for item in block:
            ids.extend(
                value
                for value in CRITERION_ID_RE.findall(item)
                if value != "dependancy"
            )
        if not ids:
            findings.append(
                Finding("warning", index + 1, "Criterion has no machine-readable id")
            )
        for criterion_id in set(ids):
            if criterion_id in seen_ids:
                findings.append(
                    Finding(
                        "error",
                        index + 1,
                        f"Duplicate criterion id {criterion_id}; first at line {seen_ids[criterion_id]}",
                    )
                )
            else:
                seen_ids[criterion_id] = index + 1
    if criteria == 0:
        findings.append(Finding("error", 1, "No criterion headings found"))
    return Report(
        path=str(path),
        criteria=criteria,
        decided=decided,
        unknown=unknown,
        dependencies=dependencies,
        findings=findings,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    report = validate(args.path)
    if args.json:
        payload = asdict(report)
        payload["errors"] = report.errors
        payload["warnings"] = report.warnings
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(
            f"criteria={report.criteria} decided={report.decided} "
            f"unknown={report.unknown} dependencies={report.dependencies} "
            f"errors={report.errors} warnings={report.warnings}"
        )
        for finding in report.findings:
            print(
                f"{finding.severity.upper()} line {finding.line}: {finding.message}"
            )
    return 1 if report.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
