# Team personas

These are the roles an agent (or a person) can take on when working in this
repo. Each persona has a file that says what it owns, what it checks when it
reviews someone else's work, and which decisions it can and cannot make.

| Persona | Owns | File |
|---------|------|------|
| Management (project manager) | Roadmap, phases, scope, product priorities, acceptance, risks | [project-manager.md](Management/personas/project-manager.md) |
| Requirements engineer | Requirements, glossary meanings, traceability, impact notes | [requirements-engineer.md](QA/personas/requirements-engineer.md) |
| Test engineer | Test plan, writing and running tests, test results | [test-engineer.md](QA/personas/test-engineer.md) |
| Architecture | Design docs, transition plans, data, APIs | [architect.md](Development/personas/architect.md) |
| UI/UX | UI specification, screens, accessibility | [ui-ux-designer.md](Development/personas/ui-ux-designer.md) |
| Developer | Code, coding standards, bug fixes | [developer.md](Development/personas/developer.md) |
| DevOps | CI, build and install scripts, dependencies, deploys, hosting, top-level README | [devops-engineer.md](Development/personas/devops-engineer.md) |
| Security (cybersecurity engineer, QA team) | Security reviews, potential data breach ratings, client security document | [cybersecurity-engineer.md](QA/personas/cybersecurity-engineer.md) |
| CFO | Cost log: adds reported rows in batches | [cfo.md](Management/personas/cfo.md) |

*Management* is a department. When a doc names Management as a persona,
it means the project manager. *Security* is another name for the
cybersecurity engineer, who works in the QA department.

## Folders

Each team is a department, with a folder here holding `notes/`,
`personas/`, and `scripts/` subfolders. Persona files are named after the
job title, such as `Development/personas/architect.md`. The
[team workspace](workspace.md#team-folders) says how the folders work.
Each persona may freely update its own files there; another persona's
files get that persona's review.

| Team | Persona files |
|------|---------------|
| Development | `architect.md`, `developer.md`, `devops-engineer.md`, `ui-ux-designer.md` |
| Management | `project-manager.md`, `cfo.md` |
| QA | `requirements-engineer.md`, `test-engineer.md`, `cybersecurity-engineer.md` |

Files every team shares stay at the top of `team/`: this README, the
[review protocol](review-protocol.md), and the [team workspace](workspace.md).
The [cost log](Management/cost-log.md) is in the Management folder, since the
CFO keeps it. Threads report their rows and the CFO adds them in batches, so
the log doesn't cause merge conflicts.

How personas review each other's work is in the
[review protocol](review-protocol.md). How they share notes, scripts, and
who's working on what is in the [team workspace](workspace.md).

## Using a persona

Tell the agent which persona to act as, and on what. For example:

- "Act as the Requirements engineer persona and review `docs/canvas-portal/03-design.md`."
- "Act as the Architecture persona and draft the design for FR-20."
- "Act as the Developer persona and implement FR-20."
- "Run a cross-review of PR #12."

An agent acting as a persona:

1. Reads its persona file, its lasting notes and recent
   [daily logs](workspace.md#daily-notes) in its team's `notes/` folder, and the
   [review protocol](review-protocol.md) before starting, and checks the
   [team board](workspace.md#the-board) for work another thread has
   claimed. It uses the words in the
   [glossary](../docs/canvas-portal/glossary.md), and adds any new term there
   in the same PR.
2. Stays inside what the persona owns. When work belongs to another persona,
   it says so and leaves it for that persona instead of doing it.
3. Starts its review or write-up with the persona's name, so readers know
   whose view it is, for example "**DevOps review**".
4. Follows the rules in [CLAUDE.md](../CLAUDE.md). Those win over anything
   in a persona file.

The Team Lead has the final say on every decision and every disagreement
between personas, and can change the reviewers a PR's author picked. A
persona recommends, and the Team Lead decides. A thread may merge its own
PR into `develop` once its reviewers recommend it, but never approves or merges anything into
`main`; see [Branches](../CLAUDE.md#branches).

## Security is everyone's job

Security is the most critical and risky part of the product, because the
portal holds students' Canvas tokens and data. So it isn't left to one
persona:

- Every persona checks its own work, and everything it reviews, for
  security and privacy risks, and raises each one it sees, even outside
  its own area and even when Security is also reviewing.
- No persona ignores a security risk, or leaves it for another persona to
  catch.
- Any persona can mark a finding a
  [potential data breach](QA/personas/cybersecurity-engineer.md#potential-data-breach).
  Management treats every one as critical and must-fix.
- The [Security persona](QA/personas/cybersecurity-engineer.md) is the specialist. On a
  security question its view carries the most weight, over the persona
  that owns the work. The owner still makes the fix, and can't decline it
  without the Team Lead.

## Changing the team

To add a persona:

1. Copy an existing persona file into the `personas/` folder of the team it
   works on, name it after the job title (such as `architect.md`), and fill
   in every section. Give it a notes file in that team's
   `notes/` folder. For a new team, create `team/<Team>/` with `notes/`,
   `personas/`, and `scripts/` subfolders.
2. Add a row to the tables above, and its name to the persona list in
   [CLAUDE.md](../CLAUDE.md).
3. Add it to the tables in the [review protocol](review-protocol.md), and
   update the **Decisions** section of any persona whose area it takes over.

Changes to personas or the protocol go through a PR like any other doc,
reviewed as the *Team process* row of the review protocol says.
