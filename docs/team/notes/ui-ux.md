# UI/UX notes

Lasting lessons for the UI/UX persona. See the
[team workspace](../workspace.md#persona-notes) for how notes work.

- Every UI PR needs screenshots of each changed page, committed under
  `docs/screenshots/pr-<number>/`, plus a phone-width shot when the layout
  is responsive. The exact embed URL is in [CLAUDE.md](../../../CLAUDE.md).
- Hover can't be the only way to see something, such as a course's full name.
- Until Phase 5 there is no card back, so the card front must show every
  field FR-22 lists (due date and time, points, status). Check sketches
  against FR-22, not just FR-65.
- Give every screen a "When / Message" table for its empty, loading, and
  error states. Reviews kept finding states that only a workflow mentioned.
- Check that example dates in sketches fall on the weekday shown. "Tue Oct
  28" slipped into the spec, and Oct 28, 2026 is a Wednesday.
- When a screen moves to another phase, update the *UI by phase* table,
  the screen map, the button ID table, and every sketch that draws its
  entry point in the same change, then tell Product and QA so the
  requirement's phase matches.
- The Team Lead wants no keyboard interactions: every action is a click
  or tap. Don't design Esc, Enter, or shortcut keys; rely on real browser
  controls so Tab and screen readers still work.
