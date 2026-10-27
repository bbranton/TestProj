---
name: ci-paths
description: Show which GitHub Actions workflows the current branch's changes will trigger, from the workflows' paths filters. Use before opening a PR, when CI didn't run, or when reviewing a CI change.
---

# Check which CI runs

Mostly used by the DevOps engineer persona. Run from the repo root:

```sh
python3 team/Development/scripts/ci_paths.py       # against origin/develop
python3 team/Development/scripts/ci_paths.py origin/x  # against another base
```

It lists each workflow in `.github/workflows/` and whether it runs on the PR
and on push to the branches each workflow names, with the first changed file that matched.

When a PR changes app code but no workflow runs, that's a finding: either
the paths filter is wrong or the code is in the wrong place. A docs-only PR
running no CI is expected.
