# DevOps notes

Lasting lessons for the DevOps persona. See the
[team workspace](../workspace.md#persona-notes) for how notes work.

- Canvas portal CI runs only when `canvas-portal/**` or its workflow file
  changes, so docs-only PRs have no checks. Run `ci-paths` to confirm.
- GitHub Pages deploys on push to `main` when `site/**` or
  `qml-hello-wasm/site/**` changes. Merging such a PR changes the live site,
  which needs the Team Lead.
- Repo merge settings (Settings > General > Pull Requests): head branches
  are deleted on merge, and merge commits use the PR title as the subject
  and the PR description as the body. Squash commits still list the
  commits. Sessions can read these with `gh api repos/bbranton/TestProj`
  but the proxy blocks writes, so the Team Lead changes them.
- Merge stacked PRs with a regular merge, bottom first. When the bottom
  branch is auto-deleted, GitHub retargets the next PR to its base, and its
  diff stays clean because the commits are already there. A squash would
  make the next PR show the bottom PR's commits again.
- Two branches: `develop` is the default and integration branch, and
  `main` is live. PRs target `develop`; only the Team Lead merges
  `develop` → `main`. A ruleset on `main` restricts deletion, blocks force
  pushes, and requires a PR (no bypass). Sessions act as the Team Lead's
  GitHub account, so GitHub can't stop a thread merging to `main`; the rule
  in CLAUDE.md does. Read rulesets with `gh api repos/bbranton/TestProj/rulesets`.
- Pages deploys only from `main`; CI runs on PRs and on pushes to `main`
  and `develop`. `ci-paths` compares against `origin/develop` by default.
  Tag each release on `main` so a patch can branch from it (#30).
- Hosting research lives in roadmap D-3, R-13, and R-15: test deploys run
  on Koyeb free plus Neon free (Render free is the fallback), and paid
  production hosting is about $13 to $14 a month plus a domain. Read these
  before any new hosting research; it cost about 20 web fetches in #4.
- The branch rename went `master` to `develop` to `main` across two PRs
  (#29). Confirm a shared name with the Team Lead before editing, and list
  every place it lives first.
- Many PRs append rows to `cost-log.md`, which causes merge conflicts and
  extra "Merge main" commits. Keep shared append-only files to one owner
  thread where possible.

## Open items

- Release plan after Phase 1 deploys: `develop`, `main`, and release tags (#30).
- Docs PRs have no checks. Proposed: a link and requirement-ID check, and a
  screenshot helper for UI PRs. Needs the Team Lead's OK before building.
- Phase 1 test deploy (Koyeb plus Neon, nightly encrypted backup) not set
  up yet; see roadmap Phase 1 step 6.
