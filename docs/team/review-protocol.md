# Review protocol

How personas review each other's work. The personas are listed in the
[team README](README.md).

## Who reviews what

Every piece of work has one **owner** persona, who writes it and answers its
findings, and one or more **required reviewers**. Optional reviewers join
when the change touches what they own.

| Work | Owner | Required reviewers | Optional reviewers |
|------|-------|--------------------|--------------------|
| Roadmap (`01-roadmap.md`) | Management | Product owner | Architecture, QA |
| Requirements (`02-requirements.md`) | Product owner | QA, Architecture | UI/UX, Management |
| Design (`03-design.md`) | Architecture | Product owner, QA | UI/UX |
| UI specification (`04-ui-specification.md`) | UI/UX | Product owner, Architecture | QA |
| Test plan (`05-test-plan.md`) | QA | Product owner | Architecture, UI/UX |
| Code PR (backend) | Architecture | QA | Product owner |
| Code PR (frontend or any UI change) | Architecture | UI/UX, QA | Product owner |
| Phase exit (moving to the next phase) | Management | QA, Product owner | Architecture, UI/UX |

Each reviewer looks through its own lens, using the review checklist in its
persona file. For example, QA reads the requirements asking "can I write a
test that passes or fails for this?", not "is this the right feature?".

## How a review runs

1. **Owner prepares.** The owner opens the PR and lists in its description
   the requirement IDs it touches and which reviewers are required, from the
   table above.
2. **Reviewers review.** Each required reviewer reads the change against its
   checklist and posts one review headed with its persona name, such as
   "**QA review**". Reviewers can run in parallel.
3. **Findings are logged.** Each finding gets an ID and a row in a findings
   table (format below). A finding that needs a change in a different doc
   names that doc under **Fix in**, and is fixed in that doc's PR, so each PR
   still changes only what it owns.
4. **Owner answers.** The owner fixes each finding or replies with why not.
   Findings that need a decision go to the Team Lead.
5. **Sign-off.** Each required reviewer ends with one verdict:
   - **Recommend** — no open findings from this reviewer.
   - **Recommend with notes** — only minor findings, which the owner may
     fix later.
   - **Changes needed** — at least one finding must be fixed before merge.
6. **Team Lead decides.** The PR is ready when the owner and every required
   reviewer recommend it. The Team Lead approves and merges. A persona never
   approves or merges.

## Findings table

Use the same shape as the canvas portal docs review:

| # | Found by | Fix in | Finding | Status |
|---|----------|--------|---------|--------|
| F-1 | QA | Requirements | FR-12 says "fast"; give a number so it can be tested. | Open |

- **#** is unique within the review (`F-1`, `F-2`, ...). Findings that span
  several docs use `X-` IDs.
- **Status** is one of Open, Fixed in #PR, Won't fix (with the reason),
  or Waiting on the Team Lead.

## Disagreements

When an owner and a reviewer disagree, each states its case in one or two
sentences in the findings table, and the finding is marked **Waiting on the
Team Lead**. Personas do not overrule each other, and no persona's view
outranks another's. The Team Lead's decision is recorded in the doc's change
log or decision list.

## Running a cross-review with an agent

When asked to "run a cross-review" of a PR or doc, the agent:

1. Finds the owner and required reviewers in the table above.
2. Reviews once per required reviewer, reading that persona's file first and
   staying inside its checklist.
3. Posts one review per persona and a single findings table that combines
   them, with no duplicate findings.
4. Lists any finding that needs the Team Lead's call at the top.

The agent does not fix the findings in the same pass unless the Team Lead
asks it to, so the reviews stay independent of the fixes.
