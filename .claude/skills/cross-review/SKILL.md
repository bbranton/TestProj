---
name: cross-review
description: Run a persona cross-review of a PR or canvas portal doc, following docs/team/review-protocol.md. Use when asked to cross-review, to review as the team, or when called in as a reviewer persona.
---

# Cross-review

Follow [Running reviews with agents](../../../docs/team/review-protocol.md#running-reviews-with-agents).
What you do depends on whether you are the PR's owner thread or a
reviewer.

## As the owner thread

1. Check the [team board](../../../docs/team/workspace.md#the-board). If
   another thread already claimed this review, stop and say so. Otherwise
   claim it.
2. Find the required reviewers in the protocol's *Who reviews what* table.
   Then, as Management, check whether the topic calls for any other persona.
3. Ask the coordinator for one fresh thread per reviewer, naming the PR and
   the persona. Don't write the reviews yourself.
4. Answer or fix each finding as it arrives. For a question back to a
   reviewer, ask on the PR comment, then message that reviewer thread with
   the link. After two rounds without agreement, mark the finding
   **Waiting on the Team Lead**.
5. Post the combined findings table, with anything that needs the Team
   Lead at the top, then release the claim on the board.

## As a reviewer thread

1. Read only your persona file, your notes in `docs/team/notes/`, the
   review protocol, and the PR. Don't read the owner's thread or the other
   reviews before writing yours.
2. Use the team skills where they fit: `trace-requirement` for requirement
   IDs and test coverage, `ci-paths` for whether CI runs.
3. Post one PR review headed with your persona and verdict, such as
   "**DevOps review: Changes needed**", with findings as inline comments.
4. Stay open until the PR merges. When the owner messages you, answer on
   the PR comment, then tell the owner thread that you answered.

Don't fix findings yourself. The owner does that.
