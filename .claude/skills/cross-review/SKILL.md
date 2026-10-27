---
name: cross-review
description: Run a persona cross-review of a PR or canvas portal doc, following team/review-protocol.md. Use when asked to cross-review, to review as the team, or when called in as a reviewer persona.
---

# Cross-review

Follow [Running reviews with agents](/team/review-protocol.md#running-reviews-with-agents).
What you do depends on whether you are the PR's owner thread or a
reviewer.

## As the owner thread

1. Check the [team board](/team/workspace.md#the-board). If
   another thread already claimed this review, stop and say so. Otherwise
   claim it.
2. Merge `develop` into the branch. If the PR changes a process rule, run
   the [ripple check](/team/review-protocol.md#ripple-check-for-process-rules)
   first. Pick the reviewers as
   [Who reviews what](/team/review-protocol.md#who-reviews-what) says, and
   fill in the *Persona review* section of the PR template with a reason
   for each.
3. Send the coordinator the PR and its reviewers, as
   [One thread per reviewer](/team/review-protocol.md#one-thread-per-reviewer)
   says. Don't write the reviews yourself.
4. Answer or fix each finding as it arrives, as
   [How a review runs](/team/review-protocol.md#how-a-review-runs) says.
   For a question back to a reviewer, follow
   [Questions between threads](/team/review-protocol.md#questions-between-threads).
   For a disagreement, follow
   [Disagreements](/team/review-protocol.md#disagreements). For a finding
   in another persona's files, follow
   [Fixes by another persona](/team/review-protocol.md#fixes-by-another-persona),
   and pull before your next push.
5. After pushing fixes for a **Changes needed** verdict, message that
   reviewer thread to re-review.
6. Post the combined findings table, with anything that needs the Team
   Lead at the top. Send each finding outside the current phase or too big
   for this PR to the Team Lead and list it in the PR's *Deferred findings*
   section, as [Follow-up work](/team/review-protocol.md#follow-up-work)
   says.
7. Merge into `develop` when the review allows it, and close out, as
   [Close out](/team/review-protocol.md#close-out) says. Tell each
   reviewer thread when the PR merges or closes.

## As a reviewer thread

1. Read only what
   [One thread per reviewer](/team/review-protocol.md#one-thread-per-reviewer)
   lists, from `develop`, and cite `develop@<sha>`, as
   [Read from `develop`](/team/review-protocol.md#read-from-develop) says.
2. Use the team skills where they fit: `trace-requirement` for requirement
   IDs and test coverage, `ci-paths` for whether CI runs.
3. Log every problem you find as a finding on this PR, in the
   [findings table](/team/review-protocol.md#findings-table), naming in
   *Fix in* the persona whose file needs the change, as
   [Who fixes a finding](/team/review-protocol.md#who-fixes-a-finding)
   says. When the PR changes a process rule, check it as the
   [ripple check](/team/review-protocol.md#ripple-check-for-process-rules)
   says. Don't open GitHub issues yourself: say when a fix is outside the
   current phase or too big for this PR, and the owner handles it as
   [Follow-up work](/team/review-protocol.md#follow-up-work) says. Handle a
   [potential data breach](/team/QA/personas/cybersecurity-engineer.md#potential-data-breach)
   as that section says.
4. Post one PR review headed with your persona and verdict, as
   [How a review runs](/team/review-protocol.md#how-a-review-runs) says,
   with findings as inline comments.
   Write it fully first, then post it only while you hold the `[posting]`
   line for this PR on the board, as
   [Posting reviews one at a time](/team/review-protocol.md#posting-reviews-one-at-a-time)
   says.
5. Stay open until the owner says the PR merged or closed. Answer the
   owner's questions as
   [Questions between threads](/team/review-protocol.md#questions-between-threads)
   says. When asked to re-review, check only the fixes and post your
   updated verdict. When the owner says the PR is done, report your cost
   with the `log-cost` skill.

To fix a finding in your own persona's files, follow
[Fixes by another persona](/team/review-protocol.md#fixes-by-another-persona).
