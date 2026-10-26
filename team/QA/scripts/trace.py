#!/usr/bin/env python3
"""Trace canvas portal requirement IDs through the docs and code.

  trace.py FR-12 [NFR-10 ...]   where each ID is defined, designed, specified, tested, and coded
  trace.py --untested [PHASE]   requirements (in PHASE, if given) that no test procedure names
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DOCS = ROOT / "docs" / "canvas-portal"
REQS = DOCS / "02-requirements.md"
TRACE_DOCS = ["03-design.md", "04-ui-specification.md", "05-test-plan.md"]
CODE = ROOT / "canvas-portal"
CODE_SUFFIXES = {".py", ".ts", ".tsx", ".js", ".jsx"}
ROW = re.compile(r"^\|\s*((?:FR|NFR)-\d+)\s*\|(.*)\|\s*$")
RANGE = re.compile(r"\b((?:FR|NFR))-(\d+) to (?:\1-)?(\d+)\b")


def body(path):
    """Doc text without its change log, which mentions IDs that aren't traced."""
    text = path.read_text()
    return text.split("\n## Change log", 1)[0]


def requirements():
    """{id: (text, phase)} from the requirement tables."""
    found = {}
    for line in body(REQS).splitlines():
        m = ROW.match(line)
        if m:
            cells = [c.strip() for c in m.group(2).split("|")]
            found[m.group(1)] = (cells[0], cells[-1])
    return found


def ids_named(text):
    """Every FR/NFR ID a text names, with "FR-40 to FR-44" ranges expanded."""
    ids = set(re.findall(r"\b(?:FR|NFR)-\d+\b", text))
    for kind, lo, hi in RANGE.findall(text):
        ids.update(f"{kind}-{n}" for n in range(int(lo), int(hi) + 1))
    return ids


def mentions(req_id, path):
    hits = []
    for n, line in enumerate(path.read_text().splitlines(), 1):
        if line.startswith("## Change log"):
            break
        if req_id in ids_named(line):
            hits.append((n, line.strip()))
    return hits


def trace(req_id, reqs):
    text, phase = reqs.get(req_id, ("(not defined in 02-requirements.md)", "?"))
    print(f"{req_id} (Phase {phase}): {text}")
    for name in TRACE_DOCS:
        hits = mentions(req_id, DOCS / name)
        print(f"  {name}: {len(hits)} mention(s)")
        for n, line in hits[:5]:
            print(f"    {n}: {line[:110]}")
    code_hits = [
        p.relative_to(ROOT)
        for p in CODE.rglob("*")
        if p.suffix in CODE_SUFFIXES and "node_modules" not in p.parts
        and re.search(rf"\b{req_id}\b", p.read_text(errors="ignore"))
    ]
    print(f"  code: {', '.join(map(str, code_hits)) or 'none'}")


def untested(reqs, phase):
    tested = ids_named(body(DOCS / "05-test-plan.md"))
    missing = [
        (i, p) for i, (_, p) in reqs.items()
        if i not in tested and (phase is None or p == phase)
    ]
    for i, p in missing:
        print(f"{i} (Phase {p}): {reqs[i][0][:100]}")
    print(f"{len(missing)} requirement(s) with no test procedure.")


def main(args):
    if not args:
        sys.exit(__doc__)
    reqs = requirements()
    if args[0] == "--untested":
        untested(reqs, args[1] if len(args) > 1 else None)
        return
    for req_id in args:
        trace(req_id.upper(), reqs)


if __name__ == "__main__":
    main(sys.argv[1:])
