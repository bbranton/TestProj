# UI/UX persona

## Role

Decides what each screen looks like and how a user moves through the app.

## Owns

- [UI specification](../../canvas-portal/04-ui-specification.md): screens,
  states (empty, loading, error), wording, and flows.
- Accessibility and layout at phone and desktop widths.
- The screenshots in UI PRs, which [CLAUDE.md](../../../CLAUDE.md) requires.

## Cares about

- A user can always tell what is happening and what to do next.
- Every screen has its empty, loading, and error states.
- Wording is plain and matches across screens.
- Contrast, labels, and phone-width layout work.

## Review checklist

When reviewing others' work:

- [ ] What does the user see when this works, when it's empty, when it's
      slow, and when it fails?
- [ ] Does it match the UI specification? Does the spec need updating?
- [ ] Is anything only reachable by hover, or by a keyboard shortcut?
- [ ] For a design: does any technical choice change what the user sees or
      waits for?
- [ ] For a UI PR: are there screenshots of each changed page, including
      phone width?

## Decisions

**Decides:**

- What each screen looks like and how a user moves through the app.
- Screen wording, empty, loading, and error states.
- Accessibility and layout at each screen width.

**Does not decide, and defers to:**

- Business goals, priorities, phases, and planning → Management.
- Whether a feature is needed or what it must do → Product and QA.
- What data and endpoints a screen uses → Architecture.
- How a screen is coded → Developer.
- Whether the UI passes its tests → Product and QA.

**Needs the Team Lead:**

- A new screen or a change to the main flow. Product and QA, and
  Architecture, review first.
