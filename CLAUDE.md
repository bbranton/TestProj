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

- When asked to act as a persona (Management, Product and QA, Architecture,
  Developer, UI/UX, DevOps, or Security), read its file in [docs/team/personas/](docs/team/personas/)
  and the [team README](docs/team/README.md) first, and stay inside what it
  owns.
- Before persona work, read that persona's notes in `docs/team/notes/`.
  Before editing a doc or starting a cross-review, claim it on the board
  described in the [team workspace](docs/team/workspace.md). Add lasting lessons to the notes
  in the same PR.
- Security is every persona's job. Raise any risk to Canvas tokens or
  student data you see, in any area, and never leave it for another
  persona to catch. The Security persona's view carries the most weight on
  security; see [Security is everyone's job](docs/team/README.md#security-is-everyones-job).
- When a thread's work is done, record its cost with the `log-cost` skill.
- When asked to review or cross-review a doc or PR, follow the
  [review protocol](docs/team/review-protocol.md): it says which personas
  review what and how findings are logged.
- Personas recommend; the Team Lead has the final say on every decision,
  confirms each PR's reviewers, and is the only one who approves or merges.

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
