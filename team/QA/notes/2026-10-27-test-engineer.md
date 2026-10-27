# Test engineer daily log, 2026-10-27

## Review of PR #88: ask the Team Lead where each deferred finding goes

- Reviewed the one changed sentence in the test engineer persona file
  against the [review protocol](/team/review-protocol.md#follow-up-work)
  and the cross-review skill on the PR branch.
- First minor finding, in my own file: "the owner" could read as the file's
  owner, and the sentence didn't say the reviewer flags the finding.
  Fixed on the PR branch to name the PR's owner and match the skill's
  reviewer step 3.
- Checked the test plan for other review follow-up rules. Its "a failed
  step becomes a GitHub issue" line is about test results, not review
  findings, so it doesn't change.
- Second minor finding, also mine: "a backlog item" could be read as the
  app's Backlog list, which the test plan names on almost every board
  test. Now "a roadmap backlog item" with the glossary link, matching the
  requirements engineer's sentence (`bfd7ee8`).
- Verdict: Recommend.

## Review of PR #89: four options for each deferred finding

- Reviewed the test engineer persona sentence, which now points to
  *Follow-up work* instead of listing the options. It no longer names the
  roadmap backlog, so the Backlog list mix-up fixed on #88 can't come
  back. No change needed in my file.
- One minor finding for the owner, in the review protocol: a deferred
  finding doesn't block the PR, so the PR can merge before the Team Lead
  answers, and then option 1 (fix it in this PR) has no PR left to fix
  in.
- Second minor finding, for the requirements engineer: its persona file
  still says "Don't hand it to another thread to make", which clashes with
  option 2 (a new thread fixes it in a separate PR). The architect fixed
  the same sentence in its own file (`c4ed7ba`).
- Verdict: Recommend with notes.

## Review of PR #91: the screenshot rule moves to the UI/UX designer

- Checked the test plan's PR checklist line, which now links to
  *Screenshots in UI PRs* in the UI/UX designer persona file. The anchor
  resolves at `cc4d695`, where the UI/UX designer added before-and-after
  shots and a test-data-only line to the rule. That now matches the
  checklist, and the test-data line keeps tokens and student data out of
  committed screenshots.
- The checklist also asks for wide and phone widths for layout changes,
  a little more than the rule. That doesn't conflict, so no change.
- The test plan's other `CLAUDE.md` links name the current phase, which is
  still there. Link-only changes don't get a change log row, as on #83 and
  #85.
- No change needed in my files. Verdict: Recommend.
