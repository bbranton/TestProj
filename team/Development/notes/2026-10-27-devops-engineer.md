# DevOps engineer, 2026-10-27

## Explain the Canvas portal CI workflow (PR #87)

- The Team Lead asked on release PR #76 for a comment saying what
  `.github/workflows/canvas-portal-ci.yml` is for.
- Added a header comment: what the backend and frontend jobs check, when
  the workflow runs (PRs and pushes to `main` and `develop`, only for
  `canvas-portal/**` or the workflow itself), and that it deploys nothing
  and uses no secrets.
- No behavior change: comments only, so no decision needed.

## Peer review of the CI workflow comment (PR #87)

- Fresh DevOps engineer thread, reviewing as peer against `develop@f2354de`.
- Checked that only comments changed (old and new workflow parse to the
  same YAML) and that each line of the header comment matches the jobs,
  triggers, and `paths` filters. Both CI jobs passed on the PR.
- Verdict: Recommend with notes. One optional wording note (F-1): say the
  automatic GitHub token is read-only because of `permissions: contents: read`.
- F-1 was fixed in `a743058` by the owner (comment only). Re-checked the
  fix: verdict now Recommend.

## Peer review of the new-project setup guide (PR #92)

- Fresh DevOps engineer thread, reviewing `d3986f8` (the version refocused
  on setup done outside the repo) against `develop@b94c197`.
- Checked the guide's GitHub steps against the live repo with `gh api`:
  default branch `develop`, the `protected` ruleset on `main` (deletion,
  non-fast-forward, pull request, no bypass), and the merge settings all
  match. No required status checks, so CI needs no web setup.
- Could not read Pages or environment settings (the proxy blocks them).
  No Pages deploy has run from `main` since `develop` became the default.
- Verdict: Changes needed, for one missing step: allow `main` in the
  `github-pages` environment's deployment branches (F-1). Three minor
  findings on branch order, the clone folders, and workflows.
- Told the Team Lead about three live-repo gaps outside the PR: no
  `decision` label, grey persona labels with no description, and a
  disabled `develop` ruleset left over.
- F-1 to F-4 fixed in `f1be7de` by the owner. Re-checked the fixes:
  verdict now Recommend.

## PR template line and review for the ripple check (PR #112)

- Carries out the Team Lead's answer on #96 in the file the DevOps
  engineer owns: added *Files that state this rule* under *Summary* in
  `.github/pull_request_template.md`. It asks the author to list every
  file that states a changed process rule, including ones that needed no
  change, or write "None: no process rule changes". Left blank on
  purpose, so a rule-changing PR can't pass with a default "None".
- The template's link uses `../blob/develop/...`, as CLAUDE.md says for
  the PR template.
- Reviewed the whole PR against `develop@94262eb`. Docs only: `ci-paths`
  says no workflow runs. Verdict below, posted on the PR.
- No new decision: this carries out #96.

## Breach rule link and review (PR #113, #97 PR 1)

- Carries out the Team Lead's #97 decision in the file the DevOps
  engineer owns: *Does not decide* in the DevOps engineer persona now links
  "potential data breach" to its one home in the cybersecurity engineer
  persona. Nothing else in the file restated the rule.
- Reviewed the whole PR against `develop@c2a78b5`. Docs only: `ci-paths`
  says no workflow runs. Found one more file that restates the rule,
  outside the PR's ripple check scope: the roadmap's risk list and
  backlog (X-1). Verdict posted on the PR.
- No new decision: this carries out #97.

## Docs check in CI (#100)

- Carries out the Team Lead's answer on
  [#100](https://github.com/bbranton/TestProj/issues/100): added
  `.github/workflows/docs-check.yml`, which runs
  `team/Development/scripts/docs_check.py` on every PR and on pushes to
  `main` and `develop`.
- The script checks every tracked `.md` file: repo links written from the
  root, relative, or as the PR template's `../blob/develop/...` form must
  name a file that exists, and a `#fragment` must match a heading. Every
  FR and NFR ID in `docs/canvas-portal/` outside a change log must be
  defined in `02-requirements.md`. Standard library only, no secrets.
- No paths filter, since renaming or deleting any file can break a link.
- Starts green on `develop`: 49 files, 0 problems. A test copy with a
  missing file, a missing heading, and an undefined ID failed with all
  three.
- Updated the files that said docs PRs run no checks: DevOps notes (and
  Open items), the DevOps persona's *Owns*, and the `ci-paths` skill.
- Not done: making the check required before merge. That is a repo
  setting, and a change to which checks must pass, so it needs the Team
  Lead.

### Decision: add a docs check to CI for links and requirement IDs

- **Date:** 2026-10-27
- **Decided by:** Team Lead
- **Options:** 1, add `docs-check.yml` backed by a script in
  `team/Development/scripts/`; 2, no change, reviewers keep checking links
  by hand
- **Recommendation:** 1: it costs $0, needs no secrets, and replaces
  manual link checks on every docs PR
- **Outcome:** 1, as recommended
- **Links:** [#100](https://github.com/bbranton/TestProj/issues/100),
  [process retro](/team/retros/2026-10-27-process.md)
