---
name: cross-review
description: Run a persona cross-review of a PR or canvas portal doc, following docs/team/review-protocol.md. Use when asked to cross-review, or to review as the team.
---

# Cross-review

1. Read [the review protocol](../../../docs/team/review-protocol.md) and the
   [team board](../../../docs/team/workspace.md#the-board). If another
   thread already claimed this review, stop and say so.
2. Claim the review on the board.
3. Find the owner and required reviewers in the protocol's *Who reviews
   what* table. Then, as Management, check whether the topic calls for any
   other persona, and add them.
4. For each reviewer: read its persona file and its notes in
   `docs/team/notes/`, review only through its checklist, and write one
   review headed with its name, such as "**DevOps review**".
5. Use the team skills where they fit: `trace-requirement` for requirement
   IDs and test coverage, `ci-paths` for whether CI runs.
6. Combine all findings into one findings table, without duplicates, with
   anything that needs the Team Lead at the top.
7. Post the reviews, then release the claim on the board.

Don't fix findings in the same pass unless the Team Lead asks.
