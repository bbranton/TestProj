# Review protocol

How personas review each other's work. The personas are listed in the
[team README](/team/README.md).

The Team Lead has the final say, as [CLAUDE.md](/CLAUDE.md#team-personas)
says, so everything below is the default when the Team Lead hasn't said
otherwise.

## The rules in short

1. **Two levels of review.** PRs into `develop` are reviewed by personas
   and merged by their owner. The `develop` → `main` release PR is the
   Team Lead's alone, as [Branches](/CLAUDE.md#branches) says.
2. **The Team Lead decides; PRs carry out decisions.** Every real
   decision goes to the Team Lead right away as a decision request,
   answered before anyone edits a doc for it.
3. **Each persona fixes its own files.** A finding is fixed in the PR it
   was found in, by the persona that owns the file, which may be the
   owner or a reviewer. No persona edits another persona's files.
4. **Read from `develop`.** Open PRs are drafts, never the source of
   truth.
5. **Small, focused PRs.** One job per PR.
6. **The author picks reviewers by what the PR touches.** Reviews are
   quick, and the author pushes fixes right away.
7. **Close out.** Log the decision, report the cost, and end the thread.
8. **A rule change fixes every copy.** A PR that changes a process rule
   runs a [ripple check](#ripple-check-for-process-rules) first.

## Two levels of review

**Into `develop`.** The owner persona opens the PR, picks its reviewers
(see [Who reviews what](#who-reviews-what)), and assigns the Team Lead as
[Branches](/CLAUDE.md#branches) says. Once every
reviewer's latest verdict is **Recommend** or **Recommend with notes**, the
owner thread merges the PR itself and posts the link in its thread.

**`develop` → `main`.** This is a batched release of what's on `develop`.
Who opens and merges it is in [Branches](/CLAUDE.md#branches).
Its summary groups everything merged since `main` by area, with links to
the merged PRs, whose descriptions show the screenshots of any UI change,
as [Screenshots in UI PRs](/team/Development/personas/ui-ux-designer.md#screenshots-in-ui-prs)
says.

## Decisions are separate from merging

The Team Lead makes every real decision, explicitly. A PR is never where a
decision is made or approved: it only carries out decisions already made.
That is why a persona can merge into `develop` without the Team Lead.

- **What goes to the Team Lead:** scope and phases, security and risk
  (token handling, accepting a known risk), hosting and domains, anything
  that costs money or changes the deploy, and team structure and process.
- **What an owner decides alone:** details inside its own area that no
  other doc depends on, such as a requirement's wording, a test case, or a
  screen's wording. When in doubt, it's a decision request.
- **A decision request** states the question, what the problem is and
  why it came up, the options, a recommendation, and the docs it changes.
  Each persona whose area it affects adds its impact: which of its files
  change, and how.
- **Ask the Team Lead right away** (Team Lead, 2026-10-27, on
  [#132](https://github.com/bbranton/TestProj/pull/132)). The persona that
  raises a request asks the Team Lead as soon as it comes up, in the
  thread that raised it, or in the project chat when there is no thread.
  The Team Lead can then ask follow-up or clarifying questions there, and
  the persona answers them in the same place. Don't hold a request to
  batch it, or leave it only in a file or an issue: a question that isn't
  asked right away may never be seen.
- **The Team Lead's answer can be anything:** one of the options, a fix
  right now, a GitHub issue for later, or a request for more information.
  A GitHub issue is one answer the Team Lead can pick, not where the
  question is asked.
- **The register is the record.** The project manager records each
  request, with a link to where it was asked, and then its answer in the
  [decision register](/docs/canvas-portal/01-roadmap.md#5-open-decisions).
  A GitHub issue labeled `decision`, when there is one, is also a record
  of the request and its answer. Only after an answer do the owners make
  their edits, citing the decision.
- **A PR that needs a new decision stops.** The owner raises a decision
  request and waits for the answer before going on. A finding that needs
  one is marked **Waiting on the Team Lead**. A deferred finding, asking
  where work outside the PR's scope goes, is the exception: it doesn't
  stop the PR unless the owner recommends fixing it in this PR, as
  [Follow-up work](#follow-up-work) says.

### Ripple check for process rules

**A rule is stated only in its home.** Each team rule is stated once, in
the file of the persona or doc that owns it, under a stable heading. Every
other file links to that heading instead of restating it (Team Lead,
[#97](https://github.com/bbranton/TestProj/issues/97)). The homes:

- Reviews, decisions, findings, and follow-up work: this protocol.
- Team folders, notes, daily logs, skills, the PR template, the board, and
  threads: the [team workspace](/team/workspace.md).
- Security is everyone's job: the
  [team README](/team/README.md#security-is-everyones-job).
- Potential data breach: the
  [cybersecurity engineer persona](/team/QA/personas/cybersecurity-engineer.md#potential-data-breach).
- Cost reporting and the cost log: the
  [CFO persona](/team/Management/personas/cfo.md#role).
- Screenshots in UI PRs: the
  [UI/UX designer persona](/team/Development/personas/ui-ux-designer.md#screenshots-in-ui-prs).
- What each persona decides: the *Decisions* section of its persona file.
- Links, naming, branches, phases, and the Team Lead's final say:
  [CLAUDE.md](/CLAUDE.md).

The [rule index](/CLAUDE.md#rule-index) in CLAUDE.md has one line per
rule, naming it and linking to its home. A PR that adds a rule, or moves
or renames its home, updates that line.

Older copies are being replaced with links, one owner at a time. A PR
that changes a process rule finds and fixes every copy before review (Team Lead,
[#96](https://github.com/bbranton/TestProj/issues/96)):

1. Change the rule in its home. Search `team/`, `.claude/skills/`,
   `CLAUDE.md`, the PR template (`.github/pull_request_template.md`), and
   the [glossary](/docs/canvas-portal/glossary.md) for the rule's key
   words and for links to its heading. Skip retro notes and the daily
   logs in the Library: they record what was true that day. When a
   persona's notes in the Library restate the rule, leave that persona a
   board `[note]` to fix them.
2. Fix every file that still states the old rule in the same PR, by
   replacing the copy with a link to the home, and fix any link the change
   breaks. The persona that owns each file fixes it, as
   [Fixes by another persona](#fixes-by-another-persona) says, and joins
   the reviewers.
3. List every file that states the rule under *Files that state this
   rule* in the PR description, including the ones that needed no change.

A reviewer who finds a file still stating the old rule, or a rule restated
outside its home, logs it as a finding on the PR.

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
touches.** Every PR has at least the peer, as a precaution, even when it
touches only the owner's area. The peer runs in a fresh thread, like every
reviewer. When the author isn't a persona, the peer is the persona that
owns most of the changed files. A persona's area is its own files in its
team folder (its persona file) and the docs it owns
in the table below. The author lists the reviewers in the PR description, with
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
| Canvas tokens, sign-in, the session cookie, secrets, student data, hosting, or deploys; the client security document (`06-security-overview.md`) or the security register (`team/QA/security-register.md`) | Cybersecurity engineer, always | Cybersecurity engineer |
| Shared files at the top of `team/`, or another team's folder | Each persona whose file changes, plus the project manager (a board note instead, for a [wording-only change](#wording-only-changes-notify-the-persona) to a persona file) | Project manager |
| Another persona's files in your own team's folder | That persona (a board note instead, for a [wording-only change](#wording-only-changes-notify-the-persona) to a persona file) | That persona |
| A team script or its skill (see [Team skills](/team/workspace.md#team-skills)) | The other personas who use it | The team whose `scripts/` folder holds it |
| Only your own persona's area: its persona file, or a doc it owns in this table | The peer reviewer only | That persona |

A code PR always has the Test engineer as a reviewer, since every change
needs a test. A PR that changes a phase or a priority always has
the project manager.

Each reviewer looks through its own lens, using the review checklist in its
persona file, and checks that the words match the
[glossary](/docs/canvas-portal/glossary.md). Every reviewer also checks
for security risks, as
[Security is everyone's job](/team/README.md#security-is-everyones-job) says.

### Wording-only changes notify the persona

When a PR changes another persona's persona file only in wording or a
link, without changing what that persona does, decides, or reviews, that
persona is notified instead of made a reviewer (Team Lead, 2026-10-27,
[#99](https://github.com/bbranton/TestProj/issues/99)):

- The owner leaves that persona a `[note]` on the
  [board](/team/workspace.md#the-board) naming the PR and the change, and
  lists it under *Persona review* in the PR description as
  `- Notified: <persona>: <change>`.
- The persona reads the change at its next own thread, fixes anything it
  disagrees with in its own PR, and deletes the note.
- The PR's peer reviewer judges whether each such change is wording-only.
  If in doubt, the persona reviews.
- The "always" rules above still apply, so a change touching the
  cybersecurity engineer's area always has the cybersecurity engineer.

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
| Feature priorities within a phase, the order of work, the roadmap backlog, keeping the decision register, rating risks | Project manager | Every scope, roadmap, or phase change; adding or dropping a goal; accepting a risk instead of reducing it |
| How a requirement is worded and traced | Requirements engineer | Adding, removing, or moving a requirement between phases |
| How it's tested, and whether tests pass | Test engineer | Calling a phase done; removing or weakening a test |
| Design: structure, data, APIs, technology, security design | Architect | A new dependency, service, or data store; how the Canvas token is stored or sent; starting a transition plan |
| Writing code, coding standards, bug fixes | Developer | Design changes go to the architect first |
| Screens, layout, wording, accessibility | UI/UX designer | A new screen, any visual change (layout, spacing, sizes, colors, fonts, icons), or a change to the main flow |
| CI, tooling, build and install scripts, branch mechanics, dependency integration | DevOps engineer | Changes to the live app or hosting; a paid service; a new secret store; new access |
| Whether a weakness is a vulnerability, its severity, and whether it is a potential data breach; the client security document | Cybersecurity engineer | Accepting a vulnerability instead of fixing it; publishing the client security document; telling anyone outside the team about a suspected leak |
| What goes in the cost log | CFO | Changing the log's columns or how threads report cost |
| Merging a PR into `develop` | The PR's owner, once its reviewers recommend it | Never: the PR only carries out decisions already made |
| Approving and merging the `develop` → `main` release PR | Team Lead | Always |

This table is a summary. Each persona file's **Decisions** section is the
home of what it decides, what it defers and to whom, and what needs the
Team Lead, and wins where the two differ.

## How a review runs

1. **Owner prepares.** The owner merges `develop` into its branch, opens
   the PR, and fills in the PR template: requirement IDs, reviewers, and
   why. A PR that changes a process rule runs the
   [ripple check](#ripple-check-for-process-rules) first.
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
- **Outside the current phase, or too big for this PR:** the Team Lead
  decides where it goes, as [Follow-up work](#follow-up-work) says.

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
  isn't the owner), Fixing in `#<n>` (a separate PR), Issue `#<n>`,
  Backlog `B-<n>`, Won't fix (with the reason), or Waiting on the Team
  Lead.
- A finding that is a [potential data breach](/team/QA/personas/cybersecurity-engineer.md#potential-data-breach) is
  marked and handled as that section says.

## Follow-up work

Nothing a review finds is parked without the Team Lead's say. Work a
review uncovers goes one of two ways:

1. **This PR, when it's in the current phase.** The persona that owns the
   file fixes it here, as [Who fixes a finding](#who-fixes-a-finding) says.
2. **The Team Lead decides, when it's outside the current phase or too big
   for this PR.** The owner asks the Team Lead right away, as
   [Decisions are separate from merging](#decisions-are-separate-from-merging)
   says, with one decision request for that finding that links to it and
   gives these four options and a recommendation:
   1. **Fix it now in this PR**, even though it's outside the phase or
      bigger than the PR was meant to be. The persona that owns the file
      fixes it here, and the status becomes Fixed in `<sha>`.
   2. **Fix it now in a separate PR.** The owner asks the coordinator for a
      new thread of the persona that owns the file, which starts right away
      and fixes it in its own PR into `develop`. The status becomes Fixing
      in `#<n>`.
   3. **A GitHub issue**, labeled with the owning persona's `persona:`
      label, for work that should be picked up soon but not right now.
   4. **The [roadmap backlog](/docs/canvas-portal/01-roadmap.md#9-backlog)**,
      for work that belongs in a later phase.

   For later-phase work, options 1 and 2 grow the current phase, so the
   decision request says what the fix displaces, or asks the Team Lead to
   let the phase grow, as the scope budget allows, and the project manager
   logs it under the
   [phase scope budget](/team/Management/personas/project-manager.md#how-it-works).

   The finding is **Waiting on the Team Lead** and is listed in the PR's
   *Deferred findings* section. It doesn't change the verdict. When the
   owner recommends option 1, the PR waits for the answer. Otherwise it
   doesn't block the PR, which may merge before the answer comes; if the
   Team Lead then picks option 1 anyway, the fix goes in a separate PR, as
   in option 2. When the Team Lead answers,
   the owner carries it out: fixes it here, asks for the new thread, opens
   the issue, or lists the item for the project manager, and updates the
   status. If the owner's thread has ended, the project manager does it.

The project manager adds each backlog item to the roadmap as soon as the
Team Lead picks the backlog, in a small roadmap PR of its own, with a `B-`
ID, the PR it came from, and the persona that owns it. It
reviews the backlog with the Team Lead at every phase boundary,
recommending a phase or dropping each item. The Team Lead plans items into
a phase; nobody starts on a backlog item before then.

**A potential data breach never goes through this choice.** It is
handled as [Potential data breach](/team/QA/personas/cybersecurity-engineer.md#potential-data-breach) says.

## Disagreements

When an owner and a reviewer disagree, each states its case in one or two
sentences in the findings table, and the finding is marked **Waiting on the
Team Lead**. Personas don't overrule each other. Inside its own area the
owner's view counts most, except on security, as
[Security is everyone's job](/team/README.md#security-is-everyones-job)
says. After two rounds on the same point without agreement, the owner
marks the finding **Waiting on the Team Lead**.

## Running reviews with agents

### One thread per reviewer

- Each reviewer runs in **its own fresh thread**. It reads only its
  persona file, its own notes and recent daily logs (in
  Library: `notes/`, as [Persona notes](/team/workspace.md#persona-notes)
  says), this protocol, the
  PR, and the docs on `develop` that the PR changes or names. It doesn't
  see the owner's thread or other reviews before writing its own.
- The owner sends the coordinator the PR and its reviewers, and the
  coordinator starts one thread per reviewer, as
  [One thread per PR](/team/workspace.md#one-thread-per-pr) says.
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
  decision to the *Decisions* section of the PR description, in the format
  in [Daily notes](/team/workspace.md#daily-notes), and any lasting lesson to
  its [notes](/team/workspace.md#persona-notes).
- **After the PR merges or closes,** the owner releases its claim on the
  [board](/team/workspace.md#the-board), and every thread that worked on the PR
  reports its cost and ends, as
  [One thread per PR](/team/workspace.md#one-thread-per-pr) says.
