# Team personas

These are the roles an agent (or a person) can take on when working in this
repo. Each persona has a file that says what it owns, what it checks when it
reviews someone else's work, and which decisions it can and cannot make.

| Persona | Owns | File |
|---------|------|------|
| Management | Roadmap, phases, scope, priorities, risks | [project-manager.md](Management/personas/project-manager.md) |
| Product and QA | Requirements, test plan, acceptance | [product-qa-analyst.md](QA/personas/product-qa-analyst.md) |
| Architecture | Design docs, transition plans, data, APIs | [architect.md](Architecture/personas/architect.md) |
| UI/UX | UI specification, screens, accessibility | [ui-ux-designer.md](Ui-Ux/personas/ui-ux-designer.md) |
| Developer | Code, coding standards, bug fixes | [developer.md](Software/personas/developer.md) |
| DevOps | CI, build and install scripts, dependencies, deploys, hosting, top-level README | [devops-engineer.md](DevOps/personas/devops-engineer.md) |
| Security | Security reviews, potential data breach ratings, client security document | [security-engineer.md](Security/personas/security-engineer.md) |
| CFO | Cost log: the only persona that edits it | [cfo.md](Finance/personas/cfo.md) |

## Folders

Each team is a department, with a folder here holding `notes/`,
`personas/`, and `scripts/` subfolders. Persona files are named after the
job title, such as `Architecture/personas/architect.md`. The
[team workspace](workspace.md#team-folders) says how the folders work.
Each team may freely update its own folder.

| Team | Persona files |
|------|---------------|
| Architecture | `architect.md` |
| DevOps | `devops-engineer.md` |
| Finance | `cfo.md` |
| Management | `project-manager.md` |
| QA | `product-qa-analyst.md` |
| Security | `security-engineer.md` |
| Software | `developer.md` |
| Test | None yet |
| Ui-Ux | `ui-ux-designer.md` |

Files every team shares stay at the top of `team/`: this README, the
[review protocol](review-protocol.md), and the [team workspace](workspace.md).
The [cost log](Finance/cost-log.md) is in the Finance folder, since only the
CFO edits it.

How personas review each other's work is in the
[review protocol](review-protocol.md). How they share notes, scripts, and
who's working on what is in the [team workspace](workspace.md).

## Using a persona

Tell the agent which persona to act as, and on what. For example:

- "Act as the Product and QA persona and review `docs/canvas-portal/03-design.md`."
- "Act as the Architecture persona and draft the design for FR-20."
- "Act as the Developer persona and implement FR-20."
- "Run a cross-review of PR #12."

An agent acting as a persona:

1. Reads its persona file, its team's `notes/` folder, and the
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
between personas, and confirms which personas review each PR. A persona recommends, and the
Team Lead decides. A thread may merge its own PR into `develop` once its
confirmed reviewers recommend it, but never approves or merges anything into
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
  [potential data breach](Security/personas/security-engineer.md#potential-data-breach).
  Management treats every one as critical and must-fix.
- The [Security persona](Security/personas/security-engineer.md) is the specialist. On a
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
3. Add it to both tables in the [review protocol](review-protocol.md), and
   update the **Decisions** section of any persona whose area it takes over.

Changes to personas or the protocol go through a PR like any other doc,
reviewed as the *Team process* row of the review protocol says.
