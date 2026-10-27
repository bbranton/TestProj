#!/usr/bin/env python3
"""Check the repo's Markdown for broken links and undefined requirement IDs.

  docs_check.py   check every tracked .md file; exit 1 on any problem

Links: every [text](target) whose target is in the repo, written from the
repo root (/team/README.md), relative to the file, or as the PR template's
../blob/develop/... form, must name a file or
folder that exists, and a #fragment must match a heading or an explicit
anchor in that file. Web links (http:, mailto:) aren't fetched.

Requirement IDs: every FR- and NFR- ID named in docs/canvas-portal/ must be
defined in the requirement tables of 02-requirements.md. Change logs are
skipped, since they may name IDs that were removed.

Runs in CI from .github/workflows/docs-check.yml. Standard library only.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DOCS = ROOT / "docs" / "canvas-portal"
REQS = DOCS / "02-requirements.md"
REQ_ROW = re.compile(r"^\|\s*((?:FR|NFR)-\d+)\s*\|")
REQ_ID = re.compile(r"\b(?:FR|NFR)-\d+\b")
LINK = re.compile(r"(?<!\\)\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
FENCE = re.compile(r"^\s*(```|~~~)")
HEADING = re.compile(r"^#{1,6}\s+(.*?)\s*#*\s*$")
BLOB = re.compile(r"^(?:\.\./)+blob/[^/]+/")  # the PR template's links
ANCHOR = re.compile(r"<a\s+(?:name|id)=\"([^\"]+)\"")


def tracked_markdown():
    out = subprocess.run(
        ["git", "ls-files", "*.md"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout
    return [ROOT / f for f in out.splitlines() if f]


def prose_lines(path):
    """(line number, text) for each line outside fenced code blocks, with
    inline code removed, so examples in code aren't checked."""
    in_fence = False
    for n, line in enumerate(path.read_text().splitlines(), 1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            yield n, re.sub(r"`[^`]*`", "", line)


def slug(heading):
    """GitHub's anchor for a heading."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading)  # links keep their text
    text = re.sub(r"<[^>]+>", "", text).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


_anchors = {}


def anchors(path):
    """Every #fragment a link may use for this file."""
    if path not in _anchors:
        found, seen = set(), {}
        for _, line in prose_lines(path):
            found.update(ANCHOR.findall(line))
            m = HEADING.match(line)
            if m:
                base = slug(m.group(1))
                count = seen.get(base, 0)
                seen[base] = count + 1
                found.add(base if count == 0 else f"{base}-{count}")
        _anchors[path] = found
    return _anchors[path]


def check_links(path):
    problems = []
    for n, line in prose_lines(path):
        for target in LINK.findall(line):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                continue  # http:, https:, mailto: and the like
            file_part, _, fragment = target.partition("#")
            file_part = BLOB.sub("/", file_part)
            if not file_part:
                dest = path
            elif file_part.startswith("/"):
                dest = ROOT / file_part.lstrip("/")
            else:
                dest = path.parent / file_part
            dest = dest.resolve()
            where = f"{path.relative_to(ROOT)}:{n}"
            if not dest.is_relative_to(ROOT):
                problems.append(f"{where}: link leaves the repo: {target}")
            elif not dest.exists():
                problems.append(f"{where}: no such file: {target}")
            elif fragment and dest.suffix == ".md" and fragment not in anchors(dest):
                problems.append(f"{where}: no heading for #{fragment} in {target}")
    return problems


def defined_requirements():
    return {m.group(1) for line in REQS.read_text().splitlines()
            if (m := REQ_ROW.match(line))}


def check_requirement_ids(defined):
    problems = []
    for path in sorted(DOCS.glob("*.md")):
        for n, line in prose_lines(path):
            if line.startswith("## Change log"):
                break
            for req_id in sorted(set(REQ_ID.findall(line)) - defined):
                problems.append(f"{path.relative_to(ROOT)}:{n}: {req_id} isn't defined in 02-requirements.md")
    return problems


def main():
    problems = []
    files = tracked_markdown()
    for path in files:
        problems += check_links(path)
    problems += check_requirement_ids(defined_requirements())
    for p in problems:
        print(p)
    print(f"Checked {len(files)} Markdown files: {len(problems)} problem(s).")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
