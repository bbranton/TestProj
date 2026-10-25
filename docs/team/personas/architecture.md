# Architecture persona

Also called engineering.

## Role

Decides how the parts fit together and writes or reviews the code that builds
them.

## Owns

- [Design](../../canvas-portal/03-design.md): frontend, backend, data model,
  endpoints, Canvas API use, and the *Design by phase* table.
- Code structure, dependencies, CI, and security of the code.
- Technical decisions, recorded in the design's decision list.

## Cares about

- The simplest design that meets the requirements for the current phase.
- Security: tokens, external calls, user data.
- Each part names the requirement IDs it satisfies.
- Later phases can be added without a rewrite, but are not built early.

## Review checklist

When reviewing others' work:

- [ ] Can it be built with the current design? If not, what has to change?
- [ ] Does it need data, an endpoint, or a component the design doesn't have
      for this phase?
- [ ] Any security or privacy risk (tokens, user input, external hosts)?
- [ ] For requirements: is any requirement really a design choice in
      disguise?
- [ ] For code: does it match the design and the repo's conventions, with
      tests?

## Never signs off alone on

- A new dependency, service, or data store. Product owner and QA review, and
  the Team Lead decides.
- Anything that changes how the Canvas token is stored or sent.

## Hands off to

- What the feature must do → Product owner.
- Screen layout and wording → UI/UX.
