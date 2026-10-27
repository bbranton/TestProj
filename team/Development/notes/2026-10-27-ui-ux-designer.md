# UI/UX designer, 2026-10-27

## Peer review of the layout-decision rule (PR #91)

- Fresh UI/UX designer thread, reviewing as peer against `develop@dbe3a46`.
- The PR carries out the Team Lead's comment on #76: layout changes go to
  the Team Lead, like new screens and main-flow changes, and the UI/UX
  designer still decides wording and accessibility alone.
- Checked the persona file's *Role* and *Decisions* and the review
  protocol's *Who decides what* row against the comment. Both match it.
- F-1, fixed in the persona file: an accessibility fix can change the
  layout (for example, reflowing a screen so it works when zoomed). The
  file now says such a fix is a layout change and goes to the Team Lead,
  as "When in doubt, it's a decision request" already implies.
- Verdict: Recommend with notes.

## Re-review: screenshot rule moved out of CLAUDE.md (PR #91, 8c85f7d)

- The Team Lead asked on #76 that the screenshot rule leave CLAUDE.md. It
  is now the *Screenshots in UI PRs* section of the UI/UX designer persona
  file, and the PR template, test plan, Canvas portal README, and notes
  link there. No links still point at CLAUDE.md for it, and the anchor
  works.
- F-3, fixed: the new section left out the before-and-after shots that the
  test plan and README require. Added.
- F-4, fixed: screenshots are committed to the repo, so the section now
  says to use test data, with no Canvas token, session, or real student's
  data in any shot.
- F-5, fixed: the notes line repeated the rule; it now points at the
  section instead.
- Verdict: Recommend with notes.

## Confirm the Team Lead's layout decision (PR #91, effd401)

- The Team Lead decided that any layout change, spacing and sizes
  included, goes straight to the Team Lead without the requirements
  engineer's and architect's reviews. New screens and main-flow changes
  keep those reviews. This answers F-2 from the first review.
- effd401 carries it out in the UI/UX designer and architect persona
  files and the review protocol. The UI/UX designer's file matches the
  decision, and F-1 (an accessibility fix that changes layout is a layout
  change) still fits.
- Note F-6: the Team Lead's option was named "Every visual change", but
  the files say "layout change". If colors, fonts, or icons are meant too,
  the files need to say so.
- Verdict: Recommend with notes.
