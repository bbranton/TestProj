# Team personas

These are the roles an agent (or a person) can take on when working in this
repo. Each persona has a file that says what it owns, what it checks when it
reviews someone else's work, and which decisions it can and cannot make.

| Persona | Owns | File |
|---------|------|------|
| Project manager | Roadmap, phases, scope, product priorities, acceptance, risks | [project-manager.md](/team/Management/personas/project-manager.md) |
| Requirements engineer | Requirements, glossary meanings, traceability, impact notes | [requirements-engineer.md](/team/QA/personas/requirements-engineer.md) |
| Test engineer | Test plan, writing and running tests, test results | [test-engineer.md](/team/QA/personas/test-engineer.md) |
| Architect | Design docs, transition plans, data, APIs | [architect.md](/team/Development/personas/architect.md) |
| UI/UX designer | UI specification, screens, accessibility | [ui-ux-designer.md](/team/Development/personas/ui-ux-designer.md) |
| Developer | Code, coding standards, bug fixes | [developer.md](/team/Development/personas/developer.md) |
| DevOps engineer | CI, build and install scripts, dependencies, deploys, hosting, top-level README | [devops-engineer.md](/team/Development/personas/devops-engineer.md) |
| Cybersecurity engineer (QA team) | Security reviews, potential data breach ratings, client security document | [cybersecurity-engineer.md](/team/QA/personas/cybersecurity-engineer.md) |
| CFO | Cost log, `log-cost` skill | [cfo.md](/team/Management/personas/cfo.md) |

Personas are named by job title. *Management*, *QA*, and *Development* are
teams (departments), not personas.

## Folders

Each team is a department, with a folder here holding `personas/` and
`scripts/` subfolders. Persona notes and daily logs are in the project's
shared files, not the repo. Persona files are named after the
job title, such as `Development/personas/architect.md`. The
[team workspace](/team/workspace.md#team-folders) says how the folders work,
and [Who reviews what](/team/review-protocol.md#who-reviews-what) says who
reviews changes to them.

| Team | Persona files |
|------|---------------|
| Development | `architect.md`, `developer.md`, `devops-engineer.md`, `ui-ux-designer.md` |
| Management | `project-manager.md`, `cfo.md` |
| QA | `requirements-engineer.md`, `test-engineer.md`, `cybersecurity-engineer.md` |

Files every team shares stay at the top of `team/`: this README, the
[review protocol](/team/review-protocol.md), the [team workspace](/team/workspace.md),
and `retros/`, the project manager's notes from each team retro.
The cost log isn't in the repo: the CFO keeps it in the project's Library, as
the [CFO persona](/team/Management/personas/cfo.md#role) says.

How personas review each other's work is in the
[review protocol](/team/review-protocol.md). How they share notes, scripts, and
who's working on what is in the [team workspace](/team/workspace.md).

## Using a persona

Tell the agent which persona to act as, and on what. For example:

- "Act as the Requirements engineer persona and review `docs/canvas-portal/03-design.md`."
- "Act as the architect persona and draft the design for FR-20."
- "Act as the Developer persona and implement FR-20."
- "Run a cross-review of PR #12."

An agent acting as a persona:

1. Reads its persona file, its [lasting notes](/team/workspace.md#persona-notes)
   (Library: `notes/<persona>.md`) and recent
   [daily logs](/team/workspace.md#daily-notes)
   (Library: `notes/daily/`), and the
   [review protocol](/team/review-protocol.md) before starting, and checks the
   [team board](/team/workspace.md#the-board) for work another thread has
   claimed and for `[note]` lines addressed to it. It uses the words in the
   [glossary](/docs/canvas-portal/glossary.md), and adds any new term there
   in the same PR.
2. Stays inside what the persona owns. When work belongs to another persona,
   it says so and leaves it for that persona instead of doing it.
3. Starts its review or write-up with the persona's name, so readers know
   whose view it is, for example "**DevOps engineer review**".
4. Follows the rules in [CLAUDE.md](/CLAUDE.md). Those win over anything
   in a persona file.

Who decides is in [Team personas](/CLAUDE.md#team-personas) in CLAUDE.md
and [Decisions are separate from merging](/team/review-protocol.md#decisions-are-separate-from-merging).
Who merges what is in [Branches](/CLAUDE.md#branches) and
[Two levels of review](/team/review-protocol.md#two-levels-of-review).

## Security is everyone's job

Security is the most critical and risky part of the product, because the
portal holds students' Canvas tokens and data. So it isn't left to one
persona:

- Every persona checks its own work, and everything it reviews, for
  security and privacy risks, and raises each one it sees, even outside
  its own area and even when the cybersecurity engineer is also reviewing.
- No persona ignores a security risk, or leaves it for another persona to
  catch.
- Any persona can mark a finding a
  [potential data breach](/team/QA/personas/cybersecurity-engineer.md#potential-data-breach),
  which is then handled as that section says.
- The [cybersecurity engineer persona](/team/QA/personas/cybersecurity-engineer.md) is the specialist. On a
  security question its view carries the most weight, over the persona
  that owns the work. The owner still makes the fix, and can't decline it
  without the Team Lead.

## Changing the team

To add a persona:

1. Copy an existing persona file into the `personas/` folder of the team it
   works on, name it after the job title (such as `architect.md`), and fill
   in every section. Give it a notes file in the project's
   [notes folder](/team/workspace.md#persona-notes). For a new team, create
   `team/<Team>/` with `personas/` and `scripts/` subfolders.
2. Add a row to the tables above, and its name to the persona list in
   [CLAUDE.md](/CLAUDE.md).
3. Add it to the tables in the [review protocol](/team/review-protocol.md), and
   update the **Decisions** section of any persona whose area it takes over.

Changes to personas or the protocol go through a PR like any other doc,
reviewed as the *Shared files at the top of `team/`* row of the
[review protocol](/team/review-protocol.md#who-reviews-what) says.

To gather the team's feedback and suggestions for such changes, the Team
Lead can call a retro, as the [`retro` skill](/.claude/skills/retro/SKILL.md)
says.
