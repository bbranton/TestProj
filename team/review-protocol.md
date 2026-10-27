# Review protocol

How personas review each other's work. The personas are listed in the
[team README](README.md).

## The Team Lead has the final say

The Team Lead has the final say on every decision and every disagreement
between personas. The Team Lead can override any persona, any rule or table
in this protocol, and the reviewers for any PR. Everything below describes
the default when the Team Lead hasn't said otherwise.

## Who reviews what

Every piece of work has one **owner** persona, who writes it and answers its
findings. The table below gives the **recommended reviewers** for each kind
of work. An optional reviewer is recommended when the change touches its
area. The owner lists the recommended and optional reviewers in the PR
description, with a reason for each optional one.

Reviews cost real time and tokens, so **the Team Lead confirms the reviewers
for each PR** before any review starts. The Team Lead can add or drop any
reviewer, including all of them when the change is small and the Team
Lead's own review gives enough coverage. The reviewers the Team Lead keeps
are the PR's **confirmed reviewers**.

Picking optional reviewers follows Management's rule: given the topic or
the changes, does another persona need to join? Any reviewer can also ask
for another persona in a finding.

| Work | Owner | Recommended reviewers | Optional reviewers |
|------|-------|--------------------|--------------------|
| Roadmap (`01-roadmap.md`) | Management | Requirements engineer, Architecture | Test engineer, DevOps |
| Requirements (`02-requirements.md`) | Requirements engineer | Test engineer, Architecture, plus Management when a priority or phase changes | UI/UX, Developer |
| Design (`03-design.md`) | Architecture | Requirements engineer, Developer | Test engineer, UI/UX, DevOps |
| Transition plan (major design change) | Architecture | Developer, Requirements engineer | Test engineer, DevOps, Management |
| UI specification (`04-ui-specification.md`) | UI/UX | Requirements engineer, Architecture | Test engineer; Management, when features must be hidden or disabled to fit the release schedule |
| Test plan (`05-test-plan.md`) | Test engineer | Requirements engineer, Architecture | Developer, UI/UX, DevOps |
| Glossary (`glossary.md`) | Requirements engineer | UI/UX | Management, for team process terms; Architecture, for web terms |
| Code PR (backend) | Developer | Architecture, Test engineer | DevOps |
| Code PR (frontend or any UI change) | Developer | Architecture, UI/UX, Test engineer | DevOps |
| Top-level `README.md` | DevOps | Developer | Test engineer |
| CI, build, install, dependency, deploy, or hosting change | DevOps | Developer | Architecture, Test engineer |
| Phase exit (moving to the next phase) | Management | Test engineer, Requirements engineer | Architecture, Developer, UI/UX, DevOps |
| Client security document (`06-security-overview.md`) | Security | Architecture, DevOps | Requirements engineer, Management |
| Team process (shared files at the top of `team/`, team skills) | Management | Each persona whose file changes | Any other persona |
| A team's own folder (`team/<Team>/`) | That team | None | Any persona the team asks |
| Cost log (`team/Management/cost-log.md`) | CFO | None | Management |

**Security joins any PR that touches tokens, sign-in, or student data.**
Whatever its row, a PR that changes how the Canvas token, the session
cookie, sign-in, secrets, or student data (Canvas data, the board, or
accounts) is stored, sent, shown, logged, tested, or backed up has
Security as a recommended reviewer. The owner says which of these it
touches.

Each reviewer looks through its own lens, using the review checklist in its
persona file. For example, DevOps reads the design asking "how is this
hosted and configured?", not "is this the right feature?", and Security
reads it asking "where could a token or a student's data leak?".

Every reviewer also checks that the words match the
[glossary](../docs/canvas-portal/glossary.md): a term used with a different
meaning, or a new term the glossary doesn't have, is a finding.

The requirements engineer runs its own testability check before handing
requirements on, and the test engineer's review of the requirements is the
outside check that each one can be tested. The requirements engineer's
review of the test plan checks that every requirement is covered.

## Who decides what

Each persona decides only inside its own area. Reviewing someone else's work
gives a persona a voice, not a decision: it can raise findings and recommend,
but the persona that owns the area makes the call. A persona's recommendation
outside its area is advice, never sign-off.

| Decision | Decided by | Needs the Team Lead for |
|----------|------------|-------------------------|
| Business goals | Team Lead | Always |
| Priorities and scope within the approved roadmap, including product priorities and accepting finished features; recommends phases, timelines, and features hidden for a release | Management | Every change to the roadmap or its phases; adding or dropping a goal |
| The risk list: rating each risk and assigning its owner. A potential data breach is always critical and must-fix | Management | Accepting a risk instead of reducing it; a mitigation that changes scope or timeline |
| How a requirement is worded and traced | Requirements engineer | Adding, removing, or moving a requirement between phases |
| How it's tested, and whether tests pass | Test engineer | Calling a phase done; removing or weakening a test |
| Design: structure, data, APIs, technology, security design | Architecture | A new dependency, service, or data store; how the Canvas token is stored or sent; starting a transition plan |
| Writing code, coding standards, bug fixes | Developer | Approving and merging every PR; design changes go to Architecture |
| Screens, layout, wording, accessibility | UI/UX | A new screen or a change to the main flow |
| CI, build and install scripts, dependency integration, deploys, hosting, secrets | DevOps | Changes to the live app or hosting; a paid service; a new secret store; new access |
| Whether a weakness is a vulnerability, its severity, and whether it is a potential data breach (any persona can raise one, and Security's view counts most); the wording of the client security document | Security | Accepting a vulnerability instead of fixing it; publishing or changing the client security document; telling anyone outside the team about a suspected leak |
| What goes in the cost log, and when rows are committed | CFO | Changing the log's columns or how threads report cost |
| Approving and merging a PR | Team Lead | Always |

Only the persona in **Decided by** makes that decision. Every other persona
can raise findings about it, and nothing more.

Each persona file has a **Decisions** section that lists what it decides,
what it defers and to whom, and what needs the Team Lead. When a decision
falls in another persona's area, the persona names that persona and leaves
the decision to them.

## How a review runs

1. **Owner prepares.** The owner opens the PR and lists in its description
   the requirement IDs it touches and the recommended reviewers, from the
   table above. The Team Lead confirms the reviewers.
2. **Reviewers review.** Each confirmed reviewer reads the change against its
   checklist and posts one review headed with its persona name, such as
   "**DevOps review**". Reviewers can write their reviews in parallel, but
   they post them one at a time, as
   [Posting reviews one at a time](#posting-reviews-one-at-a-time) says.
3. **Findings are logged.** Each finding gets an ID and a row in a findings
   table (format below). A finding that needs a change in a different doc
   names that doc under **Fix in**, and is fixed in that doc's PR, so each PR
   still changes only what it owns. Work the reviewer finds that is outside
   this PR becomes a GitHub issue, as
   [Follow-up work](#follow-up-work) says.
4. **Owner answers.** The owner fixes each finding or replies with why not.
   Findings that need a decision go to the Team Lead.
5. **Sign-off.** Each confirmed reviewer ends with one verdict:
   - **Recommend** — no open findings from this reviewer.
   - **Recommend with notes** — only minor findings, which the owner may
     fix later.
   - **Changes needed** — at least one finding must be fixed before merge.
6. **Re-review.** After the owner pushes fixes for a **Changes needed**
   verdict, that reviewer checks the fixes and updates its verdict.
7. **Team Lead decides.** The PR is ready when every confirmed reviewer's
   latest verdict is **Recommend** or **Recommend with notes**. With no
   confirmed reviewers, the Team Lead's own review is the review. The owner
   thread may then merge the PR into `develop`. Only the Team Lead merges
   into `main`, through the `develop` → `main` release PR.

## Findings table

Use the same shape as the canvas portal docs review:

| # | Found by | Fix in | Finding | Status |
|---|----------|--------|---------|--------|
| F-1 | Requirements engineer | Requirements | FR-12 says "fast"; give a number so it can be tested. | Open |

- **#** is unique within the review (`F-1`, `F-2`, ...). Findings that span
  several docs use `X-` IDs.
- **Status** is one of Open, Fixed in #PR, Moved to #issue, Won't fix
  (with the reason), or Waiting on the Team Lead.
- A finding that could expose a token, a session, or a student's data to
  anyone else starts with **Potential data breach:**, whichever persona
  finds it, as the
  [Security persona](QA/personas/cybersecurity-engineer.md#potential-data-breach) says. It
  is never Won't fix without the Team Lead.

## Follow-up work

A reviewer often spots work that the PR causes or uncovers but shouldn't
do itself, such as a doc that is now out of date or a test the change will
need later. So that this work isn't left only in a review comment:

1. **The reviewer opens an issue.** Before posting its review, the reviewer
   opens a GitHub issue for each piece of follow-up work. The issue says
   what is needed and why, links the PR, and gets two labels: the
   `persona: <name>` label of the persona that owns the work (from the
   [team README](README.md)) and `needs-triage`. A reviewer opens issues for
   any area, not only its own; the label says whose work it is. A
   potential data breach also gets `potential-breach`.
2. **The review names it.** The finding goes in the findings table with
   **Status** "Moved to #issue". Follow-ups don't block the PR, and they
   don't change the reviewer's verdict.
3. **The owner lists it.** The owner adds each issue to the PR's
   *Follow-ups opened* section before the Team Lead merges, so the Team
   Lead sees everything the PR leaves for later.
4. **Management triages.** Management reads each `needs-triage` issue and
   recommends where it goes, in a comment on the issue:
   - **Roadmap:** the phase it belongs to, by the scope rules in the
     [Management persona](Management/personas/project-manager.md). Work in the current
     phase can start once it has a priority. Work that changes the roadmap
     or a phase needs a roadmap PR first, as for any roadmap change.
   - **Backlog:** useful, but not planned for any phase yet. Management adds
     the `backlog` label.
   - **Close:** a duplicate or not needed, with the reason.

   A `potential-breach` issue is never backlog or a later phase: Management
   recommends it as critical, to be fixed first in the current phase and
   before the next deploy.

   Management then removes `needs-triage`.
5. **The Team Lead sets priority.** The Team Lead confirms or changes
   Management's recommendation and sets the issue's priority. Nobody starts
   work on an issue until the Team Lead has.

A finding the PR must fix before merge is a finding on the PR, not an
issue. Only work that would make the PR bigger than its job becomes an
issue.

## Disagreements

When an owner and a reviewer disagree, each states its case in one or two
sentences in the findings table, and the finding is marked **Waiting on the
Team Lead**. Personas do not overrule each other. Inside its own area the
owning persona's view counts most, except on security, where Security's
view counts most, as
[Security is everyone's job](README.md#security-is-everyones-job) says. A
disagreement still goes to the Team Lead. The Team Lead's decision is recorded in the doc's change
log or decision list.

## Running reviews with agents

### One thread per reviewer

Each confirmed reviewer runs in **its own thread, started fresh** for that
review. It reads only its persona file, its notes, this protocol, the PR,
and the docs the PR changes or names. It doesn't see the owner's thread or
the other reviewers' reviews before writing its own. That keeps reviews independent.

- The **owner thread** wrote the PR and is subscribed to it, so it wakes
  on every comment. It never reviews its own PR as another persona.
- Only the coordinator can start threads, and it starts reviewer threads
  only after the Team Lead confirms them. The owner sends the coordinator
  the PR and its recommended reviewers. The coordinator gives the Team Lead
  its recommendation, with the PR's size and risk and a reason for each
  reviewer, and starts only the threads the Team Lead confirms.
- Each reviewer thread posts **one PR review** headed with its persona name
  and verdict, such as "**DevOps review: Recommend with notes**", with its
  findings as inline comments. All comments post from the Team Lead's
  GitHub account, so the heading is how readers tell personas apart.
- Reviewer threads post their reviews **one at a time**, as the next
  section says.
- A reviewer thread stays open until the PR merges or closes, for
  questions and re-review. The owner messages each reviewer thread when
  that happens.

One thread playing several personas is only for quick, informal checks
that the Team Lead asks for. It never counts as a confirmed review.

### Posting reviews one at a time

GitHub keeps only one draft (pending) review per account on a PR, and every
reviewer thread posts from the Team Lead's account. Two reviewers posting at
the same time add their comments to the same draft, and their findings get
mixed into one review, as happened on PR #4. So reviewers write their
reviews in parallel but post them one after another:

1. Write the whole review, with its inline comments, before touching
   GitHub.
2. Check the [team board](workspace.md#the-board) for a `[posting]` line on
   the same PR. If there is one, wait for it to go before posting. A
   `[posting]` line older than an hour is stale and can be removed.
3. Add your own line, such as
   `- [posting] DevOps · review of PR #12 · 2026-10-25 21:30`, then create
   the draft review, add the comments, and submit it.
4. Delete your `[posting]` line as soon as the review is submitted.

### Questions and discussion between threads

A PR's GitHub events reach only the owner thread, so a reviewer doesn't
see replies on its comments by itself. When the owner needs an answer
from a reviewer:

1. **Ask on the PR.** Reply on the reviewer's comment, so the question and
   answer stay on the record.
2. **Ring the reviewer.** Message the reviewer thread directly, with a link
   to the comment. Threads may message each other when one's work depends
   on the other's, which a pending review answer does. Use the coordinator
   only when the owner doesn't know the reviewer thread, the reviewer
   thread is resolved, or a new persona is needed.
3. **Answer on the PR.** The reviewer replies on the same comment, then
   messages the owner thread that it answered.
4. **Cap the rounds.** After two rounds on the same point without
   agreement, the owner marks the finding **Waiting on the Team Lead**, as
   in [Disagreements](#disagreements).

Messages between threads aren't visible to the Team Lead, so any decision
reached there is written on the PR before anyone acts on it.

### Running a cross-review

When asked to "run a cross-review" of a PR or doc, the owner thread:

1. Finds the recommended reviewers in the table above, adds optional ones
   by Management's rule, and lists them in the PR description with a reason
   for each.
2. Sends the coordinator the PR and its recommended reviewers. The
   coordinator recommends reviewers to the Team Lead and starts one fresh
   thread per reviewer the Team Lead confirms. If the Team Lead confirms
   none, no reviewer threads start and the Team Lead reviews the PR
   directly.
3. Waits for the reviews to arrive as PR comments, then answers or fixes
   each finding, following the steps above for any question.
4. After pushing fixes for a **Changes needed** verdict, messages that
   reviewer thread to re-review the fixes and update its verdict.
5. Collects all findings into a single findings table on the PR, without
   duplicates, with anything that needs the Team Lead at the top.

Reviews are written before any fixes, so they stay independent of them.
