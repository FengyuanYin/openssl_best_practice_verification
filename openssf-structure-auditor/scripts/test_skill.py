#!/usr/bin/env python3
"""Deterministic tests for the OpenSSF structure auditor scripts."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

import evaluate_against_truth  # noqa: E402
import fetch_structure  # noqa: E402
import validate_structure  # noqa: E402


FIXTURE_HTML = """
<html><body><div class="panel panel-primary">
<div class="panel-heading" id="analysis"><h2 class="panel-title">Analysis <span class="satisfaction">0/2</span></h2></div>
<ul><li class="list-group-item"><h3>Static code analysis</h3>
<div id="static_analysis_common_vulnerabilities" class="row criterion-data" data-status="Met" data-justification="gosec in CI">
<div class="criteria-radio">Met</div></div>
<div class="criteria-desc"><br/>The project MUST use a static analysis tool to look for common vulnerabilities.
<sup>[static_analysis_common_vulnerabilities]</sup><button class="details-toggler">Details</button>
<div class="details-text">Use a FLOSS security analyzer.</div></div></li>
<li class="list-group-item"><h3>Dynamic code analysis</h3>
<div id="dynamic_analysis_unsafe" class="row criterion-data" data-status="N/A" data-justification="Go-only release">
<div class="criteria-desc"><br/>If the project uses a memory-unsafe language, it MUST use a dynamic tool.
<sup>[dynamic_analysis_unsafe]</sup></div></div></li></ul></div></body></html>
"""


class SkillTests(unittest.TestCase):
    def test_parse_and_render(self):
        criteria = fetch_structure.parse_project_page(FIXTURE_HTML)
        self.assertEqual(2, len(criteria))
        rendered = fetch_structure.render_structure(criteria, "https://example.test/project/silver", "unknown")
        self.assertIn("# Analysis", rendered)
        self.assertIn("### [?] [MUST]", rendered)
        self.assertIn("[dynamic_analysis_unsafe]", rendered)

    def test_page_status_and_dependency(self):
        criteria = fetch_structure.parse_project_page(FIXTURE_HTML)
        rendered = fetch_structure.render_structure(criteria, "https://example.test/project/silver", "page")
        self.assertIn("### [Met] [MUST]", rendered)
        self.assertIn("[dependancy]: gosec in CI", rendered)

    def test_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "structure.md"
            target.write_text("original", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                fetch_structure.write_new_file(target, "replacement")
            self.assertEqual("original", target.read_text(encoding="utf-8"))

    def test_truth_template_validates(self):
        truth = SKILL_DIR / "assets" / "structure-template.md"
        report = validate_structure.validate(truth)
        self.assertEqual([], [f for f in report.findings if f.severity == "error"])
        self.assertEqual(report.decided, report.dependencies)

    def test_missing_dependency_is_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "structure.md"
            target.write_text("### [Met] [MUST]\nA project MUST do a thing. [thing]\n", encoding="utf-8")
            report = validate_structure.validate(target)
            self.assertGreater(report.errors, 0)

    def test_truth_self_evaluation(self):
        truth = SKILL_DIR / "assets" / "structure-template.md"
        metrics = evaluate_against_truth.evaluate(truth, truth)
        self.assertEqual(1.0, metrics["structural_recall"])
        self.assertEqual(1.0, metrics["decision_recall"])
        self.assertEqual(1.0, metrics["status_agreement"])
        self.assertEqual(1.0, metrics["dependency_coverage"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
