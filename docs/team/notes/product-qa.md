# Product and QA notes

Lasting lessons for the Product and QA persona. See the
[team workspace](../workspace.md#persona-notes) for how notes work.

- Define a term once, in the [glossary](../../canvas-portal/glossary.md),
  and link to it. The README once held the web terms, and the Team Lead
  moved them out: a README describes its folder, not the product.
- Run `trace-requirement --untested <phase>` before calling a phase's test
  plan complete. It also catches IDs that a range like "FR-10 to FR-14"
  already covers.
- A finding that needs a change in another doc gets an `X-` ID and is fixed
  in that doc's PR, as in the canvas portal docs review.
- Keyboard actions are not a requirement (NFR-31 was removed). Tests and
  specs shouldn't use shortcuts like Ctrl+Enter.
- Mark each test step with the phase it needs. A step that uses a later phase's
  feature (notes, the Archived view) blocks an earlier phase's exit criteria.
- When a requirement's *Phase* column changes, update *Requirements by phase*
  and *Requirements by goal* in the same PR. A split phase such as
  "1, 2 (dropping)" is listed under each phase, with the part in parentheses.
- A requirement says the need, not the look. FR-65's "colored label strip"
  and "grayed out" made color the only signal and tied one look to three
  meanings (UI/UX F-3 on #6).
- Check each security NFR's phase against the roadmap's deploy step. HTTPS
  was set to Phase 4 while the internet-facing test deploy was in Phase 1
  (Management M-1 on #6).
- Phase moves rippled into four docs each time (FR-45 went 3, 2, 1; FR-78
  went 1, 2, 1). Write the impact note before asking, not after.
