# Review protocol

How personas review each other's work. The personas are listed in the
[team README](/team/README.md).

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
3. **Each persona fixes its own files.** A finding is fixed in the PR it
   was found in, by the persona that owns the file, which may be the
   owner or a reviewer. No persona edits another persona's files.
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
owner thread merges the PR itself and posts the link in its thread.
Every PR has at least one reviewer: a fresh thread of the owner's own
persona reviews it as a peer, as a precaution, even when the PR touches
only the owner's area. When the owner isn't a persona, the peer is the
persona that owns most of the changed files. A persona's area is its own
files in its team folder (its persona file, notes, and daily log) and the
docs it owns in [Who reviews what](#who-reviews-what). Teams hold several personas, so a
change to another persona's files in the same team folder is reviewed by
that persona, and a team script or skill by the other personas who use it.
The "always" rules below still apply: a code PR always has the Test
engineer, and anything touching the cybersecurity engineer's area always has the cybersecurity engineer.

**`develop` → `main`.** This is a batched release of what's on `develop`.
Any persona may open it: it assigns the Team Lead and
summarizes everything merged since `main`, grouped by area, with links to
the merged PRs and to the screenshots of any UI change. The Team Lead is
its only reviewer and the only one who merges it. No persona approves or
merges a PR into `main`.

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
  in the project manager's
  [decision register](/docs/canvas-portal/01-roadmap.md#5-open-decisions)
  or in a GitHub issue labeled `decision`.
- **The Team Lead answers in batches.** The project manager keeps the register and
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

The author picks the reviewers. The rule: **a peer reviewer from the
author's own persona, plus each other persona whose area the PR
touches.** The peer runs in a fresh thread, like every reviewer. When the
author isn't a persona, the peer is the persona that owns most of the
changed files. The author lists the reviewers in the PR description, with
one line each on why. Any reviewer can ask for
another persona in a finding, and the Team Lead can add or drop reviewers
at any time.

| If the PR touches | Reviewer | Owner of the area |
|-------------------|----------|-------------------|
| Phases, scope, priorities, risks, or the roadmap (`01-roadmap.md`) | Project manager | Project manager |
| Requirement wording, IDs, or the glossary (`02-requirements.md`, `glossary.md`) | Requirements engineer | Requirements engineer |
| What needs testing, the test plan (`05-test-plan.md`), or test code | Test engineer | Test engineer |
| Structure, data, APIs, new dependencies, or the design (`03-design.md`) | Architect | Architect |
| Any page, screen, style, on-screen wording, accessibility, or the UI specification (`04-ui-specification.md`) | UI/UX designer | UI/UX designer |
| App code | Developer | Developer |
| CI, build, install scripts, repo settings, or the top-level `README.md` | DevOps engineer | DevOps engineer |
| Canvas tokens, sign-in, the session cookie, secrets, student data, hosting, or deploys; the client security document (`06-security-overview.md`) | Cybersecurity engineer, always | Cybersecurity engineer |
| Shared files at the top of `team/`, or another team's folder | Each persona whose file changes, plus the project manager | Project manager |
| Another persona's files in your own team's folder | That persona | That persona |
| A team script or its skill (see [Team skills](/team/workspace.md#team-skills)) | The other personas who use it | The team whose `scripts/` folder holds it |
| Only your own persona's area: its persona file, notes, and daily log, or a doc it owns in this table | The peer reviewer only | That persona |
| The cost log (`team/Management/cost-log.md`) | The peer reviewer (CFO) only | CFO, who adds reported rows in batches |

A code PR always has the Test engineer as a reviewer, since every change
needs a test. A PR that changes a phase or a priority always has
the project manager.

Each reviewer looks through its own lens, using the review checklist in its
persona file, and checks that the words match the
[glossary](/docs/canvas-portal/glossary.md). Security is still everyone's
job: any reviewer raises any token or student-data risk it sees, as
[Security is everyone's job](/team/README.md#security-is-everyones-job) says.

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
| Feature priorities within a phase, the order of work, the roadmap backlog, keeping the decision register, rating risks. A potential data breach is always critical and must-fix | Project manager | Every scope, roadmap, or phase change; adding or dropping a goal; accepting a risk instead of reducing it |
| How a requirement is worded and traced | Requirements engineer | Adding, removing, or moving a requirement between phases |
| How it's tested, and whether tests pass | Test engineer | Calling a phase done; removing or weakening a test |
| Design: structure, data, APIs, technology, security design | Architect | A new dependency, service, or data store; how the Canvas token is stored or sent; starting a transition plan |
| Writing code, coding standards, bug fixes | Developer | Design changes go to the architect first |
| Screens, layout, wording, accessibility | UI/UX designer | A new screen or a change to the main flow |
| CI, tooling, build and install scripts, branch mechanics, dependency integration | DevOps engineer | Changes to the live app or hosting; a paid service; a new secret store; new access |
| Whether a weakness is a vulnerability, its severity, and whether it is a potential data breach; the client security document | Cybersecurity engineer | Accepting a vulnerability instead of fixing it; publishing the client security document; telling anyone outside the team about a suspected leak |
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
   such as "**DevOps engineer review: Changes needed**".
3. **Findings get fixed.** The persona that owns each file pushes the fix
   to the PR right away, as [Who fixes a finding](#who-fixes-a-finding)
   says, or replies with why not.
4. **Verdict.** Each reviewer ends with **Recommend**, **Recommend with
   notes** (minor findings that may be fixed later), or **Changes needed**.
   After fixes, the reviewer checks only the fixes and updates its verdict.
5. **Merge.** When every latest verdict is Recommend or Recommend with
   notes, the owner merges into `develop`.

### Who fixes a finding

Each persona edits only its own files, even on another persona's PR. A
finding is fixed in the PR it was found in whenever the fix is in the
current phase, by whichever persona owns the file:

- **In the owner's files:** the owner fixes it before merge.
- **In another persona's files, such as a requirement change found while
  reviewing the UI specification:** that persona commits the fix to the
  same PR, as [Fixes by another persona](#fixes-by-another-persona) says.
  That persona joins the PR's reviewers if it wasn't one.
- **Outside the current phase, or too big for this PR:** it goes on the
  backlog, as [Follow-up work](#follow-up-work) says.

A fix that needs a new decision, such as moving a requirement between
phases, goes to the Team Lead as a decision request first, and the finding
is marked **Waiting on the Team Lead**.

### Fixes by another persona

When a finding needs a change in another persona's files:

1. The owner messages that persona's thread (through the coordinator if
   none is open) with the finding and the PR link.
2. That persona's thread fetches the PR's branch, pulls the latest, and
   commits its change to its own files only. It never force-pushes or
   rewrites the branch's history.
3. It pushes, replies on the finding with the commit, and tells the owner.
   The owner pulls before its next push.
4. The finding's status is "Fixed in `<sha>` by `<persona>`", and the
   reviewer who raised it checks the fix like any other.

## Findings table

| # | Found by | Fix in | Finding | Status |
|---|----------|--------|---------|--------|
| F-1 | Requirements engineer | Requirements | FR-12 says "fast"; give a number so it can be tested. | Open |

- **#** is unique within the review (`F-1`, `F-2`, ...). Findings whose fix
  is in another doc use `X-` IDs.
- **Status** is one of Open, Fixed in `<sha>` (with the persona when it
  isn't the owner), Backlog, Won't fix (with the reason), or Waiting on
  the Team Lead.
- A finding that could expose a token, a session, or a student's data
  starts with **Potential data breach:**, whichever persona finds it, as
  the [cybersecurity engineer persona](/team/QA/personas/cybersecurity-engineer.md#potential-data-breach)
  says. It is never Won't fix without the Team Lead.

## Follow-up work

Review follow-ups never become GitHub issues, so nothing is left open
somewhere nobody looks. Work a review uncovers goes one of two places:

1. **This PR, when it's in the current phase.** The persona that owns the
   file fixes it here, as [Who fixes a finding](#who-fixes-a-finding) says.
2. **The backlog, when it's outside the current phase or too big for this
   PR.** The finding's status is "Backlog", and the owner lists it in the
   PR's *Backlog items* section before merging. The project manager adds each item
   to the [backlog](/docs/canvas-portal/01-roadmap.md#9-backlog) in the
   roadmap, in its next roadmap PR, with a `B-` ID, the PR it came from,
   and the persona that owns it. Backlog items don't block the PR or change
   the verdict.

The project manager reviews the backlog with the Team Lead at every phase boundary,
recommending a phase or dropping each item. An item whose suggested phase is
the current one goes to the Team Lead in the project manager's next decision batch
instead of waiting for the boundary. The Team Lead plans items into a phase;
nobody starts on a backlog item before then.

**A potential data breach never goes on the backlog.**

- **One the PR adds** is always fixed in that PR before merge.
- **One already on `develop`** that the review uncovers is fixed in the PR
  by the persona that owns the file. Only if the cybersecurity engineer agrees the fix is too
  big for that PR does it wait, as the first work of the current phase,
  fixed before the next deploy.
- **Every one not yet fixed** goes in the
  [security register](/team/QA/notes/cybersecurity-engineer.md#security-register)
  with the gate *before the next deploy*, before the PR merges. The project manager
  checks the register at every phase boundary and before every deploy. Only
  the Team Lead can delay one.

## Disagreements

When an owner and a reviewer disagree, each states its case in one or two
sentences in the findings table, and the finding is marked **Waiting on the
Team Lead**. Personas don't overrule each other. Inside its own area the
owner's view counts most, except on security, where the cybersecurity engineer's counts
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

1. Check the [team board](/team/workspace.md#the-board) for a `[posting]` line on
   the same PR, and wait for it to go. A line older than an hour is stale.
2. Add your own, such as
   `- [posting] DevOps engineer · review of PR #12 · 2026-10-25 21:30`, create the
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
  [Daily notes](/team/workspace.md#daily-notes), and any lasting lesson to its
  notes.
- **After the PR merges or closes,** the owner releases its claim on the
  [board](/team/workspace.md#the-board), and every thread that worked on the PR
  reports its cost to the CFO with the `log-cost` skill and ends.
