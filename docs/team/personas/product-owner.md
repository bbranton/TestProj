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

## Never signs off alone on

- Adding, removing, or changing the phase of a requirement. QA and
  Architecture review it, and the Team Lead decides.

## Hands off to

- How it's built → Architecture.
- How it looks → UI/UX.
- Whether it can be tested → QA.
