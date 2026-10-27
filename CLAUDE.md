# Working in TestProj

## Links

- Link to files in the repo from the repo root, starting with `/`, such as
  `[design](/docs/canvas-portal/03-design.md#design-by-phase)`. Don't use
  `../` or file-relative paths. A leading `/` means the repo root, not the
  computer's root: to open a linked file with a file tool, put the repo's
  path in front of it. GitHub and VS Code's Markdown preview read it that
  way. Obsidian, with the repo folder as the vault, should too, but that
  hasn't been tested.
- The one exception is the PR template, whose links show on the PR page and
  so use `../blob/develop/...`.

## Naming

- Never use the project owner's first name anywhere in the repo: files, docs,
  code comments, and commit messages. Refer to them as "Team Lead".

## Team personas

- When asked to act as a persona (Project manager, Requirements engineer, Test engineer, Architect,
  Developer, UI/UX designer, DevOps engineer, Cybersecurity engineer, or CFO), read its file in its team's `personas/` folder
  (see the [team README](/team/README.md)) first, and stay inside what it
  owns.
- Before persona work, read the notes in its team's `notes/` folder
  under `team/<Team>/`.
  Before editing a doc or starting a cross-review, claim it on the board
  described in the [team workspace](/team/workspace.md). Add lasting lessons to the notes
  in the same PR.
- Each persona keeps one daily log per day with work, named
  `YYYY-MM-DD-<persona>.md` in its team's `notes/` folder, such as
  `team/Development/notes/2026-10-27-devops-engineer.md`. Every thread of
  that persona adds to the same file, and only to its own persona's log.
  Any persona can read any log. Record decisions in the format in
  [Daily notes](/team/workspace.md#daily-notes).
- Every PR has at least one reviewer: a fresh thread of the owner's own
  persona reviews it as a peer (for a team thread with no persona, the
  persona that owns most of the changed files). A PR that touches only its owner persona's
  area (its persona file, notes, and daily log, and the docs it owns) needs
  only that peer, unless an "always" rule in the
  [review protocol](/team/review-protocol.md) applies. Another persona's
  files, even in the same team, team scripts and skills, shared files at
  the top of `team/`, and other teams' folders follow the review protocol.
- Security is every persona's job. Raise any risk to Canvas tokens or
  student data you see, in any area, and never leave it for another
  persona to catch. The cybersecurity engineer's view carries the most weight on
  security; see [Security is everyone's job](/team/README.md#security-is-everyones-job).
- When a thread's work is done, report its cost with the `log-cost` skill.
  Don't add rows to `team/Management/cost-log.md` in your own PR: the CFO
  adds reported rows in batches, so the log doesn't cause merge conflicts.
- When asked to review or cross-review a doc or PR, follow the
  [review protocol](/team/review-protocol.md): it says which personas
  review what and how findings are logged. The PR's author picks its
  reviewers by what the PR touches.
- Personas recommend; the Team Lead has the final say on every decision
  and can change any PR's reviewers. Every real decision goes to the Team
  Lead as a decision request, and PRs only carry out decisions already
  made; see the [review protocol](/team/review-protocol.md#decisions-are-separate-from-merging).
- A PR that changes a process rule fixes every file that states it, in the
  same PR, and lists them; see the
  [ripple check](/team/review-protocol.md#ripple-check-for-process-rules).

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
  [Requirements by phase](/docs/canvas-portal/02-requirements.md#requirements-by-phase).
  Anything marked a later phase in any doc under `docs/canvas-portal/` is out
  of scope, even when the design or UI specification already describes it.
  Ask the Team Lead before building it.
- The design doc covers Phases 0 to 4 only. Its
  [Design by phase](/docs/canvas-portal/03-design.md#design-by-phase) table
  says which tables, endpoints, and components each phase builds.
- Every implementation PR lists the requirement IDs it implements in its
  description.
