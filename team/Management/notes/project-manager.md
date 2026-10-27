# Management notes

Lasting lessons for the Management persona. See the
[team workspace](../../workspace.md#persona-notes) for how notes work.

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
- Add Backlog items from merged PRs to the roadmap backlog before
  planning the next piece of work, so reviewer follow-ups don't sit
  unread. The Team Lead dropped GitHub issues for review follow-ups
  (2026-10-27) because they left too many loose ends.
- Price hosting per phase, not only for the final deploy. The Team Lead
  wants $0 until real users arrive, so test deploys use free tiers (D-3)
  and the paid host waits for Phase 4. Ask DevOps to research free options
  before offering a paid one.
- A potential data breach never goes on the backlog: it is fixed in the
  PR, or first in the current phase and before the next deploy, tracked in
  Security's register meanwhile. Check that register at every phase
  boundary and before every deploy. Only the Team Lead can delay one.
- Before any deploy that puts real tokens online, the roadmap lists its
  go-live conditions (incident plan, key handling, secret scanning, cookie
  safety on the host's domain, private secrets and backups). A shared
  default domain that isn't on the Public Suffix List makes other tenants
  "same site"; check it when picking a free host.
- The roadmap trailed the other docs during the docs review: #32, #36, #42,
  and #44 were all catch-ups, and moving course colors to Phase 5 took five
  PRs. Bring decisions to the Team Lead before downstream reviews start, and
  send every owner the full list of follow-ups at once.
- Phase 1 grew during the requirements review (filter menu, availability
  dates, card matching, hidden orphaned cards) while R-10 only warned about
  it. Ask for a matching cut or the Team Lead's OK each time.
- Skill scripts in `team/<Team>/scripts/` find the repo root with
  `parents[3]`, the same depth they had in `.claude/skills/<name>/`. Keep
  scripts at that depth, or fix `ROOT` when moving one.
- Finding decisions by approving PRs didn't work for the Team Lead. Raise
  every real decision as a separate decision request, and keep PRs to
  carrying out answered ones.
- Reviewers come from what a PR touches, not from the kind of doc: each
  persona whose area changes reviews it. The Team Lead found Team Lead
  confirmation of every PR's reviewers too slow once PRs were small.
- When a persona is split or renamed, relabel its open issues in the same
  pass. Setting a missing label on an issue creates it, grey and with no
  description, so give it a color and description afterward if they matter.
