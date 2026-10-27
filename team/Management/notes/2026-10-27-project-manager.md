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

## Review the "each persona fixes its own files" wording (#86)

- Reviewed #86 as the peer and the shared-files reviewer. It removes the
  last "only the owner fixes" wording, matching *Who fixes a finding* and
  *Fixes by another persona* from #80.
- Findings: the new rule 3 says "No one edits another persona's files",
  which is broader than before and would rule out team threads such as
  #83's and #85's, which edited every persona's files under the Team
  Lead's decisions; "No persona" keeps the old scope. And step 4's "minor
  findings the owner may fix later" still names the owner as the fixer.
- No new decision: #86 carries out #80.

## Review "ask per finding: issue or backlog" (#88)

- Reviewed #88 as the peer and area reviewer for the shared files, the
  roadmap, and the glossary. The direction matches the Team Lead's pick.
- Findings: a potential data breach must stay out of the issue-or-backlog
  choice, and the cybersecurity engineer's persona file and notes still
  say follow-ups never become issues; "Waiting on the Team Lead" clashes
  with "a PR that needs a new decision stops"; the new-name `persona:`
  labels don't exist yet; the workspace still lists "backlog items" in
  the PR template; and the protocol doesn't say where the per-finding
  requests go.
- Updated the backlog lesson in the notes to the new rule.
- No new decision: #88 carries out the Team Lead's "Ask per finding,
  issue or backlog" pick.

## Review the four options for deferred findings (#89)

- Reviewed #89 as the peer and area reviewer for the shared files and the
  roadmap. The four options match the Team Lead's comment on #76.
- Findings: fixing a later-phase finding now grows the current phase, so
  it falls under the phase scope budget and R-10; option 1 only works if
  the PR waits for the answer; and the cybersecurity engineer's persona
  file still names only an issue or the backlog for deferred security
  findings.
- Committed to the PR branch: the phase scope budget in this persona file
  now covers later-phase findings fixed now, and the backlog lesson in the
  notes lists the four options.
- No new decision: #89 carries out the Team Lead's comment.

## Review #89's follow-up notes (#90)

- Reviewed the protocol line that logs later-phase "fix now" picks under
  the phase scope budget (8c40f11). It matches this persona's budget,
  except the budget also allows the Team Lead's OK to let the phase grow
  instead of naming a cut; noted as a minor finding.
- No new decision.

## Review UI layout changes going to the Team Lead (#91)

- Reviewed the review protocol's change for #91: layout changes join new
  screens and main-flow changes as Team Lead decisions; the UI/UX
  designer still decides wording and accessibility alone.
- Findings: the architect's persona still says the UI/UX designer "makes
  the call" on how a screen looks, and "a layout change" has no line
  between a change that needs the Team Lead and a detail inside the spec.
- Updated this persona's *Does not decide* line for the UI/UX designer to
  say layout changes still need the Team Lead.
- No new decision: #91 carries out the Team Lead's comment on #76.
- Part 2 of #91 (8c85f7d) moves the screenshot rule from CLAUDE.md to the
  UI/UX designer's persona file, from the Team Lead's comment on #76.
  Links resolve, and the PR template still reaches every PR. Notes: the
  PR bundles two jobs on one branch, so part 2 waits on part 1's open
  decision; a Developer thread opening a UI PR only meets the rule
  through the template.

## Review the new-project setup guide (#92)

- Reviewed #92 as Management: Changes needed. Read `d3986f8`, the version
  refocused on setup done outside the repo, against `develop@b94c197`.
- Two major findings in its copy step: starting every notes file empty
  drops the security register, and the roadmap's decision register,
  risks, backlog, and change log (plus the glossary) aren't in the copy
  list, though the review protocol and persona files link to them.
- One minor note for the DevOps engineer peer: the merge settings step
  restates the DevOps engineer notes.
- The owner fixed all three in `da26f94`; re-checked at `868dbe9` and
  changed the verdict to Recommend.
- No decision was raised.

## Review the retro skill (#94)

- Reviewed #94 as the peer and shared-files reviewer against
  `develop@d3df9bf`: Recommend with notes. The skill matches the plan the
  Team Lead approved in the project chat on 2026-10-27.
- Notes for the owner: say where each suggestion's decision request goes,
  keep tokens and student data out of feedback and notes, and give the
  Team Lead a rough cost per retro.
- Fixed in this persona's files: the team README's stale *Team process*
  row link and its list of shared `team/` contents, and a *Retros* line in
  this persona's *How it works*.
- The owner fixed F-1 to F-3 in `d044ac7` and `a1795b4`; re-checked and
  changed the verdict to Recommend.
- No new decision: #94 carries out the Team Lead's approval.

## Combine the docs retro (#109)

- Combined the nine personas' docs retro feedback into
  [the 2026-10-27 docs retro note](/team/retros/2026-10-27-docs.md). The
  process retro ran the same day, so this one saved under
  `2026-10-27-docs` and the other under `2026-10-27-process`.
- Main themes: requirements moved while the downstream docs were
  reviewed, and the design, UI spec, and test plan merged with no
  reviewers.
- Raised six decision requests, #101 and #103 to #107, one per
  suggestion.

### Decision: how to raise the docs retro's suggestions

- **Date:** 2026-10-27
- **Decided by:** Project manager
- **Options:** one issue per persona's suggestion (nine), or merge the
  ones that ask for the same change
- **Recommendation:** merge: the requirements engineer's, UI/UX
  designer's, and CFO's ordering and freeze ideas became S-1, and the
  test engineer's, developer's, and architect's review ideas became S-2,
  so the Team Lead answers six questions instead of nine. The CFO's
  fresh-thread and cost-row points went to the process retro.
- **Links:** #101, #103, #104, #105, #106, #107

## Peer review of the docs retro note (#109)

- Checked the note against all nine feedback files and decision issues
  #101 and #103 to #107. Every suggestion maps to one issue; the CFO's
  fresh-thread and cost-row points are in the process retro (#102).
- Fixed three attribution and evidence gaps in the note: the developer
  didn't raise the scope churn theme, the UI/UX designer raised the gaps
  that reached the Team Lead, and the open potential data breaches #25
  and #26 now show in the security theme.
- Left for the owner: S-2 and #103 drop the UI spec from the developer's
  ask and name no UI spec reviewer. Verdict Recommend with notes.

## Combine the process retro (team/retros/2026-10-27-process.md)

- Combined all nine personas' process feedback into
  [the retro note](/team/retros/2026-10-27-process.md), following the
  `retro` skill. Used the retro date `2026-10-27-process` so it doesn't
  collide with the docs retro run the same day.
- First retro, so nothing earlier to check.
- Raised seven decision requests, all recommended: #95 fresh thread per
  PR, #96 ripple check on rule changes, #97 one place for the potential
  data breach rule, #98 batch process changes during Phase 1, #99 notify
  for wording-only persona changes, #100 docs check in CI, #102 daily CFO
  batch thread.
- No decision was made here: each waits on the Team Lead.

## Review the process retro note (#108)

- Peer review of `team/retros/2026-10-27-process.md` against the `retro`
  skill and all nine feedback files: **Changes needed**.
- All seven suggestions map one to one to decision requests #95 to #100
  and #102, each with a recommendation and the files it changes. #101 is
  the docs retro's S-1.
- F-1 to F-4 are attribution and coverage fixes: process churn was raised
  by eight personas, not nine (the DevOps engineer didn't); the
  cybersecurity engineer's counterpoint that one reused thread stayed
  cheap for small reviews; the architect's fixes were on #88, #89, and
  #91; and two missing points (the cost log for planning, the UI/UX
  designer's #54 self-review). F-5, an unlinked claim, is optional.
- Lesson: when combining feedback, check each "raised by" list against
  the files, one persona at a time, rather than from memory of the
  themes.
- The owner fixed F-1 to F-5 in `ab79936`; re-checked at `33a3f79` and
  changed the verdict to Recommend.
- No new decision: the retro's decisions wait on the Team Lead.

## Carry out #95: one thread per PR

- Added *One thread per PR* to `team/workspace.md` and a pointer in
  `CLAUDE.md`. The architect's "one long-running architect thread" line
  goes in the architect's own PR.

### Decision: fresh thread per PR, with a $10 hand-off check

- **Date:** 2026-10-27
- **Decided by:** Team Lead
- **Options:** fresh thread per PR plus a hard hand-off cap (about four
  Team Lead rounds or $10); fresh thread per PR only; no change.
- **Recommendation:** the hard cap, to stop long threads driving the bill.
- **Outcome:** fresh thread per PR with no hard cap. Instead, an owner
  thread past about $10 asks the Team Lead whether now is a good time to
  hand off, and writes a hand-off note if so.
- **Links:** [#95](https://github.com/bbranton/TestProj/issues/95),
  [process retro](/team/retros/2026-10-27-process.md)

## Carry out #96: ripple check for process rules

- Added *Ripple check for process rules* to `team/review-protocol.md`
  (rule 8 and step 1 of *How a review runs*), a step for the owner and
  reviewer in the `cross-review` skill, the Ripple check term in the
  glossary's team process terms, and a pointer in `CLAUDE.md`. The DevOps
  engineer adds the *Files that state this rule* line to the PR template.
- Ran the ripple check on this rule itself: the files above are every
  place that states the PR author's steps.

### Decision: a PR that changes a process rule fixes every copy

- **Date:** 2026-10-27
- **Decided by:** Team Lead
- **Options:** ripple check in the PR (owner finds and fixes every file
  that states the rule, and lists them); list only, with reviewers
  checking; no change.
- **Recommendation:** the ripple check in the PR, the process version of
  a requirement's impact note, to stop follow-up PRs for stale wording.
- **Outcome:** as recommended.
- **Links:** [#96](https://github.com/bbranton/TestProj/issues/96),
  [process retro](/team/retros/2026-10-27-process.md),
  [ripple check](/team/review-protocol.md#ripple-check-for-process-rules)

## Review the ripple check PR (#112)

- Peer review of the ripple check for #96 at `0aef974`, against
  `develop@94262eb`: **Recommend with notes**.
- The rule's text is sound and matches the Team Lead's answer. Re-ran the
  ripple check on the rule: no other file in `team/`, `.claude/skills/`,
  `CLAUDE.md`, the PR template, or the glossary restates the owner's
  steps. The DevOps engineer's template heading matches step 3 word for
  word, and the branch merges cleanly with `develop`.
- F-1 (minor): *Based on* in the PR description still says `8faa950`;
  the branch now has `develop@94262eb`.
- N-1 (optional): the project manager's "Ripple list for each decision"
  covers phase and scope decisions, close in name to the new ripple check.
  No change needed now.
- No new decision: #96 is already answered.

## Link the project manager's files to the breach rule (#113)

- On the cybersecurity engineer's PR #113 (#97, PR 1 of 5), changed the
  project manager's files to link to
  [Potential data breach](/team/QA/personas/cybersecurity-engineer.md#potential-data-breach)
  instead of restating it: the review protocol (*Who decides what*,
  *Findings table*, *Follow-up work*), the team README (*Security is
  everyone's job*), the project manager persona (*Owns*, *Decisions*), the
  project manager notes, and the `cross-review` skill's reviewer step 3.
  Kept "Delaying the fix of a potential data breach" under *Needs the Team
  Lead*, since it names a Team Lead call rather than restating the rule.
- Wording follows the cybersecurity engineer's proposed text on the PR.
- No new decision: the Team Lead answered it on #97.

## Review the breach rule's one home (#113)

- Shared-files review at `9c7b18a`, against `develop@c2a78b5`:
  **Recommend with notes**.
- Re-ran the ripple check on the branch: outside the home and the
  security register intro, every mention links to
  *Potential data breach* or only names the term.
- F-1 (minor): the PR description still lists the other owners' changes
  as still to come.
- N-1 (optional): the glossary repeats the home's "what counts" sentence.
- X-1 (DevOps engineer): the roadmap still restated the rule in the risk
  list intro and the backlog intro. Both now link to the home, and the
  step 6 gate list links the term too. My ripple check had skipped
  `docs/`, since the ripple check's search list names only the glossary
  there.

## Notify, not review, for wording-only persona file changes (#99)

- Added *Wording-only changes notify the persona* to the review
  protocol's *Who reviews what*, as the rule's one home per #97, and
  linked to it from *Two levels of review*, the two *Who reviews what*
  rows for another persona's files, the team README's *Folders*, and the
  workspace's *Team folders* and board rule 4.
- From the peer review: the team README's step 1 for a persona thread now
  checks the board for `[note]` lines addressed to it, so a notified
  persona sees the change, and notified personas go under *Persona
  review* in the PR description, so the PR template needn't change.
- Ripple check: `CLAUDE.md`, the PR template, and the `cross-review` skill
  send readers to the review protocol's *Who reviews what* for reviewers,
  where the exception now lives, so they needed no change. No glossary
  term covers it.

### Decision: notify, not review, for wording-only persona file changes

- **Date:** 2026-10-27
- **Decided by:** Team Lead
- **Options:** 1, notify the persona with a board `[note]`, keeping the
  security "always" rule; 2, no change, every persona whose file changes
  reviews
- **Recommendation:** 1, with the PR's peer reviewer judging whether a
  change is wording-only, and the persona reviewing if in doubt
- **Outcome:** 1, as recommended
- **Links:** [#99](https://github.com/bbranton/TestProj/issues/99),
  [process retro](/team/retros/2026-10-27-process.md),
  [Wording-only changes](/team/review-protocol.md#wording-only-changes-notify-the-persona)

## Peer review of PR #114 (#99)

- Peer review at `0facf70`, against `develop@c2a78b5`: **Changes needed**.
- F-1: the workspace's *Team folders* still stated the old rule and was
  missing from *Files that state this rule*. F-2: nothing told a persona
  thread to read board `[note]` lines left for it. F-3: the *Who reviews
  what* rows for another persona's files didn't point to the exception,
  though the `cross-review` skill sends owners to the table. F-4
  (optional): say where notified personas go in the PR description.
- All four are in the project manager's own files; no other reviewer
  needed. Fixed in `84d9890` and the next commit.
- No new decision: #99 is already answered.

## Link the workspace to the CFO's daily batch thread (#102)

- On the CFO's PR #116, added one line to the workspace's *One thread per
  PR*, after "Only the coordinator starts threads.": it links to the CFO
  persona's
  [Daily batch thread](/team/Management/personas/cfo.md#daily-batch-thread)
  and doesn't restate the rule, per #97.
- Left the hunks PR #114 changes (*Team folders*, board rule 4) alone.
- No new decision: the Team Lead answered it on #102.

## Review the CFO's daily batch thread (#116)

- Shared-files review: **Recommend**. Ripple check found no other file
  that gives the batch's timing; the rest say "in batches" or link to the
  CFO persona.

## Give the review protocol, workspace, and README rules one home (#97, PR 2)

- Carried out PR 2 of the #97 rollout from `develop@7cb311b`.
- Review protocol: added *A rule is stated only in its home* and the list
  of rule homes to the *Ripple check*, and step 2 now replaces a copy
  with a link. *Who reviews what* is the one home of the peer reviewer
  rule; *Two levels of review* links to it instead of restating it. The
  release PR, security weight, thread starting, and close-out lines link
  to CLAUDE.md, the team README, and the workspace.
- Workspace and team README: review routing, the cost log, and the Team
  Lead's say now link to their homes.
- Cost log: the project manager persona's *Cost plans* no longer says the
  CFO "owns the log"; it links to the CFO persona's *Role*, which gives
  the merge-conflict reason from #72.
- Left for later PRs in the series: the other persona files (PR 3), the
  glossary, skills, and PR template (PR 4), and CLAUDE.md (PR 5). The
  roadmap's stakeholder row restates the Team Lead's say; noted for PR 5.
  Searching `docs/canvas-portal/` in the ripple check waits on the Team
  Lead's answer.
- Reviews: cybersecurity engineer Recommend; CFO Recommend with notes
  (F-1 fixed in `fef0b0d`); project manager peer Recommend with notes.
  Peer F-1 to F-3 fixed: *The rules in short* links to Branches for the
  release PR, the intro credits CLAUDE.md only with the final say, and
  *Who decides what* says it is a summary of the persona files'
  *Decisions*. For PR 5: CLAUDE.md *Branches* should say the Team Lead is
  the release PR's only reviewer, and *Team personas* still restates the
  security weight.
- No new decision: #97 is already answered and logged in #113.

## Link persona files to rule homes (#97, PR 3)

- Carried out PR 3 of the #97 rollout from `develop@c5aac0e`, as the
  project manager owner thread.
- In all seven persona files that had it, the security line in
  *Decisions* and the review checklist now links to
  [Security is everyone's job](/team/README.md#security-is-everyones-job)
  instead of restating the cybersecurity engineer's weight and "raise it
  yourself". The cybersecurity engineer persona's *Role* and *Decides* link
  there too.
- The requirements engineer, test engineer, architect, and project manager
  link to [Who fixes a finding](/team/review-protocol.md#who-fixes-a-finding)
  instead of restating how a fix in another persona's PR goes.
- Also relinked: the developer's release PR line to Branches, the
  project manager's and architect's UI deferral to the UI/UX designer's
  *Decisions*, the DevOps engineer's screenshot helper to the screenshot
  rule, and the project manager's phase line, backlog, and reviewer lines
  to CLAUDE.md and the review protocol. The CFO persona needed no change.
- Other personas' files changed only in links and wording, so they get a
  board `[note]` under #99, except the cybersecurity engineer, which
  reviews because the PR touches *Security is everyone's job*.
- Left for PR 4 and PR 5: the glossary's Team Lead row, CLAUDE.md's
  *Team personas* and *Branches*, and the roadmap's stakeholder row still
  restate the security weight, the reviewer say, or the release PR.
- No new decision: #97 is already answered and logged in #113.
- Reviews: cybersecurity engineer Recommend. Project manager peer
  Changes needed, both fixed: F-1, the test engineer's security line read
  as deferring untested risks, so it again says the test engineer still
  raises them; F-2, the project manager's checklist no longer lists part
  of the cybersecurity engineer's triggers and points to its row instead.
## Carry out #98: process ideas wait for retros

### Decision: process changes wait for retros, and ideas go in a shared ideas file

- **Date:** 2026-10-27
- **Decided by:** Team Lead
- **Options:** a weekly batched process PR (the retro's suggestion); an
  `[idea]` note type on the board; a separate ideas file in the project's
  shared files; not tracking ideas between retros.
- **Recommendation:** after the Team Lead explained that the run of
  process PRs was a deliberate pause to fix the process, no weekly batch,
  and a separate ideas file, since the board is busy with claims and cost
  notes and the file needs no PR per idea.
- **Outcome:** no weekly batch: process improvements wait for periodic
  retros. Ideas go in `/mnt/project-files/retros/process-ideas.md`.
- **Links:** [#98](https://github.com/bbranton/TestProj/issues/98),
  [team workspace](/team/workspace.md#process-ideas).

- Added *Process ideas* to the team workspace, pointed the `retro` skill
  at the file, and created the file in the shared files.
