---
name: cross-review
description: Run a persona cross-review of a PR or canvas portal doc, following team/review-protocol.md. Use when asked to cross-review, to review as the team, or when called in as a reviewer persona.
---

# Cross-review

Follow [Running reviews with agents](../../../team/review-protocol.md#running-reviews-with-agents).
What you do depends on whether you are the PR's owner thread or a
reviewer.

## As the owner thread

1. Check the [team board](../../../team/workspace.md#the-board). If
   another thread already claimed this review, stop and say so. Otherwise
   claim it.
2. Find the recommended reviewers in the protocol's *Who reviews what*
   table. Add optional reviewers by Management's rule (does the topic call
   for another persona?), and fill in the *Persona review* section of the
   PR template with a reason for each.
3. Send the coordinator the PR and its recommended reviewers. The
   coordinator recommends reviewers to the Team Lead and starts a fresh
   thread only for each one the Team Lead confirms. Don't write the reviews
   yourself. If the Team Lead confirms none, the Team Lead reviews the PR
   directly.
4. Answer or fix each finding as it arrives. For a question back to a
   reviewer, ask on the PR comment, then message that reviewer thread with
   the link. After two rounds without agreement, mark the finding
   **Waiting on the Team Lead**.
5. After pushing fixes for a **Changes needed** verdict, message that
   reviewer thread to re-review.
6. Post the combined findings table, with anything that needs the Team
   Lead at the top. List each issue the reviewers opened in the PR's
   *Follow-ups opened* section. When the PR merges or closes, tell each reviewer thread,
   report your cost with the `log-cost` skill, and release the claim on the
   board.

## As a reviewer thread

1. Read only your persona file, your team's notes in `team/<Team>/notes/`, the
   review protocol, the PR, and the docs the PR changes or names. Don't read the owner's thread or the other
   reviews before writing yours.
2. Use the team skills where they fit: `trace-requirement` for requirement
   IDs and test coverage, `ci-paths` for whether CI runs.
3. For work you find that is outside this PR, open a GitHub issue that
   links the PR, with the owning persona's `persona: <name>` label and
   `needs-triage` (plus `potential-breach` when Security marks it one), and log it as a finding with status "Moved to #issue".
   See [Follow-up work](../../../team/review-protocol.md#follow-up-work).
4. Post one PR review headed with your persona and verdict, such as
   "**DevOps review: Changes needed**", with findings as inline comments.
   Write it fully first, then post it only while you hold the `[posting]`
   line for this PR on the board, as
   [Posting reviews one at a time](../../../team/review-protocol.md#posting-reviews-one-at-a-time)
   says.
5. Stay open until the owner says the PR merged or closed. When the owner
   asks a question, answer on the PR comment, then tell the owner thread.
   When asked to re-review, check only the fixes and post your updated
   verdict. When the owner says the PR is done, report your cost with the
   `log-cost` skill.

Don't fix findings yourself. The owner does that.
