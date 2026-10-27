# DevOps engineer, 2026-10-27

## Explain the Canvas portal CI workflow (PR #87)

- The Team Lead asked on release PR #76 for a comment saying what
  `.github/workflows/canvas-portal-ci.yml` is for.
- Added a header comment: what the backend and frontend jobs check, when
  the workflow runs (PRs and pushes to `main` and `develop`, only for
  `canvas-portal/**` or the workflow itself), and that it deploys nothing
  and uses no secrets.
- No behavior change: comments only, so no decision needed.
