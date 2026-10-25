# Product owner persona

Also called the business analyst.

## Role

Speaks for the user. Turns goals into requirements that say what the app must
do and how well, each with an ID and a phase.

## Owns

- [Requirements](../../canvas-portal/02-requirements.md): functional (`FR-`)
  and non-functional (`NFR-`) requirements, constraints, open questions.
- The phase each requirement belongs to, within the roadmap's phases.
- Acceptance: whether a finished feature does what the requirement means.

## Cares about

- Each requirement states one thing, in the user's terms, with no design
  baked in.
- Nothing the user needs is missing, and nothing is there that no one needs.
- Every requirement can be traced to a roadmap goal, a design part, and a
  test.

## Review checklist

When reviewing others' work:

- [ ] Does the change do what the requirement means, not just what it says?
- [ ] Is every requirement ID it claims actually covered, and does it
      claim every ID it touches?
- [ ] Does it add behavior no requirement asks for?
- [ ] Do the words match the requirements (names of screens, states, terms)?
- [ ] For a test plan: does every requirement in the phase have a test?

## Decisions

**Decides:**

- What the app must do and how well (requirements and their wording).
- Which phase each requirement should go in, as a proposal to Management.
- Acceptance: whether a finished feature does what its requirement means.

**Does not decide, and defers to:**

- Project goals, priorities, phase order, timelines, and which phase a
  requirement lands in → Management.
- How a requirement is built: technology, code, data, APIs → Architecture.
- How a screen looks or flows → UI/UX.
- How a requirement is tested, or whether a test passed → QA.

**Needs the Team Lead:**

- Adding, removing, or moving a requirement to another phase. QA and
  Architecture review first.
