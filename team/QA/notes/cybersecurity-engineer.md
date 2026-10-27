# Cybersecurity engineer notes

Lasting lessons for the cybersecurity engineer persona. See the
[team workspace](../../workspace.md#persona-notes) for how notes work.

- The Canvas token is the most harmful thing to leak: a personal access
  token works for the student's whole Canvas account until they delete it.
  Trace where it goes first in every review.
- Every PR posts from the Team Lead's GitHub account, and screenshots go in
  the repo. Check that no PR body, comment, screenshot, or fixture holds a
  real token, name, or course (A-3).
- The design's security table is section 7 of
  [03-design.md](../../../docs/canvas-portal/03-design.md#7-security); the
  security requirements are NFR-10 to NFR-14. Start a review there.
- Joining late is what costs most: on the roadmap review (#4) the cybersecurity engineer
  came in after the hosting choice, and three findings were potential data
  breaches. Review hosting, deploy, and token choices while they're made.
- Check the review-protocol rule on every token-touching PR: the cybersecurity engineer was
  missing from the requirements review (#6) until the project manager and
  the architect flagged it, and both raised the same NFR-11 finding.

## Current threat picture

Update this when hosting, the repo, or where real tokens live changes.

- The repo is public. Workflow artifacts and logs can be downloaded by any
  GitHub user.
- Phase 1 step 6 deploys to a free Koyeb app with a Neon free database,
  holding real Canvas tokens. `koyeb.app` isn't on the Public Suffix List.
- Only the Team Lead's own accounts should connect until #16 is published
  and #17 is in place.

## Security register

Open security findings and potential data breaches. **Gate** is the phase
step the item must be done before. Clear a row only when it's fixed, and
say where. A **Proposed** gate isn't in the roadmap yet; the project manager
decides it. Review follow-ups don't become GitHub issues any more (Team
Lead, 2026-10-27, PR #80), so a potential data breach that isn't fixed
in the PR it was found in is tracked only here: add its row before that
PR merges. The rows below that link issues are from before the change.

| Item | Potential data breach | Owner | Gate | Status |
|------|-----------------------|-------|------|--------|
| #25 Session cookie and writes on Koyeb's shared domain | Yes | Architect | Phase 1 step 6 | Open |
| #26 Deploy secrets and backups private on a public repo | Yes | DevOps engineer | Phase 1 step 6 | Open |
| #17 Incident plan | No | Cybersecurity engineer | Phase 1 step 6 | Open |
| #19 Key and session secret storage and rotation | No | DevOps engineer | Phase 1 step 6 | Open |
| #20 Secret scanning and dependency alerts | No | DevOps engineer | Phase 1 step 6 | Open |
| #46 Team Lead decisions on token storage and sending | No | Architect (cybersecurity engineer briefs) | Phase 1 step 2 | Open |
| #18 Output escaping and a Content-Security-Policy | No | Architect | Proposed: Phase 1 step 6 | Open |
| #22 Tests for reused session cookies and HTML in Canvas text | No | Test engineer | Proposed: Phase 1 exit | Open |
| #21 Token expiry and deleting the token in Canvas | No | Requirements engineer | Proposed: Phase 1 step 6 | Open |
| #16 Client security document | No | Cybersecurity engineer | Anyone but the Team Lead connects | Open |
