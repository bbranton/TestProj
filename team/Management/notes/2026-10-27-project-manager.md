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
