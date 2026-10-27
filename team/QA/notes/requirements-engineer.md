# Requirements engineer notes

Lasting lessons for the requirements engineer persona. See the
[team workspace](/team/workspace.md#persona-notes) for how notes work.

- Define a term once, in the [glossary](/docs/canvas-portal/glossary.md),
  and link to it. The README once held the web terms, and the Team Lead
  moved them out: a README describes its folder, not the product.
- A finding that needs a change in another doc gets an `X-` ID and is fixed
  in that doc's PR, as in the canvas portal docs review.
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
- Keyboard actions are not a requirement (NFR-31 was removed).
- A glossary meaning says what a term is, and links the rule for the
  details. Listing a rule's steps in the glossary makes one more copy to
  keep in step (Ripple check on #112).
- A ripple check covers every folder that might state the rule, `docs/`
  included. PR #113's check skipped the roadmap, which still restated the
  breach rule (DevOps X-1 on #113).
