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
