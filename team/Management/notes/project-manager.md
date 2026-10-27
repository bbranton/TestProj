# Project manager notes

Lasting lessons for the project manager persona. See the
[team workspace](/team/workspace.md#persona-notes) for how notes work.

- The current phase is the line in [CLAUDE.md](/CLAUDE.md). Only the
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
- As soon as the Team Lead sends a deferred finding to the backlog, add
  it to the roadmap in a small PR of its own, so reviewer follow-ups don't
  sit unread (Team Lead, 2026-10-27, #89). Answers that arrive together
  can share one PR, to save review threads.
  Each finding outside the current phase or too big for its PR is its own
  decision request: the Team Lead picks fix it in this PR, fix it now in
  a separate PR, a GitHub issue, or the backlog (2026-10-27, #88, #89).
  Issues alone had left too many loose ends, and the backlog alone parked
  work without the Team Lead's say. A later-phase finding fixed now grows
  the current phase, so log it under the phase scope budget.
- Price hosting per phase, not only for the final deploy. The Team Lead
  wants $0 until real users arrive, so test deploys use free tiers (D-3)
  and the paid host waits for Phase 4. Ask the DevOps engineer to research free options
  before offering a paid one.
- Issues opened under the old follow-up rule stay open until done (Team
  Lead, 2026-10-27), so check open issues as well as the roadmap backlog
  when planning.
- Check the cybersecurity engineer's
  [security register](/team/QA/notes/cybersecurity-engineer.md#security-register)
  at every phase boundary and before every deploy; breach handling is in
  [Potential data breach](/team/QA/personas/cybersecurity-engineer.md#potential-data-breach).
- The roadmap applies team rules too (risk ratings, the backlog, step 6
  gates), but the ripple check's search list leaves out `docs/` apart
  from the glossary. When a ripple check covers a rule the project manager
  uses, search `01-roadmap.md` as well (#113, X-1).
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
- Every PR has at least one reviewer: a fresh thread of the owner's own
  persona as a peer, even for an own-area PR (2026-10-27, #82). When a
  team thread owns a PR, the project manager is often the peer, since it owns most
  shared process files. Budget one reviewer thread for every PR.
- When a persona is split or renamed, relabel its open issues in the same
  pass. Setting a missing label on an issue creates it, grey and with no
  description, so give it a color and description afterward if they matter.
- A persona rename isn't done until the `persona:` issue labels and the
  prose headers of other personas' files (such as the cost log's intro)
  match. Grep for the old name outside change logs, daily logs, and old
  finding IDs, and check the labels on open issues (#83).
- Two retros called on the same day collide on the `retro` skill's
  paths, which are named by date alone. Give each a suffix, such as
  `2026-10-27-docs` and `2026-10-27-process`, for both the feedback folder
  and the note. When combining, merge suggestions that ask for the same
  change into one decision request, and send points outside the retro's
  topic to the other retro (2026-10-27).
- A process rule lives in several files, and #86, #88, #89, and #91 each
  found one still stating the old rule. Run the
  [ripple check](/team/review-protocol.md#ripple-check-for-process-rules)
  on every process PR, and bring the owners of the matching files in
  before review, not after (Team Lead, 2026-10-27, #96).
