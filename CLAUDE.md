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
- Each persona keeps one daily log per day with work, named
  `YYYY-MM-DD-<persona>.md` in its team's `notes/` folder, such as
  `team/Development/notes/2026-10-27-devops-engineer.md`. Every thread of
  that persona adds to the same file, and only to its own persona's log.
  Any persona can read any log. Record decisions in the format in
  [Daily notes](team/workspace.md#daily-notes).
- A PR that touches only its owner persona's area (its persona file,
  notes, and daily log, and the docs it owns) needs no reviewers, unless an
  "always" rule in the [review protocol](team/review-protocol.md) applies.
  Another persona's files, even in the same team, team scripts and skills,
  shared files at the top of `team/`, and other teams' folders follow the
  review protocol.
- Security is every persona's job. Raise any risk to Canvas tokens or
  student data you see, in any area, and never leave it for another
  persona to catch. The Security persona's view carries the most weight on
  security; see [Security is everyone's job](team/README.md#security-is-everyones-job).
- When a thread's work is done, report its cost with the `log-cost` skill.
  Don't add rows to `team/Management/cost-log.md` in your own PR: the CFO
  adds reported rows in batches, so the log doesn't cause merge conflicts.
- When asked to review or cross-review a doc or PR, follow the
  [review protocol](team/review-protocol.md): it says which personas
  review what and how findings are logged. The PR's author picks its
  reviewers by what the PR touches.
- Personas recommend; the Team Lead has the final say on every decision
  and can change any PR's reviewers. Every real decision goes to the Team
  Lead as a decision request, and PRs only carry out decisions already
  made; see the [review protocol](team/review-protocol.md#decisions-are-separate-from-merging).

## Branches

- `develop` is the default branch and the integration branch. Every PR
  targets `develop`, and a thread may merge its own PR into `develop` once
  its reviewers recommend it.
- Still open a PR for every change to `develop`, so the Team Lead can see
  the diff. Assign the Team Lead, but don't request their review. Merge it
  yourself and post the PR link in the thread. The Team Lead reviews only
  the `develop` → `main` release PR.
- `main` is what's live. The only PR into `main` is the `develop` → `main`
  release PR. Any persona may open it, assigning the Team Lead
  and summarizing everything merged since `main`. Never approve or merge
  it: only the Team Lead merges into `main`.
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
