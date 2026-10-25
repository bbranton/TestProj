# Management notes

Lasting lessons for the Management persona. See the
[team workspace](../workspace.md#persona-notes) for how notes work.

- The current phase is the line in [CLAUDE.md](../../../CLAUDE.md). Only the
  Team Lead changes it, so a phase move is a request to them, never an edit.
- The design covers Phases 0 to 4 only. Work for Phase 5 and later needs a
  design PR before anyone builds it.
- Each phase's work list in the roadmap names every requirement that the
  requirements' *Requirements by phase* index puts in that phase. Check the
  two against each other in every roadmap PR; the first review found a third
  of Phase 1 missing from the roadmap.
- Each later phase lists what must be decided "Before it starts", so a
  decision is asked for before the phase that needs it, not during it.
- Exit criteria name exact test steps that can run in that phase, such as
  "TP-14 steps 3 and 4". "The Phase 1 steps of TP-10" failed review
  because the test plan didn't mark its steps by phase.
