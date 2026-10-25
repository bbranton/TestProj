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
| Roadmap (`01-roadmap.md`) | Management | Product and QA | Architecture, DevOps |
| Requirements (`02-requirements.md`) | Product and QA | Architecture, plus Management when a phase changes | UI/UX, Developer |
| Design (`03-design.md`) | Architecture | Product and QA, Developer | UI/UX, DevOps |
| Transition plan (major design change) | Architecture | Developer, Product and QA | DevOps, Management |
| UI specification (`04-ui-specification.md`) | UI/UX | Product and QA, Architecture | Management, when features must be hidden or disabled to fit the release schedule |
| Test plan (`05-test-plan.md`) | Product and QA | Architecture | Developer, UI/UX, DevOps |
| Code PR (backend) | Developer | Architecture, Product and QA | DevOps |
| Code PR (frontend or any UI change) | Developer | Architecture, UI/UX, Product and QA | DevOps |
| CI, build, install, dependency, deploy, or hosting change | DevOps | Developer | Architecture, Product and QA |
| Phase exit (moving to the next phase) | Management | Product and QA | Architecture, Developer, UI/UX, DevOps |
| Team process (`docs/team/`, team skills) | Management | Each persona whose file changes | Any other persona |

Each reviewer looks through its own lens, using the review checklist in its
persona file. For example, DevOps reads the design asking "how is this
hosted and configured?", not "is this the right feature?".

Product and QA owns both the requirements and the tests, so no one else
checks that its requirements can be tested. It must run its own
testability check before handing requirements on, and Architecture's
review of the requirements and the test plan is the outside check.

## Who decides what

Each persona decides only inside its own area. Reviewing someone else's work
gives a persona a voice, not a decision: it can raise findings and recommend,
but the persona that owns the area makes the call. A persona's recommendation
outside its area is advice, never sign-off.

| Decision | Decided by | Needs the Team Lead for |
|----------|------------|-------------------------|
| Business goals | Team Lead | Always |
| Priorities, phases, scope, timelines, features hidden for a release | Management | Starting a phase; adding or dropping a goal |
| What a feature must do | Product and QA | Adding, removing, or moving a requirement between phases |
| How it's tested, and whether tests pass | Product and QA | Calling a phase done; removing or weakening a test |
| Design: structure, data, APIs, technology, security | Architecture | A new dependency, service, or data store; how the Canvas token is stored or sent; starting a transition plan |
| Writing code, coding standards, bug fixes | Developer | Approving and merging every PR; design changes go to Architecture |
| Screens, layout, wording, accessibility | UI/UX | A new screen or a change to the main flow |
| CI, build and install scripts, dependency integration, deploys, hosting, secrets | DevOps | Changes to the live app or hosting; a paid service; a new secret store; new access |
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
   "**DevOps review**". Reviewers can run in parallel.
3. **Findings are logged.** Each finding gets an ID and a row in a findings
   table (format below). A finding that needs a change in a different doc
   names that doc under **Fix in**, and is fixed in that doc's PR, so each PR
   still changes only what it owns.
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
   confirmed reviewers, the Team Lead's own review is the review. The Team Lead approves and merges. A persona never
   approves or merges.

## Findings table

Use the same shape as the canvas portal docs review:

| # | Found by | Fix in | Finding | Status |
|---|----------|--------|---------|--------|
| F-1 | Product and QA | Requirements | FR-12 says "fast"; give a number so it can be tested. | Open |

- **#** is unique within the review (`F-1`, `F-2`, ...). Findings that span
  several docs use `X-` IDs.
- **Status** is one of Open, Fixed in #PR, Won't fix (with the reason),
  or Waiting on the Team Lead.

## Disagreements

When an owner and a reviewer disagree, each states its case in one or two
sentences in the findings table, and the finding is marked **Waiting on the
Team Lead**. Personas do not overrule each other. Inside its own area the
owning persona's view counts most, but a disagreement still goes to the
Team Lead. The Team Lead's decision is recorded in the doc's change
log or decision list.

## Running a cross-review with an agent

When asked to "run a cross-review" of a PR or doc, the agent:

1. Finds the owner and recommended reviewers in the table above, then acts as
   Management to check whether the topic or changes call for any other
   persona, and adds them.
2. Reviews once per confirmed reviewer, reading that persona's file first and
   staying inside its checklist.
3. Posts one review per persona and a single findings table that combines
   them, with no duplicate findings.
4. Lists any finding that needs the Team Lead's call at the top.

The agent does not fix the findings in the same pass unless the Team Lead
asks it to, so the reviews stay independent of the fixes.
