# Developer notes

Lasting lessons for the Developer persona. See the
[team workspace](/team/workspace.md#persona-notes) for how notes work.

- Every implementation PR lists the requirement IDs it implements. Run
  `trace-requirement` on them to confirm each ID exists, is in the current
  phase, and has a test.
- Backend tests run with `pytest` in `canvas-portal/backend` after
  `pip install -e ".[dev]"`, the same as CI.
- The design's later-phase sections are not a to-do list. Build only what
  *Design by phase* lists for the current phase.
