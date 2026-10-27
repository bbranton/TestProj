# 2026-10-27 · Security

## Security review of PR #80 (review follow-ups in the same PR or the roadmap backlog)

- Reviewed the cybersecurity engineer persona changes and how a potential
  data breach is handled now that review follow-ups don't become GitHub
  issues. Read from `develop@d5d0539` and the PR head `1c0d371`.
- Fixed Security's own files on the PR branch, as the new
  *Fixes by another persona* steps say: the persona file now says how a
  breach the PR adds, one already on `develop`, and one found outside any
  review are each handled, and that the security register is where an
  unfixed breach is tracked. Added the same lesson to the Security notes.
- Raised two findings in the review protocol for the PR's owner: a breach
  the PR itself adds must never use the "too big for this PR" path, and
  the protocol should name the security register as where an unfixed
  breach is tracked.

## Security review of PR #88 (the Team Lead decides issue or backlog for each deferred finding)

- Reviewed the breach handling in *Follow-up work* against `develop@1a3f31f`
  and the PR at `9f64a55`. A potential data breach stays out of the
  issue-or-backlog choice and is fixed or tracked in the security register.
- Fixed Security's own files on the PR branch: the persona file's
  "follow-ups no longer become GitHub issues" sentence and the register
  note now match the new rule. Added that any other deferred security
  finding also gets a register row linking its issue or `B-` item.
- Noted for the incident plan (#17): a deferred security finding sent to
  an issue describes a weakness in public, since the repo is public.

## Security review of PR #90 (later-phase fixes under the phase scope budget)

- Fixed the project manager's F-3 in my own files: a deferred security
  finding's register row also links a separate fix PR (the "fix it now in
  a separate PR" option from #89), and stays until that PR merges. The
  register note lists all four options.
- Read the new scope-budget paragraph in *Follow-up work*: it changes no
  breach handling, since a potential data breach never goes through the
  four options.

## Security review of PR #92 (setup guide for a new project)

- Reviewed `SETUP-NEW-PROJECT.md` at `4e51648`, after the owner refocused
  it at the Team Lead's ask on setup done outside the repo. Sent four
  early points on the first version; the owner folded all of them in
  before this review: the Remote Control approval covers only the repo's
  folder, a public repo is cloned over HTTPS with no credentials (a
  private one with a read-only deploy key), the guide says the standing OK
  is an instruction and not a technical limit, and the GitHub step turns
  on secret scanning, push protection, and Dependabot alerts.
- Verdict Recommend with notes: name the folder in the standing OK's
  words, and optionally set Actions' default token to read-only. No
  potential data breach, and no register row needed.
- Added the Team Lead's local clone to the threat picture in the
  cybersecurity engineer notes.


## One home for the potential data breach rule (#97, PR 1 of 5)

- Made the *Potential data breach* section of the cybersecurity engineer
  persona the rule's only home: what counts, the **Potential data breach:**
  marker, never Won't fix without the Team Lead, critical and must-fix,
  only the Team Lead can delay it, fix timing, never deferred, and the
  project manager's register checks. It no longer points back to the
  project manager persona for "critical and must-fix", which was the loop
  #97 found.
- The security register intro in the cybersecurity engineer notes now
  links to that section instead of restating it.
- The other copies (review protocol, team README, project manager and
  DevOps engineer personas, `cross-review` skill, glossary) are each
  changed by the persona that owns the file, on this PR's branch.

### Decision: state each team rule once, in its home file, and make CLAUDE.md an index

- **Date:** 2026-10-27
- **Decided by:** Team Lead
- **Options:** 1, one `team/rules.md` for every rule; 2, each rule stated
  once in its owner's file, with every other file linking to it; 3,
  CLAUDE.md as a one-line-per-rule index, on top of 1 or 2; 4, a CI check
  for copied rule text
- **Recommendation:** 2 plus 3, holding 4, since 2 keeps each rule with
  the persona who decides it and 3 keeps CLAUDE.md from silently losing
  rules
- **Outcome:** 2 plus 3, as recommended. 4 not adopted for now. The
  widened decision replaces #97's original question, and rolls out in
  five PRs, the breach rule first
- **Links:** [#97 decision](https://github.com/bbranton/TestProj/issues/97#issuecomment-6440241457),
  [Potential data breach](/team/QA/personas/cybersecurity-engineer.md#potential-data-breach)
