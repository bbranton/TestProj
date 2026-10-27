# Review protocol

How personas review each other's work. The personas are listed in the
[team README](README.md).

The Team Lead has the final say on every decision and every disagreement,
and can override any rule here, including the reviewers on any PR.
Everything below is the default when the Team Lead hasn't said otherwise.

## The rules in short

1. **Two levels of review.** PRs into `develop` are reviewed by personas
   and merged by their owner. The `develop` → `main` release PR is
   reviewed and merged only by the Team Lead.
2. **The Team Lead decides; PRs carry out decisions.** Every real
   decision goes to the Team Lead as a decision request, answered before
   anyone edits a doc for it.
3. **The owner fixes, the reviewer reports.** A reviewer never edits
   another persona's files.
4. **Read from `develop`.** Open PRs are drafts, never the source of
   truth.
5. **Small, focused PRs.** One job per PR.
6. **The author picks reviewers by what the PR touches.** Reviews are
   quick, and the author pushes fixes right away.
7. **Close out.** Log the decision, report the cost, and end the thread.

## Two levels of review

**Into `develop`.** The owner persona opens the PR, picks its reviewers
(see [Who reviews what](#who-reviews-what)), and assigns the Team Lead
without requesting their review, so the Team Lead sees the diff. Once every
reviewer's latest verdict is **Recommend** or **Recommend with notes**, the
owner thread merges the PR itself and posts the link in its thread. A PR
whose changes touch no other persona's area, such as a team's edit to its
own folder, needs no reviewers and is merged straight away.

**`develop` → `main`.** This is a batched release of what's on `develop`.
The Team Lead opens it, is its only reviewer, and is the only one who
merges it. No persona opens, approves, or merges a PR into `main`.

## Decisions are separate from merging

The Team Lead makes every real decision, explicitly. A PR is never where a
decision is made or approved: it only carries out decisions already made.
That is why a persona can merge into `develop` without the Team Lead.

- **What goes to the Team Lead:** scope and phases, security and risk
  (token handling, accepting a known risk), hosting and domains, anything
  that costs money or changes the deploy, and team structure and process.
- **What an owner decides alone:** details inside its own area that no
  other doc depends on, such as a requirement's wording, a test case, or a
  layout detail within the spec. When in doubt, it's a decision request.
- **A decision request** states the question, the options, a
  recommendation, and the docs it changes. Each persona whose area it
  affects adds its impact: which of its files change, and how. Requests go
  in Management's
  [decision register](../docs/canvas-portal/01-roadmap.md#5-open-decisions)
  or in a GitHub issue labeled `decision`.
- **The Team Lead answers in batches.** Management keeps the register and
  brings it to the Team Lead. Only after an answer do the owners make their
  edits, each in its own PR, citing the decision.
- **A PR that needs a new decision stops.** The owner raises a decision
  request and waits for the answer before going on. A finding that needs
  one is marked **Waiting on the Team Lead**.

### Keeping the Team Lead informed

The coordinator tells the Team Lead in real time, in the project chat,
when a PR merges into `develop` and when a decision request is raised,
with links. The `develop` → `main` release PR is the Team Lead's final
check of everything merged.

## Small, focused PRs

- A PR does one job. A small PR is quick to review and quick to fix.
- When a new change is related to a persona's open PR, it goes on that
  PR. When it isn't, it gets a new PR. Prefer several small PRs over one
  sprawling one.
- Merge `develop` into the branch before asking for review, so reviewers
  see the PR against the current base.

## Read from `develop`

Reviews and impact lists read the docs on `develop` and cite the commit,
such as `develop@3245fa4`. Another persona's open PR is a draft: read it to
avoid clashes, never as the source of truth.

## Who reviews what

The author picks the reviewers. The rule: **each persona whose area the PR
touches reviews it**, except the author. The author lists the reviewers in
the PR description, with one line each on why. Any reviewer can ask for
another persona in a finding, and the Team Lead can add or drop reviewers
at any time.

| If the PR touches | Reviewer | Owner of the area |
|-------------------|----------|-------------------|
| Phases, scope, priorities, risks, or the roadmap (`01-roadmap.md`) | Management | Management |
| Requirement wording, IDs, or the glossary (`02-requirements.md`, `glossary.md`) | Requirements engineer | Requirements engineer |
| What needs testing, the test plan (`05-test-plan.md`), or test code | Test engineer | Test engineer |
| Structure, data, APIs, new dependencies, or the design (`03-design.md`) | Architecture | Architecture |
| Any page, screen, style, on-screen wording, accessibility, or the UI specification (`04-ui-specification.md`) | UI/UX | UI/UX |
| App code | Developer | Developer |
| CI, build, install scripts, repo settings, or the top-level `README.md` | DevOps | DevOps |
| Canvas tokens, sign-in, the session cookie, secrets, student data, hosting, or deploys; the client security document (`06-security-overview.md`) | Security, always | Security |
| Shared files at the top of `team/`, or another team's folder | Each persona whose file changes, plus Management | Management |
| A team's own folder (`team/<Team>/`), or a skill whose script is in it | None | That team (the `log-cost` skill: CFO) |
| The cost log (`team/Management/cost-log.md`) | None | CFO, the only persona that edits it |

A code PR always has the Test engineer as a reviewer, since every change
needs a test. A PR that changes a phase or a priority always has
Management.

Each reviewer looks through its own lens, using the review checklist in its
persona file, and checks that the words match the
[glossary](../docs/canvas-portal/glossary.md). Security is still everyone's
job: any reviewer raises any token or student-data risk it sees, as
[Security is everyone's job](README.md#security-is-everyones-job) says.

## Who decides what

The Team Lead is the primary decision maker. Each persona decides only
details inside its own area that no other doc depends on; everything in the
last column goes to the Team Lead as a
[decision request](#decisions-are-separate-from-merging). A review gives a
persona a voice, not a decision: a reviewer decides only whether the PR is
acceptable for its area.

| Decision | Decided by | Decision request to the Team Lead for |
|----------|------------|-------------------------|
| Business goals, scope and phases, hosting and domains, cost, team structure and process | Team Lead | Always |
| Feature priorities within a phase, the order of work, triage, keeping the decision register, rating risks. A potential data breach is always critical and must-fix | Management | Every scope, roadmap, or phase change; adding or dropping a goal; accepting a risk instead of reducing it |
| How a requirement is worded and traced | Requirements engineer | Adding, removing, or moving a requirement between phases |
| How it's tested, and whether tests pass | Test engineer | Calling a phase done; removing or weakening a test |
| Design: structure, data, APIs, technology, security design | Architecture | A new dependency, service, or data store; how the Canvas token is stored or sent; starting a transition plan |
| Writing code, coding standards, bug fixes | Developer | Design changes go to Architecture first |
| Screens, layout, wording, accessibility | UI/UX | A new screen or a change to the main flow |
| CI, tooling, build and install scripts, branch mechanics, dependency integration | DevOps | Changes to the live app or hosting; a paid service; a new secret store; new access |
| Whether a weakness is a vulnerability, its severity, and whether it is a potential data breach; the client security document | Security | Accepting a vulnerability instead of fixing it; publishing the client security document; telling anyone outside the team about a suspected leak |
| What goes in the cost log | CFO | Changing the log's columns or how threads report cost |
| Merging a PR into `develop` | The PR's owner, once its reviewers recommend it | Never: the PR only carries out decisions already made |
| Approving and merging the `develop` → `main` release PR | Team Lead | Always |

Each persona file has a **Decisions** section listing what it decides,
what it defers and to whom, and what needs the Team Lead.

## How a review runs

1. **Owner prepares.** The owner merges `develop` into its branch, opens
   the PR, and fills in the PR template: requirement IDs, reviewers, and
   why.
2. **Reviewers review.** Each reviewer reads the change against its
   checklist and posts one review headed with its persona and verdict,
   such as "**DevOps review: Changes needed**".
3. **Owner fixes.** The owner pushes a fix for each finding right away, or
   replies with why not.
4. **Verdict.** Each reviewer ends with **Recommend**, **Recommend with
   notes** (minor findings the owner may fix later), or **Changes needed**.
   After fixes, the reviewer checks only the fixes and updates its verdict.
5. **Merge.** When every latest verdict is Recommend or Recommend with
   notes, the owner merges into `develop`.

### The owner fixes, the reviewer reports

A reviewer never edits another persona's files. Each finding goes one of
three ways:

- **About this PR:** a finding on the PR. The owner fixes it before merge.
- **About the reviewer's own doc:** the reviewer fixes it in its own PR.
- **About another persona's area, outside this PR:** the reviewer opens a
  GitHub issue, as [Follow-up work](#follow-up-work) says.

## Findings table

| # | Found by | Fix in | Finding | Status |
|---|----------|--------|---------|--------|
| F-1 | Requirements engineer | Requirements | FR-12 says "fast"; give a number so it can be tested. | Open |

- **#** is unique within the review (`F-1`, `F-2`, ...). Findings whose fix
  is in another doc use `X-` IDs.
- **Status** is one of Open, Fixed in #PR, Moved to #issue, Won't fix
  (with the reason), or Waiting on the Team Lead.
- A finding that could expose a token, a session, or a student's data
  starts with **Potential data breach:**, whichever persona finds it, as
  the [Security persona](QA/personas/cybersecurity-engineer.md#potential-data-breach)
  says. It is never Won't fix without the Team Lead.

## Follow-up work

Work a review uncovers outside the PR becomes a GitHub issue, not a
comment that gets lost:

1. **The reviewer opens it.** The issue says what is needed and why, links
   the PR, and gets the owning department's label, such as `team: QA`,
   plus `needs-triage`. A
   potential data breach also gets `potential-breach`.
2. **The review names it.** The finding's status is "Moved to #issue".
   Follow-ups don't block the PR or change the verdict.
3. **The owner lists it** in the PR's *Follow-ups opened* section before
   merging.
4. **Management triages it,** naming the persona that owns it and
   recommending a phase, the backlog, or closing, in a comment on the issue, then removes `needs-triage`. A
   `potential-breach` issue is always critical, first in the current
   phase, and fixed before the next deploy.
5. **The Team Lead sets its priority.** Nobody starts on an issue before
   then.

## Disagreements

When an owner and a reviewer disagree, each states its case in one or two
sentences in the findings table, and the finding is marked **Waiting on the
Team Lead**. Personas don't overrule each other. Inside its own area the
owner's view counts most, except on security, where Security's counts
most. After two rounds on the same point without agreement, the owner
marks the finding **Waiting on the Team Lead**.

## Running reviews with agents

### One thread per reviewer

- Each reviewer runs in **its own fresh thread**. It reads only its
  persona file, its own notes and recent daily logs, this protocol, the
  PR, and the docs on `develop` that the PR changes or names. It doesn't
  see the owner's thread or other reviews before writing its own.
- Only the coordinator starts threads. The owner sends the coordinator the
  PR and its reviewers, and the coordinator starts one thread per
  reviewer.
- The owner thread is subscribed to the PR and wakes on every comment. It
  never reviews its own PR as another persona.
- All comments post from the Team Lead's GitHub account, so the review
  heading is how readers tell personas apart.
- A reviewer thread stays open until the PR merges or closes. The owner
  tells it when that happens.

One thread playing several personas is only for quick, informal checks the
Team Lead asks for. It never counts as a review.

### Posting reviews one at a time

GitHub keeps one draft review per account on a PR, and every reviewer
posts from the Team Lead's account, so two reviewers posting at once get
their findings mixed into one review (as on PR #4). Write the whole review
first, then:

1. Check the [team board](workspace.md#the-board) for a `[posting]` line on
   the same PR, and wait for it to go. A line older than an hour is stale.
2. Add your own, such as
   `- [posting] DevOps · review of PR #12 · 2026-10-25 21:30`, create the
   draft review, add the comments, and submit.
3. Delete your line as soon as the review is submitted.

### Questions between threads

A PR's GitHub events reach only the owner thread. When the owner needs an
answer from a reviewer, it replies on the reviewer's comment, then messages
the reviewer thread with the link. The reviewer answers on the same
comment and tells the owner thread. Any decision reached between threads
is written on the PR before anyone acts on it.

## Close out

- **Before merging,** the owner adds a `### Decision:` entry for each
  decision to its persona's daily log in the same PR, in the format in
  [Daily notes](workspace.md#daily-notes), and any lasting lesson to its
  notes.
- **After the PR merges or closes,** the owner releases its claim on the
  [board](workspace.md#the-board), and every thread that worked on the PR
  reports its cost to the CFO with the `log-cost` skill and ends.
