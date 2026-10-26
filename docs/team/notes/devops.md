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
- The default branch is `main` (renamed from `master`). Workflow
  `branches:` filters, the `ci-paths` default base, and any deploy
  environment's branch rule must name `main`. Old clones need
  `git branch -m master main && git fetch origin && git branch -u origin/main main`.
- One branch for now: every PR merges to `main`, which is live. After Phase 1
  deploys, the Team Lead wants a release plan: `develop` for next-phase
  work, `main` for what's live, and a tag at each release so a patch can
  branch from it (#30).
