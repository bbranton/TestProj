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

## Canvas portal phases

- The current phase is **Phase 0** (decisions and setup). The Team Lead
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
