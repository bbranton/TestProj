#!/usr/bin/env python3
"""Tests for docs_check.py: each problem it should catch is caught, and
nothing it should skip is reported. Builds a small repo in a temp folder.

  python3 -m unittest discover -s team/Development/scripts -p "test_*.py"

Standard library only. Runs in CI from .github/workflows/docs-check.yml.
"""
import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path

import docs_check

REQUIREMENTS = """\
# Requirements

| ID | Requirement | Phase |
|----|-------------|-------|
| FR-1 | Connect to Canvas. | 1 |
| FR-2 | *(Removed: no table view.)* | n/a |
| NFR-1 | Fast. | 1 |

FR-2 is named here to explain its removal.

## Change log

| Date | Change |
|------|--------|
| 2026-10-27 | Removed FR-2 and FR-99. |
"""

TARGET = """\
# Target

## Read from `develop`

## Plain heading

## Plain heading

<a id="custom"></a>
"""


class DocsCheckTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.write("docs/canvas-portal/02-requirements.md", REQUIREMENTS)
        self.write("team/target.md", TARGET)
        self.saved = docs_check.ROOT, docs_check.DOCS, docs_check.REQS
        docs_check.ROOT = self.root
        docs_check.DOCS = self.root / "docs" / "canvas-portal"
        docs_check.REQS = docs_check.DOCS / "02-requirements.md"
        docs_check._anchors.clear()

    def tearDown(self):
        docs_check.ROOT, docs_check.DOCS, docs_check.REQS = self.saved
        docs_check._anchors.clear()
        self.tmp.cleanup()

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(text))
        return path

    def links(self, text, name="team/page.md"):
        return docs_check.check_links(self.write(name, text))

    def ids(self, text):
        self.write("docs/canvas-portal/03-design.md", text)
        return docs_check.check_requirement_ids(*docs_check.requirement_rows())

    # Links that must pass

    def test_good_links_pass(self):
        self.assertEqual(self.links("""\
            [root](/team/target.md) [relative](target.md) [folder](/team/)
            [code heading](/team/target.md#read-from-develop)
            [second duplicate](/team/target.md#plain-heading-1)
            [explicit anchor](/team/target.md#custom)
            [same file](#title)
            [web](https://example.com/missing) [mail](mailto:a@b.c)

            # Title
            """), [])

    def test_pr_template_blob_links_pass(self):
        self.assertEqual(self.links(
            "[x](../blob/develop/team/target.md#plain-heading)\n",
            ".github/pull_request_template.md"), [])

    def test_links_in_code_are_skipped(self):
        self.assertEqual(self.links("""\
            `[x](/team/nope.md)`

            ```
            [y](/team/nope.md)
            ```
            """), [])

    # Links that must fail

    def test_missing_file(self):
        [p] = self.links("[x](/team/nope.md)\n")
        self.assertIn("no such file: /team/nope.md", p)

    def test_missing_heading(self):
        [p] = self.links("[x](/team/target.md#not-there)\n")
        self.assertIn("no heading for #not-there", p)

    def test_bad_blob_link(self):
        [p] = self.links("[x](../blob/develop/team/nope.md)\n",
                         ".github/pull_request_template.md")
        self.assertIn("no such file", p)

    def test_link_leaving_the_repo(self):
        [p] = self.links("[x](../../../outside.md)\n")
        self.assertIn("leaves the repo", p)

    # Requirement IDs

    def test_defined_ids_pass(self):
        self.assertEqual(self.ids("FR-1 and NFR-1, and `FR-77` in code.\n"), [])

    def test_undefined_id(self):
        [p] = self.ids("See FR-9999.\n")
        self.assertIn("FR-9999 isn't defined", p)

    def test_removed_id(self):
        [p] = self.ids("The table view (FR-2).\n")
        self.assertIn("FR-2 was removed", p)

    def test_suffixed_id(self):
        [p] = self.ids("See FR-1a.\n")
        self.assertIn("FR-1a isn't a requirement ID", p)

    def test_change_log_is_skipped(self):
        self.assertEqual(self.ids("Text.\n\n## Change log\n\nDropped FR-99.\n"), [])

    # The whole run

    def test_main_reports_and_fails(self):
        self.write("team/page.md", "[x](/team/nope.md)\n")
        subprocess.run(["git", "init", "-q"], cwd=self.root, check=True)
        subprocess.run(["git", "add", "."], cwd=self.root, check=True)
        self.assertEqual(docs_check.main(), 1)


if __name__ == "__main__":
    unittest.main()
