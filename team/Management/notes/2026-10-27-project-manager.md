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

## Review the follow-up rule change (#80)

- Reviewed #80 as Management: Changes needed, then Recommend after the
  fixes in `1ac4e08`. Read from `develop@d5d0539`.
- Found a potential data breach too big for its PR had nowhere to be
  tracked (now the security register, which Management checks at every
  phase boundary and before every deploy), current-phase backlog items
  waited for the phase boundary (now in the next decision batch), and the
  persona's "Fix the roadmap on its own PR" contradicted the new rule.
- Raised a decision request to the Team Lead on what happens to the 23
  issues still open from the old rule, including `potential-breach` #25
  and #26. It doesn't block #80.
- #80's owner is a team thread with no persona log, so the decision is
  recorded here, committed to the PR branch as *Fixes by another persona*
  says.

### Decision: Review follow-ups are fixed in the same PR or go on the roadmap backlog, not GitHub issues

- **Date:** 2026-10-27
- **Decided by:** Team Lead
- **Options:** keep opening a GitHub issue for each follow-up (the old
  rule); fix each finding in the same PR, committed by the persona that
  owns the file, and put only work outside the current phase or too big
  for the PR on a roadmap backlog Management keeps
- **Recommendation:** the Team Lead's own proposal, since follow-up issues
  left too many loose ends
- **Outcome:** as proposed. Other personas may commit their own files to
  a PR's branch. A potential data breach never goes on the backlog: it is
  fixed in the PR, or, when Security agrees it is too big, tracked in the
  security register and fixed first in the current phase, before the next
  deploy.
- **Links:** #80, #76 (Team Lead's comment), `team/review-protocol.md#who-fixes-a-finding`,
  `docs/canvas-portal/01-roadmap.md#9-backlog`

## Review the peer reviewer rule change (#82)

- Reviewed #82 as Management, both as its peer (Management owns most of
  the changed files) and as area reviewer. Read from `develop@b2b23fd`.
- Checked it against the Team Lead's comment on #76: at least one
  reviewer on every PR, a same-persona peer by default, as a precaution.
- Found the glossary's *Reviewers* entry still says one reviewer per area
  touched, which leaves none for an own-area PR. The glossary is the
  Requirements engineer's, so it commits the fix to the PR.
- Notes for the owner: say who the peer is when the owner is a team
  thread in `CLAUDE.md`, the skill, and the PR template; the owner's own
  pushes after the last verdict (the Close out log entry, merging
  `develop`) still go in without a peer look; and each own-area PR now
  costs one more thread.
- #82's owner is a team thread with no persona log, so the decision is
  recorded here, committed to the PR branch as *Fixes by another persona*
  says.

### Decision: Every PR has at least one reviewer, a same-persona peer by default

- **Date:** 2026-10-27
- **Decided by:** Team Lead
- **Options:** no reviewers when a PR touches only the owner persona's
  area (the rule from #79); always at least one reviewer, a fresh thread
  of the owner's own persona as a peer
- **Recommendation:** the Team Lead's own proposal, as a precaution
- **Outcome:** as proposed. Area reviewers and the "always" rules apply on
  top. When the owner is a team thread, the peer is the persona that owns
  most of the changed files. "Every push" is read as every PR into
  `develop`, with reviewers re-checking fixes.
- **Links:** #82, #76 (Team Lead's comment), `team/review-protocol.md#who-reviews-what`

## Review the job-title rename (#83)

- Reviewed #83 as the peer and the shared-files reviewer. The rename is
  complete in the persona files, team rules, and Canvas portal docs;
  findings were a missed rename in the cost log's intro and one in the
  security register, the `persona:` issue labels, and mixed capitals for
  persona names mid-sentence.
- Fixed the capitals in this persona's *Does not decide* list, and added
  the rename lesson to the notes.
- #83's owner is a team thread with no persona log, so the decision is
  recorded here.

### Decision: Personas are named by job title

- **Date:** 2026-10-27
- **Decided by:** Team Lead
- **Options:** keep the area names (Management, Architecture, UI/UX,
  DevOps, Security); name personas by job title
- **Recommendation:** none asked; the Team Lead's own comment
- **Outcome:** Project manager, Architect, UI/UX designer, DevOps engineer,
  and Cybersecurity engineer. Management, QA, and Development stay as team
  names. History (change logs, daily logs, old finding IDs) is not renamed.
- **Links:** #83, #76 (Team Lead's comment)

## Old follow-up issues after #80 (#84)

- Raised the X-1 decision request from the #80 review: what happens to the
  23 open issues, most of them opened under the old follow-up rule. The
  Team Lead chose to leave them open. The `decision` issue (#46) and the
  test-plan issues among them were never follow-ups and stay as they are.

### Decision: Issues opened under the old follow-up rule stay open until done

- **Date:** 2026-10-27
- **Decided by:** Team Lead
- **Options:** move each old follow-up issue to the roadmap backlog (#25
  and #26 to the Risks list) and close it with a link; leave them open and
  work them as before, with only new follow-ups on the backlog
- **Recommendation:** move them, so there's one tracker
- **Outcome:** leave them open until done. Only new review follow-ups use
  the roadmap backlog. `decision` and test-plan issues were never in
  question.
- **Links:** #80, #84, `docs/canvas-portal/01-roadmap.md#9-backlog`

## Review the root-path links (#85)

- Reviewed #85 as the peer and the shared-files reviewer. A script
  checked every Markdown link in the repo: none is broken, every section
  anchor exists, and the only relative link left is the PR template's
  named exception. The diff changes link targets only.
- Findings were wording in the new *Links* rule: say a leading `/` means
  the repo root, not the computer's, since agents open these paths with
  file tools, and don't state the untested Obsidian behavior as fact.
- No new decision: #85 carries out the Team Lead's "Switch all links now"
  pick on #76.
