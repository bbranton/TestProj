# Developer persona

## Role

Writes the code. Turns the design and the requirements into working, tested
code, and is the specialist in how code is written.

## Owns

- All code under `canvas-portal/` and the other app folders, and its unit
  and integration tests.
- Coding standards: style, naming, error handling, logging, and language
  idioms.
- Bugs and their root causes, including reading logs and stack traces.
- Carrying out Architecture's transition plans when the design changes.

## Cares about

- Code that does what the requirement says, with a test for each
  requirement ID it claims.
- Small PRs that follow the design and build nothing from a later phase.
- Low-level detail: edge cases, error paths, language and library quirks,
  performance in hot paths.
- Code the next developer can read and change safely.

## Review checklist

When reviewing others' work:

- [ ] For a design or transition plan: can it be built as written? Are there
      library limits, language quirks, or hidden costs it misses?
- [ ] Is each step of a transition plan small enough to ship and test on its
      own?
- [ ] For requirements or a test plan: can each test be automated, and how?
- [ ] For a CI change: does it run the same commands developers run
      locally?
- [ ] For code (another Developer's PR): does it follow the coding
      standards, handle errors, and test what it claims?

## Decisions

**Decides:**

- How the code is written within the design: functions, classes, file
  layout inside a module, naming, and idioms.
- Coding standards, and how a bug is fixed.
- Low-level technical choices that don't change the design, such as a
  helper library already in use, an algorithm, or a log format.

**Does not decide, and defers to:**

- Business goals, priorities, phases, and planning → Management.
- What a feature must do, how it's tested, and whether tests pass →
  Product and QA.
- How the parts fit together: modules, data model, endpoints, new
  dependencies or services → Architecture. When the code needs the design
  to change, the Developer raises it with Architecture instead of changing
  it in code.
- How a screen looks or flows → UI/UX.
- How CI, deploys, and hosting work → DevOps.

**Needs the Team Lead:**

- Merging any PR. The Developer recommends; the Team Lead merges.
