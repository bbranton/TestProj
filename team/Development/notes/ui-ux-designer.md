# UI/UX designer notes

Lasting lessons for the UI/UX designer persona. See the
[team workspace](/team/workspace.md#persona-notes) for how notes work.

- Every UI PR needs screenshots of each changed page, committed under
  `docs/screenshots/pr-<number>/`, plus a phone-width shot when the layout
  is responsive. The exact embed URL is in
  [Screenshots in UI PRs](/team/Development/personas/ui-ux-designer.md#screenshots-in-ui-prs).
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
  entry point in the same change, then tell the requirements engineer so the
  requirement's phase matches.
- The Team Lead wants no keyboard interactions: every action is a click
  or tap. Don't design Esc, Enter, or shortcut keys; rely on real browser
  controls so Tab and screen readers still work.
- Button IDs are CAPS_WITH_UNDERSCORES, such as `REFRESH`, for logs, docs,
  code, and tests. The label a screen reader announces stays plain words.
- Keep menus light. A long list of cards belongs on the board behind a
  filter, never in a menu. The Team Lead set this for archived and
  orphaned cards.
- Emoji such as 🔒 take two columns in text sketches. Drop a space of
  padding so the box borders still line up.
- A README only describes what's in its folder. Product terms go in the
  [glossary](/docs/canvas-portal/glossary.md).
