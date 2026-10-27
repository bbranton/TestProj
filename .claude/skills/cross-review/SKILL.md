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
2. Merge `develop` into the branch. Pick the reviewers from the
   protocol's *Who reviews what* table: a peer from your own persona (or,
   for a team thread with no persona, the persona that owns most of the
   changed files), plus each other persona whose area the PR touches. Fill
   in the *Persona review* section of the PR template with a reason for
   each.
3. Send the coordinator the PR and its reviewers. The coordinator starts a
   fresh thread for each one. Don't write the reviews yourself. Every PR has
   at least the peer reviewer; never merge without one.
4. Answer or fix each finding as it arrives. For a question back to a
   reviewer, ask on the PR comment, then message that reviewer thread with
   the link. After two rounds without agreement, mark the finding
   **Waiting on the Team Lead**. For a finding in another persona's files,
   ask that persona's thread to commit the fix to this branch, as
   [Fixes by another persona](../../../team/review-protocol.md#fixes-by-another-persona)
   says, and pull before your next push.
5. After pushing fixes for a **Changes needed** verdict, message that
   reviewer thread to re-review.
6. Post the combined findings table, with anything that needs the Team
   Lead at the top. List each finding marked Backlog in the PR's
   *Backlog items* section, and your `### Decision:` log entries.
   When every verdict is Recommend or Recommend with notes, merge into
   `develop`. Then tell each reviewer thread, release the claim on the
   board, and report your cost with the `log-cost` skill.

## As a reviewer thread

1. Read only your persona file, your persona's notes and recent daily logs
   in your team's `notes/` folder, the review protocol, the PR, and the docs
   on `develop` that the PR changes or names. Cite `develop@<sha>`. Don't read the owner's thread or the other
   reviews before writing yours.
2. Use the team skills where they fit: `trace-requirement` for requirement
   IDs and test coverage, `ci-paths` for whether CI runs.
3. Log every problem you find as a finding on this PR, naming in *Fix in*
   the persona whose file needs the change. Don't open GitHub issues. Mark
   a finding "Backlog" only when its fix is outside the current phase or
   too big for this PR. A potential data breach never is: add it to the
   [security register](../../../team/QA/notes/cybersecurity-engineer.md#security-register)
   too. See
   [Who fixes a finding](../../../team/review-protocol.md#who-fixes-a-finding).
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
