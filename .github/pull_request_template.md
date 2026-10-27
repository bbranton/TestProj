## Summary

<!-- What changes and why, in a few lines. -->

### Files that state this rule

<!-- For a PR that changes a process rule: every file that states the rule,
     including the ones that needed no change, from the ripple check in
     ../blob/develop/team/review-protocol.md#ripple-check-for-process-rules
     Otherwise write "None: no process rule changes". -->

## Requirement IDs

<!-- The FR- and NFR- IDs this PR implements or changes, or "None" and why.
     Check them with the trace-requirement skill. -->

## Persona review

**Owner:** <!-- the persona that wrote this PR -->

**Based on:** `develop@<sha>` <!-- merge develop in before asking for review -->

Reviewers: a peer from the owner's own persona, plus each other persona
whose area this PR touches, from *Who reviews what* in
[the review protocol](../blob/develop/team/review-protocol.md#who-reviews-what).
Never "None": every PR has at least the peer.

<!-- One line per reviewer, with why. The cybersecurity engineer always reviews anything
     touching tokens, sign-in, secrets, student data, hosting, or deploys;
     say which. Assign the Team Lead, but don't request their review. -->
- Peer (owner's persona, or for a team thread the persona owning most changed files): precaution, every PR
- Persona: reason

### Verdicts

| Reviewer | Verdict | Re-reviewed after fixes |
|----------|---------|-------------------------|
| | Recommend / Recommend with notes / Changes needed | |

### Findings

| # | Found by | Fix in | Finding | Status |
|---|----------|--------|---------|--------|

## Deferred findings

<!-- Each finding outside the current phase or too big for this PR, with
     the persona that owns it, the Team Lead's decision request, and the
     answer: fixed in this PR, separate PR #n, GitHub issue #n, or roadmap
     backlog B-n. "None" when there are none. See "Follow-up work" in the review protocol. -->
- None

## Cost

<!-- For a feature with a cost plan: the plan's estimate. After merge, each
     thread reports its actual cost with the log-cost skill. Delete this
     section for small PRs with no plan. -->
Estimate: 

## Testing

<!-- What you ran and what it showed. The ci-paths skill says whether CI
     runs on this PR. -->

## Screenshots

<!-- Required for any UI change: each changed page, plus a phone-width shot
     when the layout is responsive. How to store and embed them:
     ../blob/develop/team/Development/personas/ui-ux-designer.md#screenshots-in-ui-prs
     Delete this section when nothing in the UI changes. -->
