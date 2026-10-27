# Requirements engineer log, 2026-10-27

## Review of PR #80: review follow-ups in the same PR or the roadmap backlog

- Reviewed the glossary changes against `develop@d5d0539`: *Follow-up
  issue* and the `backlog` label replaced by *Roadmap backlog*, and the
  Backlog list now points at the new term. No requirement IDs touched.
- Verdict: Recommend with notes
  ([review](https://github.com/bbranton/TestProj/pull/80#issuecomment-6435185149)).
  F-1: *Other IDs* is missing `B-`. F-2: glossary date. F-3 (optional):
  drop the rule sentence from the *Roadmap backlog* meaning. X-1: status
  written as both "Backlog" and "Backlog B-n" in the review protocol.
  X-2: roadmap section 7 leaves out "too big for its pull request".
- No decisions made; the PR carries out the Team Lead's decision.

## Glossary fix on PR #82: every PR has a peer reviewer

- Management's X-1 on #82: *Reviewers* said "one for each area the PR
  touches", which gave an own-area PR none. Reworded it to a same-persona
  peer (for a team thread, the persona that owns most of the changed
  files) plus one per other area, and "Every PR has at least one."
  Committed to the #82 branch, as *Fixes by another persona* says.
- No decisions made; the PR carries out the Team Lead's decision.

## Review of PR #88: the Team Lead decides where each deferred finding goes

- Reviewed the one changed sentence in the requirements engineer persona
  file, and the *Roadmap backlog* glossary row, against `develop@1a3f31f`.
  No requirement IDs touched.
- F-1, fixed on the PR branch: "a backlog item" could be read as the
  portal's *Backlog* list, so the sentence now says *roadmap backlog* and
  links the glossary; it also says to flag the finding, names "the PR's
  owner", links *Follow-up work*, and is wrapped like the rest of the file.
- No decisions made; the PR carries out the Team Lead's decision.

## Review of PR #89: four options for each deferred finding

- Reviewed the requirements engineer persona sentence and the *Roadmap
  backlog* glossary row against `develop@18e59e5`. Both read correctly; the
  sentence now points at *Follow-up work* instead of listing options, so it
  can't drift. No requirement IDs touched.
- X-1 for the project manager: the PR doesn't wait for the answer, so it
  can merge before the Team Lead picks "fix it in this PR".
- No decisions made; the PR carries out the Team Lead's decision.
- Missed in my review: the persona sentence's "Don't hand it to another
  thread" clashed with option 2 (fix in a separate PR by a new thread).
  The owner thread added "unless the Team Lead picks a fix in a separate
  PR" in 31ae463, matching the architect's fix; checked and kept as is.

## Review of PR #94: the retro skill

- Reviewed the new *Retro* glossary row and the skill's words against
  `develop@d3df9bf`. The row sits with the team process terms, matches the
  table's format, and has a change log entry. No requirement IDs touched.
- F-1, fixed on the PR branch: the meaning said who runs a retro but not
  what it is for, and named the `retro` skill without linking it, unlike
  the other team process rows. It now says it is a look back at how well
  the personas work together and links the skill.
- F-2 (optional) for the owner, in the skill: say whether a persona's
  retro feedback goes in its daily log. A point on keeping tokens and
  student data out of the feedback was already fixed in d044ac7.
- No decisions made; the PR carries out the Team Lead's decision.

## Review of PR #112: ripple check for process rules

- Reviewed the new *Ripple check* glossary row and its change log entry
  against `develop@94262eb`. The row sits with the team process terms,
  links the new protocol section, and the change log row cites #96. No
  requirement IDs touched.
- F-1, fixed on the PR branch: the meaning described steps instead of
  saying what the term is, and repeated the protocol's list of places to
  search, which would itself need a ripple check whenever that list
  changes. It also left out that each file's owner makes the fix. It now
  says what the check is, who fixes each file, and links the protocol for
  the rest.
- F-2, fixed on the PR branch: "ripple check" sits close to the project
  manager's *ripple list* for phase and scope decisions, so the row now
  says it isn't that.
- No decisions made; the PR carries out the Team Lead's decision.

## Glossary fix and review of PR #113: one home for the breach rule

- Fixed the *Potential data breach* glossary row on the PR branch. The
  meaning left out acting as the student, so it was narrower than the
  rule's home in the
  [cybersecurity engineer persona](/team/QA/personas/cybersecurity-engineer.md#potential-data-breach).
  It now uses the home's words for what counts and links the home for how
  one is marked and handled. "Always critical and must-fix" is dropped
  from the row, since that is part of the rule and lives only in the home.
  Added a change log entry citing #97.
- Reviewed the whole PR against the glossary and the requirements. No
  requirement IDs touched. Verdict: Changes needed.
- F-1, for the project manager: the ripple check skipped
  `docs/canvas-portal/` apart from the glossary, and the roadmap's risk
  list (section 8) still restates the rule: must-fix, mitigations first in
  the current phase and before the next deploy, only the Team Lead can
  delay one. The roadmap backlog intro (section 9) restates where one is
  tracked instead of linking the home.
- Lesson for the notes: a ripple check for a rule that the docs also
  state covers `docs/` too, not only `team/` and the glossary.
- No decisions made; the PR carries out the Team Lead's decision on #97.
