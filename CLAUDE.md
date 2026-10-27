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
- **Library paths start with `Library:`** (Team Lead, 2026-10-27). The
  Library is the project's shared files, outside the repo. Write a path
  there as `Library:` and then the path from the Library's root as code
  text, such as Library: `costs/cost-log.md`. Never make it a link, and
  never start it with `/`, so it can't be mistaken for a repo path. So: a
  link is in the repo, and `Library:` is in the Library. In a project
  thread the Library is the folder `/mnt/project-files/`, so Library:
  `costs/cost-log.md` is `/mnt/project-files/costs/cost-log.md`; a session
  outside the project can't open it.

## Naming

- Never use the project owner's first name anywhere in the repo: files, docs,
  code comments, and commit messages. Refer to them as "Team Lead".

## Team personas

The personas are Project manager, Requirements engineer, Test engineer,
Architect, Developer, UI/UX designer, DevOps engineer, Cybersecurity
engineer, and CFO.

Personas recommend; the Team Lead has the final say on every decision,
including any PR's reviewers.

### Rule index

Each team rule is stated once, in its home. This list names each rule and
links to the home, which says what to do. Read the home before you act on
a rule. The security and breach rules apply to every thread, with or
without a persona.

- Repo and Library paths: [Links](/CLAUDE.md#links).
- Acting as a persona: [Using a persona](/team/README.md#using-a-persona).
- Persona notes: [Persona notes](/team/workspace.md#persona-notes).
- Claiming work: [The board](/team/workspace.md#the-board).
- Daily logs and decision entries: [Daily notes](/team/workspace.md#daily-notes).
- One thread per PR, and the $10 hand-off check:
  [One thread per PR](/team/workspace.md#one-thread-per-pr).
- Process ideas: [Process ideas](/team/workspace.md#process-ideas).
- Team skills: [Team skills](/team/workspace.md#team-skills).
- The PR template: [PR template](/team/workspace.md#pr-template).
- Reporting cost: [CFO persona](/team/Management/personas/cfo.md#role).
- Security is everyone's job:
  [Security is everyone's job](/team/README.md#security-is-everyones-job).
- Potential data breach:
  [Potential data breach](/team/QA/personas/cybersecurity-engineer.md#potential-data-breach).
- What each persona decides: the *Decisions* section of its persona file,
  summarized in [Who decides what](/team/review-protocol.md#who-decides-what).
- Decision requests:
  [Decisions are separate from merging](/team/review-protocol.md#decisions-are-separate-from-merging).
- Who reviews a PR: [Who reviews what](/team/review-protocol.md#who-reviews-what).
- Wording-only changes to another persona's file:
  [Wording-only changes notify the persona](/team/review-protocol.md#wording-only-changes-notify-the-persona).
- Running a review or cross-review:
  [How a review runs](/team/review-protocol.md#how-a-review-runs).
- Each persona edits only its own files:
  [Who fixes a finding](/team/review-protocol.md#who-fixes-a-finding).
- Work outside the phase or the PR:
  [Follow-up work](/team/review-protocol.md#follow-up-work).
- Changing a process rule, and where each rule lives:
  [Ripple check](/team/review-protocol.md#ripple-check-for-process-rules).
- Screenshots in UI PRs:
  [Screenshots in UI PRs](/team/Development/personas/ui-ux-designer.md#screenshots-in-ui-prs).

## Branches

- `develop` is the default branch and the integration branch. Every PR
  targets `develop`.
- Open a PR for every change to `develop`, so the Team Lead can see the
  diff. Assign the Team Lead, but don't request their review. The owner
  merges it, as [Two levels of review](/team/review-protocol.md#two-levels-of-review)
  says.
- `main` is what's live. The only PR into `main` is the `develop` → `main`
  release PR. Any persona may open it, assigning the Team Lead
  and summarizing everything merged since `main`. The Team Lead is its
  only reviewer: never approve or merge it. Only the Team Lead merges
  into `main`.
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
