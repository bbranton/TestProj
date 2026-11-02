# Security register

Owned by the cybersecurity engineer. It stays in the repo, unlike the
persona notes, so every change has history and review
([#127](https://github.com/bbranton/TestProj/issues/127)).

## Current threat picture

Update this when hosting, the repo, or where real tokens live changes.

- The TestProj repo is public. Workflow artifacts and logs can be
  downloaded by any GitHub user.
- The CanSync repo, set up in Phase 0, is private (D-17). On a private
  repository, GitHub enforces branch rules and required checks only on a
  paid plan. Actions environments and their branch limits need Pro,
  Team, or Enterprise, and an environment's required reviewers need
  Enterprise. Push protection needs paid GitHub Secret Protection.
  Whatever the CanSync repo's plan doesn't give is a rule the team
  follows, not a control GitHub enforces, so #20 and #26 below say what
  replaces it.
- From Phase 0's local proof of concept, a real Canvas token sits in a
  git-ignored `.env` on the Team Lead's computer, used by a server on
  `127.0.0.1` only. Keep that `.env` outside any folder a Claude session
  or the Remote Control pull below works in, so the token can't reach a
  transcript, and readable only by the Team Lead's user. If the token is
  ever committed, pasted, or shown, delete it in Canvas at once and make
  a new one (#21); that is the incident plan until #17 is in place.
- Phase 1 step 6 deploys to a free Koyeb app with a Neon free database,
  holding real Canvas tokens. `koyeb.app` isn't on the Public Suffix List.
- Only the Team Lead's own accounts should connect until #16 is published
  and #17 is in place.
- A Remote Control thread on the Team Lead's computer runs `git fetch` and
  `git pull --ff-only` in the local `develop` clone under a standing OK. It
  runs as the Team Lead's own user, so keep secrets and real tokens out of
  that folder, and nothing there should run code it pulls
  ([setup guide](/SETUP-NEW-PROJECT.md#5-set-up-the-local-clone)).

## Open findings

Open security findings and potential data breaches. **Gate** is the phase
step the item must be done before. Clear a row only when it's fixed, and
say where. A **Proposed** gate isn't in the roadmap yet; the project manager
decides it. A potential data breach that isn't fixed in the PR it was
found in is tracked only here, as
[Potential data breach](/team/QA/personas/cybersecurity-engineer.md#potential-data-breach)
says. Any other deferred security finding goes to the Team Lead with the four
options in *Follow-up work*. Unless it's fixed in the PR it was found in,
it gets a row here too, linking its separate fix PR, issue, or `B-` item.

| Item | Potential data breach | Owner | Gate | Status |
|------|-----------------------|-------|------|--------|
| #25 Session cookie and writes on Koyeb's shared domain | Yes | Architect | Phase 1 step 6 | Open |
| #26 Deploy secrets and backups private. On any plan short of Enterprise, the Team Lead decides the [Phase 1](/docs/canvas-portal/01-roadmap.md#phase-1-read-only-viewer-minimum-viable-product) deploy-secrets fallback with the cybersecurity engineer before step 6, such as the host deploying from the CanSync repo with automatic deploys off, the Team Lead starting each deploy, the host's GitHub app able only to read the CanSync repo, and backups made by the host or Neon that still meet Phase 1's 30-day encrypted backup, or the Team Lead accepts less | Yes | DevOps engineer | Phase 1 step 6 | Open |
| #17 Incident plan | No | Cybersecurity engineer | Phase 1 step 6 | Open |
| #19 Key and session secret storage and rotation | No | DevOps engineer | Phase 1 step 6 | Open |
| #20 Secret scanning with push protection, and dependency alerts. If the CanSync repo's plan has no push protection, a CI secret scan runs from Phase 0 (D-17), and before step 6 the Team Lead either pays for push protection (which may need the CanSync repo in an organization on Team) or accepts the CI scan in its place | No | DevOps engineer | Phase 1 step 6 | Open |
| #46 Team Lead decisions on token storage and sending | No | Architect (cybersecurity engineer briefs) | Phase 1 step 2 | Open |
| #18 Output escaping and a Content-Security-Policy | No | Architect | Proposed: Phase 1 step 6 | Open |
| #22 Tests for reused session cookies and HTML in Canvas text | No | Test engineer | Proposed: Phase 1 exit | Open |
| #21 Token expiry and deleting the token in Canvas | No | Requirements engineer | Proposed: Phase 1 step 6 | Open |
| #16 Client security document | No | Cybersecurity engineer | Anyone but the Team Lead connects | Open |
