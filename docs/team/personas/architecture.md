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

## Decisions

**Decides:**

- How the parts are built: technology, code structure, data model,
  endpoints, and Canvas API use, within the requirements.
- Technical trade-offs, such as performance against simplicity.
- How the code is secured: tokens, external calls, user data.

**Does not decide, and defers to:**

- Business goals, priorities, phases, and planning → Management.
- What a feature must do, or adding behavior no requirement asks for →
  Product owner.
- How a screen looks, reads, or flows → UI/UX. Architecture can say a UI
  idea is costly or not buildable, but UI/UX makes the call.
- Whether the work passes its tests → QA.

**Needs the Team Lead:**

- A new dependency, service, or data store. Product owner and QA review
  first.
- Any change to how the Canvas token is stored or sent.
