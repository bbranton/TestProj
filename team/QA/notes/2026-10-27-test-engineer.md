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

## Review of PR #115: docs check in CI (#100)

- Ran the script on the branch and on the branch merged with `develop`:
  0 problems both times, exit 0.
- Ran a scratch file of 15 cases through it. It catches a missing file, a
  missing heading, a bad `../blob/develop/` link, and an undefined ID, and
  exits 1. It skips IDs in inline code and in change logs, as intended.
- F-1 (Changes needed): a heading with inline code, such as *Read from
  `develop`* in the review protocol, gets the wrong anchor, so a valid link
  to it fails. Two such headings are on `develop` today.
- F-2 (Changes needed): the check's behavior isn't verified by anything
  committed. The negative test was a one-off on a scratch copy, so a
  regression that makes the check pass everything would stay green.
- Removed requirements counting as defined was already fixed in `ef632ba`
  while I reviewed; checked it reports FR-30 as removed.
- Verdict: Changes needed.
- Re-check at `015bb20`: F-1, F-2, and N-1 fixed. The 13 new tests pass,
  and each of five deliberate breaks to the script (code stripped from
  headings again, a link or ID pattern that matches nothing, exit 0 on
  problems, removed rows counted as defined) makes a test fail. A temp
  repo per test is better than the fixture folder I suggested, since
  committed bad links would fail the check itself.
- Minor: the commit also added two `__pycache__/*.pyc` files. Asked the
  DevOps engineer to remove them and ignore `__pycache__/`.
- Verdict: Recommend with notes.
