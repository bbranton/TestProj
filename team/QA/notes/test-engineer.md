# Test engineer notes

Lasting lessons for the test engineer persona. See the
[team workspace](../../workspace.md#persona-notes) for how notes work.

- Run `trace-requirement --untested <phase>` before calling a phase's test
  plan complete. It also catches IDs that a range like "FR-10 to FR-14"
  already covers.
- Keyboard actions are not a requirement (NFR-31 was removed). Tests
  shouldn't use shortcuts like Ctrl+Enter.
- Mark each test step with the phase it needs. A step that uses a later phase's
  feature (notes, the Archived view) blocks an earlier phase's exit criteria.
- Check that each security NFR has a test by the phase of the first
  internet-facing deploy. HTTPS was once set to Phase 4 while that deploy
  was in Phase 1 (Management M-1 on #6).
