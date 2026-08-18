#!/usr/bin/env python3
"""Fetch an OpenSSF project criteria page and generate a structure.md skeleton."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


VALID_STATUSES = {"?", "Met", "Unmet", "N/A"}


@dataclass
class Criterion:
    panel: str
    section: str
    criterion_id: str
    requirement: str
    description: str
    details: str
    page_status: str
    page_justification: str


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def requirement_level(description: str) -> str:
    """Map OpenSSF keywords to the two-level notation used by the template."""
    if re.search(r"\bMUST(?:\s+NOT)?\b", description):
        return "MUST"
    if re.search(r"\bSHOULD(?:\s+NOT)?\b", description):
        return "SHOULD"
    if re.search(r"\bSUGGESTED\b", description):
        return "SHOULD"
    raise ValueError(f"Cannot determine requirement level: {description[:120]}")


def fetch_html(url: str, timeout: int = 30) -> str:
    parsed = urlparse(url)
    if parsed.scheme == "file":
        return Path(parsed.path).read_text(encoding="utf-8")
    response = requests.get(
        url,
        timeout=timeout,
        headers={"User-Agent": "openssf-structure-auditor/1.0"},
    )
    response.raise_for_status()
    return response.text


def _panel_title(heading) -> str:
    title = heading.select_one(".panel-title") if heading is not None else None
    if title is None:
        return "Criteria"
    clone = BeautifulSoup(str(title), "html.parser")
    satisfaction = clone.select_one(".satisfaction")
    if satisfaction is not None:
        satisfaction.decompose()
    return clean_text(clone.get_text(" ", strip=True))


def _criterion_description(row) -> tuple[str, str]:
    desc = row.select_one(".criteria-desc")
    if desc is None:
        desc = row.find_next_sibling("div", class_="criteria-desc")
    if desc is None:
        raise ValueError(f"Criterion {row.get('id')} has no description")
    clone = BeautifulSoup(str(desc), "html.parser")
    details_node = clone.select_one(".details-text")
    details = clean_text(details_node.get_text(" ", strip=True)) if details_node else ""
    for selector in (".details-text", ".details-toggler", "sup"):
        for node in clone.select(selector):
            node.decompose()
    description = clean_text(clone.get_text(" ", strip=True))
    return description, details


def parse_project_page(html: str) -> list[Criterion]:
    soup = BeautifulSoup(html, "html.parser")
    criteria: list[Criterion] = []
    # BadgeApp's HTML places many criterion rows as siblings of panel bodies.
    # Parse globally and associate each row with the nearest preceding headings.
    for row in soup.select(".criterion-data[id]"):
        panel_heading = row.find_previous("div", class_="panel-heading")
        panel_title = _panel_title(panel_heading)
        section_node = row.find_previous("h3")
        section_title = (
            clean_text(section_node.get_text(" ", strip=True))
            if section_node is not None
            else panel_title
        )
        description, details = _criterion_description(row)
        status = row.get("data-status", "?")
        if status not in VALID_STATUSES:
            status = "?"
        criteria.append(
            Criterion(
                panel=panel_title,
                section=section_title,
                criterion_id=row["id"],
                requirement=requirement_level(description),
                description=description,
                details=details,
                page_status=status,
                page_justification=clean_text(row.get("data-justification", "")),
            )
        )
    if not criteria:
        raise ValueError("No OpenSSF criteria were found in the page")
    return criteria


def render_structure(
    criteria: Iterable[Criterion], source_url: str, status_source: str = "unknown"
) -> str:
    lines = [
        "# Symbols",
        "## 项目是否具备选项",
        "[?] 不确定",
        "[Unmet] 未实现",
        "[Met] 已实现",
        "[N/A] 没有这个功能or不需要考虑这一点",
        "",
        "## 项目是否必须满足这一条要求",
        "[SHOULD] 不强制要求",
        "[MUST] 强制要求",
        "",
        "## 做出选项的依据",
        "[dependancy]: 做出选项的依据，用于已经做出选择的问卷内容",
        "三级标题[A][B] A最多有四种选择([?], [Unmet], [Met], [N/A])。如果把[?]替换成其他选项，必须在该条目的最后一行补充[dependancy]，并说明证据。",
        "",
        f"<!-- OpenSSF source: {source_url} -->",
        "",
    ]
    last_panel = None
    last_section = None
    for criterion in criteria:
        if criterion.panel != last_panel:
            lines.extend([f"# {criterion.panel}", ""])
            last_panel = criterion.panel
            last_section = None
        if criterion.section != last_section:
            lines.extend([f"## {criterion.section}", ""])
            last_section = criterion.section
        status = criterion.page_status if status_source == "page" else "?"
        lines.append(f"### [{status}] [{criterion.requirement}]")
        lines.append(f"{criterion.description} [{criterion.criterion_id}]")
        if criterion.details:
            lines.extend(["", criterion.details])
        if status != "?" and criterion.page_justification:
            lines.extend(["", f"[dependancy]: {criterion.page_justification}"])
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def write_new_file(path: Path, content: str, force: bool = False) -> None:
    if path.exists() and not force:
        raise FileExistsError(
            f"Refusing to overwrite existing file: {path}. "
            "Use the existing file as the audit target or pass --force explicitly."
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", required=True, help="OpenSSF project criteria URL")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument(
        "--status-source",
        choices=("unknown", "page"),
        default="unknown",
        help="Start all criteria as unknown, or copy page selections",
    )
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite output. Never use this for a user-maintained structure.md.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        html = fetch_html(args.url, timeout=args.timeout)
        criteria = parse_project_page(html)
        content = render_structure(criteria, args.url, args.status_source)
        write_new_file(args.output, content, force=args.force)
    except Exception as exc:  # CLI boundary
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"generated {args.output} with {len(criteria)} criteria")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
