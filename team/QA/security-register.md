# Security register

Owned by the cybersecurity engineer. It stays in the repo, unlike the
persona notes, so every change has history and review
([#127](https://github.com/bbranton/TestProj/issues/127)).

## Current threat picture

Update this when hosting, the repo, or where real tokens live changes.

- The repo is public. Workflow artifacts and logs can be downloaded by any
  GitHub user.
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
| #26 Deploy secrets and backups private on a public repo | Yes | DevOps engineer | Phase 1 step 6 | Open |
| #17 Incident plan | No | Cybersecurity engineer | Phase 1 step 6 | Open |
| #19 Key and session secret storage and rotation | No | DevOps engineer | Phase 1 step 6 | Open |
| #20 Secret scanning and dependency alerts | No | DevOps engineer | Phase 1 step 6 | Open |
| #46 Team Lead decisions on token storage and sending | No | Architect (cybersecurity engineer briefs) | Phase 1 step 2 | Open |
| #18 Output escaping and a Content-Security-Policy | No | Architect | Proposed: Phase 1 step 6 | Open |
| #22 Tests for reused session cookies and HTML in Canvas text | No | Test engineer | Proposed: Phase 1 exit | Open |
| #21 Token expiry and deleting the token in Canvas | No | Requirements engineer | Proposed: Phase 1 step 6 | Open |
| #16 Client security document | No | Cybersecurity engineer | Anyone but the Team Lead connects | Open |
