# Working in TestProj

## Pull requests

- Any PR that changes the UI (pages, styles, app screens) must include
  screenshots of each changed page in the PR description. Commit them under
  `docs/screenshots/pr-<number>/` and embed them with
  `https://raw.githubusercontent.com/bbranton/TestProj/<commit-sha>/docs/screenshots/pr-<number>/<file>.png`.
  Include a phone-width shot when the layout is responsive.

## Naming

- Never use the project owner's first name anywhere in the repo: files, docs,
  code comments, and commit messages. Refer to them as "Team Lead".

## Team personas

- When asked to act as a persona (Management, Requirements engineer, Test engineer, Architecture,
  Developer, UI/UX, DevOps, Security, or CFO), read its file in its team's `personas/` folder
  (see the [team README](team/README.md)) first, and stay inside what it
  owns.
- Before persona work, read the notes in its team's `notes/` folder
  under `team/<Team>/`.
  Before editing a doc or starting a cross-review, claim it on the board
  described in the [team workspace](team/workspace.md). Add lasting lessons to the notes
  in the same PR.
- Each team may freely update its own folder, `team/<Team>/` (`notes/`,
  `personas/`, `scripts/`), through a PR like any other change. Shared
  files at the top of `team/` and other teams' folders follow the
  [review protocol](team/review-protocol.md).
- Security is every persona's job. Raise any risk to Canvas tokens or
  student data you see, in any area, and never leave it for another
  persona to catch. The Security persona's view carries the most weight on
  security; see [Security is everyone's job](team/README.md#security-is-everyones-job).
- When a thread's work is done, report its cost with the `log-cost` skill.
  Only the CFO persona edits `team/Finance/cost-log.md`.
- When asked to review or cross-review a doc or PR, follow the
  [review protocol](team/review-protocol.md): it says which personas
  review what and how findings are logged.
- Personas recommend; the Team Lead has the final say on every decision
  and confirms each PR's reviewers.

## Branches

- `develop` is the default branch and the integration branch. Every PR
  targets `develop`, and a thread may merge its own PR into `develop` once
  its confirmed reviewers recommend it.
- Still open a PR for every change to `develop`, so the Team Lead can see
  the diff. Assign the Team Lead, but don't request their review. Merge it
  yourself and post the PR link in the thread. Review requests to the Team
  Lead are only for the `develop` → `main` release PR.
- `main` is what's live. Never open, approve, or merge a PR into `main`.
  Only the Team Lead opens and merges the `develop` → `main` release PR.
- Never force-push or delete `main` or `develop`.

## Canvas portal phases

- The current phase is **Phase 1** (read-only viewer). The Team Lead
  changes this line when a new phase starts.
- Build only the requirements listed for the current phase in
  [Requirements by phase](docs/canvas-portal/02-requirements.md#requirements-by-phase).
  Anything marked a later phase in any doc under `docs/canvas-portal/` is out
  of scope, even when the design or UI specification already describes it.
  Ask the Team Lead before building it.
- The design doc covers Phases 0 to 4 only. Its
  [Design by phase](docs/canvas-portal/03-design.md#design-by-phase) table
  says which tables, endpoints, and components each phase builds.
- Every implementation PR lists the requirement IDs it implements in its
  description.
