#!/usr/bin/env python3
"""Say which GitHub Actions workflows a branch's changes will trigger.

  ci_paths.py [BASE]   compare HEAD with BASE (default origin/develop)

Reads the `paths:` filters in .github/workflows/*.yml. Only the one-line
form `paths: ["a/**", "b"]` is understood, which is what this repo uses.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WORKFLOWS = ROOT / ".github" / "workflows"


def changed_files(base):
    out = subprocess.run(
        ["git", "diff", "--name-only", f"{base}...HEAD"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    ).stdout
    return [f for f in out.splitlines() if f]


def glob_to_regex(glob):
    parts = re.split(r"(\*\*/?|\*)", glob)
    out = ""
    for part in parts:
        if part in ("**", "**/"):
            out += ".*"
        elif part == "*":
            out += "[^/]*"
        else:
            out += re.escape(part)
    return re.compile(out + "$")


def triggers(path):
    """{event: [path globs] or None for no filter} for push and pull_request."""
    found, event = {}, None
    for line in path.read_text().splitlines():
        m = re.match(r"^  (push|pull_request|workflow_dispatch)\s*:", line)
        if m:
            event = m.group(1)
            found[event] = None
        elif re.match(r"^\S", line):
            event = None
        elif event:
            p = re.match(r"^\s+paths:\s*\[(.*)\]", line)
            if p:
                found[event] = [g.strip().strip("\"'") for g in p.group(1).split(",")]
    return found


def main(args):
    base = args[0] if args else "origin/develop"
    files = changed_files(base)
    print(f"{len(files)} file(s) changed since {base}.")
    for wf in sorted(WORKFLOWS.glob("*.y*ml")):
        for event, globs in triggers(wf).items():
            if event == "workflow_dispatch":
                continue
            when = "on this PR" if event == "pull_request" else "on push to develop"
            if globs is None:
                print(f"  {wf.name}: runs {when} (no paths filter)")
                continue
            hits = [f for f in files if any(glob_to_regex(g).match(f) for g in globs)]
            verdict = f"runs {when}, matched by {hits[0]}" if hits else f"does not run {when}"
            print(f"  {wf.name}: {verdict}")


if __name__ == "__main__":
    main(sys.argv[1:])
