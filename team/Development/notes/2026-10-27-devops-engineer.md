# DevOps engineer, 2026-10-27

## Explain the Canvas portal CI workflow (PR #87)

- The Team Lead asked on release PR #76 for a comment saying what
  `.github/workflows/canvas-portal-ci.yml` is for.
- Added a header comment: what the backend and frontend jobs check, when
  the workflow runs (PRs and pushes to `main` and `develop`, only for
  `canvas-portal/**` or the workflow itself), and that it deploys nothing
  and uses no secrets.
- No behavior change: comments only, so no decision needed.

## Peer review of the CI workflow comment (PR #87)

- Fresh DevOps engineer thread, reviewing as peer against `develop@f2354de`.
- Checked that only comments changed (old and new workflow parse to the
  same YAML) and that each line of the header comment matches the jobs,
  triggers, and `paths` filters. Both CI jobs passed on the PR.
- Verdict: Recommend with notes. One optional wording note (F-1): say the
  automatic GitHub token is read-only because of `permissions: contents: read`.
- F-1 was fixed in `a743058` by the owner (comment only). Re-checked the
  fix: verdict now Recommend.

## Peer review of the new-project setup guide (PR #92)

- Fresh DevOps engineer thread, reviewing `d3986f8` (the version refocused
  on setup done outside the repo) against `develop@b94c197`.
- Checked the guide's GitHub steps against the live repo with `gh api`:
  default branch `develop`, the `protected` ruleset on `main` (deletion,
  non-fast-forward, pull request, no bypass), and the merge settings all
  match. No required status checks, so CI needs no web setup.
- Could not read Pages or environment settings (the proxy blocks them).
  No Pages deploy has run from `main` since `develop` became the default.
- Verdict: Changes needed, for one missing step: allow `main` in the
  `github-pages` environment's deployment branches (F-1). Three minor
  findings on branch order, the clone folders, and workflows.
- Told the Team Lead about three live-repo gaps outside the PR: no
  `decision` label, grey persona labels with no description, and a
  disabled `develop` ruleset left over.
- F-1 to F-4 fixed in `f1be7de` by the owner. Re-checked the fixes:
  verdict now Recommend.
