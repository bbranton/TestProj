# 2026-10-27 · Management (project manager)

## Rewrite the review protocol (#71)

- Rewrote `team/review-protocol.md` around seven rules from the Team Lead's
  discussion with the coordinator.
- Fixed the conflicts in the team folder scan so CLAUDE.md, the team README
  and workspace, persona files, the cross-review skill, the PR template,
  the glossary, and roadmap section 8 agree with it.

### Decision: PR authors pick reviewers, and personas merge their own PRs into develop

- **Date:** 2026-10-27
- **Decided by:** Team Lead
- **Options:** Team Lead confirms every PR's reviewers; one reviewer per PR
  picked for the biggest risk; the author picks a reviewer for each area
  the PR touches
- **Recommendation:** one reviewer per PR, to cut review cost
- **Outcome:** the author picks a reviewer for each area the PR touches
  (UI → UI/UX, tokens, secrets, hosting, or deploys → Security), reviews are
  quick, and the author fixes right away. The Team Lead only reviews and
  merges the `develop` → `main` release.
- **Links:** #71, `team/review-protocol.md`

### Decision: Small, focused PRs instead of one open PR per persona

- **Date:** 2026-10-27
- **Decided by:** Team Lead
- **Options:** a hard limit of one open PR per persona; related changes on
  the open PR, unrelated ones in a new small PR
- **Recommendation:** drop the hard limit, since PRs now merge into
  `develop` quickly
- **Outcome:** as recommended; smaller, focused PRs are preferred over
  sprawling ones
- **Links:** #71, `team/review-protocol.md#small-focused-prs`

### Decision: The Team Lead decides through decision requests, not PR approvals

- **Date:** 2026-10-27
- **Decided by:** Team Lead
- **Options:** decide by approving each PR (the old scheme); let owners
  decide anything no other doc depends on; send every real decision to the
  Team Lead as an explicit decision request, separate from merging
- **Recommendation:** separate deciding from merging
- **Outcome:** as recommended. Decision requests go in Management's
  register or a `decision` issue, answered in batches. PRs only carry out
  decisions already made, so owners merge into `develop` themselves. The
  coordinator tells the Team Lead in real time when a PR merges or a
  request is raised.
- **Links:** #71, `team/review-protocol.md#decisions-are-separate-from-merging`

## Relabel the old Product and QA issues

- Moved the 9 open issues labeled `persona: product-qa` to the split
  personas. Requirements engineer: #13, #21, #48, #49, #50. Test engineer:
  #14, #22, #37, #51. Each got a triage comment naming its owner.
- Created `persona: requirements-engineer` and `persona: test-engineer`.
  Left priorities, phases, `backlog`, and `needs-triage` unchanged.
- None was ambiguous: each one changes either `02-requirements.md` or
  `05-test-plan.md`.

## Review the release PR rule change (#77)

- Reviewed #77 as Management: Recommend with notes. Only `CLAUDE.md` and
  `team/review-protocol.md` changed, and every other doc that states the
  rule already agreed with it.
- Two minor notes for the owner: "when asked" narrows the decision, and
  `CLAUDE.md` still speaks of requesting the Team Lead's review on the
  release PR, which GitHub can't do when the PR is opened through their
  account.
- #77's owner is a team thread with no persona log, so the decision is
  recorded here.

### Decision: Any persona may open the develop → main release PR

- **Date:** 2026-10-27
- **Decided by:** Team Lead
- **Options:** only the Team Lead opens and merges the release PR (the old
  rule); any persona may open it, and only the Team Lead merges it
- **Recommendation:** let personas open it, since a persona thread had just
  opened #76 at the Team Lead's request
- **Outcome:** as recommended. The opener assigns the Team Lead and
  summarizes what changed since `main`; no persona approves or merges into
  `main`.
- **Links:** #76, #77, `team/review-protocol.md#two-levels-of-review`
