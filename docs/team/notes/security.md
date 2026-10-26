# Security notes

Lasting lessons for the Security persona. See the
[team workspace](../workspace.md#persona-notes) for how notes work.

- The Canvas token is the most harmful thing to leak: a personal access
  token works for the student's whole Canvas account until they delete it.
  Trace where it goes first in every review.
- Every PR posts from the Team Lead's GitHub account, and screenshots go in
  the repo. Check that no PR body, comment, screenshot, or fixture holds a
  real token, name, or course (A-3).
- The design's security table is section 7 of
  [03-design.md](../../canvas-portal/03-design.md#7-security); the
  security requirements are NFR-10 to NFR-14. Start a review there.
