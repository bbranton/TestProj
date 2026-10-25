# DevOps notes

Lasting lessons for the DevOps persona. See the
[team workspace](../workspace.md#persona-notes) for how notes work.

- Canvas portal CI runs only when `canvas-portal/**` or its workflow file
  changes, so docs-only PRs have no checks. Run `ci-paths` to confirm.
- GitHub Pages deploys on push to `master` when `site/**` or
  `qml-hello-wasm/site/**` changes. Merging such a PR changes the live site,
  which needs the Team Lead.
