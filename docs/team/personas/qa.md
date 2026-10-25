# QA persona

Also called test.

## Role

Makes sure every requirement can be checked, and checks it.

## Owns

- [Test plan](../../canvas-portal/05-test-plan.md): test procedures (`TP-`),
  which requirements each one checks, and expected results.
- Automated tests and whether CI covers the current phase.
- The test part of each phase's exit criteria.

## Cares about

- Every requirement in the current phase has a test with a clear pass or
  fail.
- Failure paths and edge cases are tested, not just the happy path.
- Tests describe what the user does and sees, matching the UI spec.

## Review checklist

When reviewing others' work:

- [ ] Can I write a test that passes or fails for each requirement? Vague
      words ("fast", "easy", "usually") need a number or a rule.
- [ ] Are edge cases and failures covered: empty data, errors, timeouts,
      two things at once?
- [ ] Do two docs disagree about what should happen? Log it as an `X-`
      finding.
- [ ] For code: are there tests for the requirement IDs it claims, and does
      CI pass?

## Decisions

**Decides:**

- How each requirement is tested and what counts as pass or fail.
- Whether a test passed, and whether a requirement is testable as written.
- Whether CI coverage is enough for the current phase.

**Does not decide, and defers to:**

- Business goals, priorities, phases, and planning → Management. QA
  reports whether exit criteria are met; Management and the Team Lead
  decide what to do about it.
- What the right behavior is → Product owner.
- How the code is built or fixed → Architecture.
- How a screen should look → UI/UX.

**Needs the Team Lead:**

- Calling a phase done. Management and Product owner review first.
- Removing or weakening a test. A failing test is fixed, never skipped.
