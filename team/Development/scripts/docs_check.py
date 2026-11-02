#!/usr/bin/env python3
"""Check the repo's Markdown for broken links and undefined requirement IDs.

  docs_check.py   check every tracked .md file; exit 1 on any problem

Links: every [text](target) whose target is in the repo, written from the
repo root (/team/README.md), relative to the file, or as the PR template's
../blob/develop/... form, must name a file or
folder that exists, and a #fragment must match a heading or an explicit
anchor in that file. Web links (http:, mailto:) aren't fetched, and
reference-style links ([text][ref]) and percent-encoded paths aren't
checked; neither is used in the repo.

Requirement IDs: every FR- and NFR- ID named in docs/canvas-portal/ must be
defined in the requirement tables of the requirements doc. A row marked
*(Removed: ...)* doesn't count, except inside the requirements doc, which
names removed IDs to explain them. An ID with a letter suffix, such as
FR-12a, is reported too. Change logs are skipped, since they may name IDs
that were removed.

Docs split by phase: any doc may be one file (02-requirements.md) or one
file per phase (02-requirements_phase0.md, 02-requirements_phase1.md, and
so on), or both while a split is under way. doc_files() finds them, so a
split needs no change here. The requirements doc is every one of its files
together: an ID defined in any of them counts.

Runs in CI from .github/workflows/docs-check.yml. Standard library only.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DOCS = ROOT / "docs" / "canvas-portal"
REQS = "02-requirements.md"  # the doc's name, before any phase split
REQ_ROW = re.compile(r"^\|\s*((?:FR|NFR)-\d+)\s*\|\s*(\*?\(Removed)?")
REQ_ID = re.compile(r"\b(?:FR|NFR)-\d+[A-Za-z]*\b")
LINK = re.compile(r"(?<!\\)\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
HEADING = re.compile(r"^#{1,6}\s+(.*?)\s*#*\s*$")
BLOB = re.compile(r"^(?:\.\./)+blob/[^/]+/")  # the PR template's links
ANCHOR = re.compile(r"<a\s+(?:name|id)=\"([^\"]+)\"")


def tracked_markdown():
    out = subprocess.run(
        ["git", "ls-files", "*.md"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout
    return [ROOT / f for f in out.splitlines() if f]


def prose_lines(path, keep_code=False):
    """(line number, text) for each line outside fenced code blocks, with
    inline code removed unless keep_code, so examples in code aren't
    checked."""
    fence = None  # the marker that opened the current fence
    for n, line in enumerate(path.read_text().splitlines(), 1):
        m = FENCE.match(line)
        if m and fence is None:
            fence = m.group(1)
            continue
        if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
            fence = None
            continue
        if fence is None:
            yield n, line if keep_code else re.sub(r"`[^`]*`", "", line)


def slug(heading):
    """GitHub's anchor for a heading."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading)  # links keep their text
    text = re.sub(r"<[^>]+>", "", text).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


_anchors = {}
checked = {"links": 0, "IDs": 0}  # so "0 problems" can't mean "checked nothing"


def anchors(path):
    """Every #fragment a link may use for this file."""
    if path not in _anchors:
        found, seen = set(), {}
        # Inline code in a heading keeps its text in the anchor:
        # "Read from `develop`" is #read-from-develop.
        for _, line in prose_lines(path, keep_code=True):
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
            checked["links"] += 1
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


def doc_files(name):
    """The files of one doc in docs/canvas-portal/: name itself, such as
    02-requirements.md, and its phase files, 02-requirements_phase0.md and
    up, in phase order. Empty if the doc has neither."""
    stem = name.removesuffix(".md")
    numbered = {}
    for path in DOCS.glob(f"{stem}_phase*.md"):
        if m := re.fullmatch(re.escape(stem) + r"_phase(\d+)\.md", path.name):
            numbered[path] = int(m.group(1))
    phases = sorted(numbered, key=numbered.get)
    whole = DOCS / name
    return ([whole] if whole.exists() else []) + phases


def doc_label(name):
    """How a message names a doc that may be split: 02-requirements*.md."""
    return name.removesuffix(".md") + "*.md"


def requirement_rows():
    """({current IDs}, {removed IDs}) from the requirement tables of every
    file of the requirements doc. An ID current in one file and removed in
    another counts as current."""
    current, removed = set(), set()
    for path in doc_files(REQS):
        for line in path.read_text().splitlines():
            if m := REQ_ROW.match(line):
                (removed if m.group(2) else current).add(m.group(1))
    return current, removed - current


def check_requirement_ids(current, removed):
    problems = []
    req_files = doc_files(REQS)
    if not req_files:
        return [f"{DOCS.relative_to(ROOT)}: no requirements doc "
                f"({REQS} or its _phaseN.md files)"]
    for path in sorted(DOCS.glob("*.md")):
        allowed = current | removed if path in req_files else current
        for n, line in prose_lines(path):
            if line.startswith("## Change log"):
                break
            named = set(REQ_ID.findall(line))
            checked["IDs"] += len(named)
            for req_id in sorted(named - allowed):
                if req_id in removed:
                    why = f"was removed in {doc_label(REQS)}"
                elif not req_id.split("-")[1].isdigit():
                    why = "isn't a requirement ID (IDs are plain numbers)"
                else:
                    why = f"isn't defined in {doc_label(REQS)}"
                problems.append(f"{path.relative_to(ROOT)}:{n}: {req_id} {why}")
    return problems


def main():
    problems = []
    files = tracked_markdown()
    for path in files:
        problems += check_links(path)
    problems += check_requirement_ids(*requirement_rows())
    for p in problems:
        print(p)
    print(f"Checked {len(files)} Markdown files, {checked['links']} repo links, "
          f"and {checked['IDs']} requirement ID mentions: {len(problems)} problem(s).")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
