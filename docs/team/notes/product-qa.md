# Product and QA notes

Lasting lessons for the Product and QA persona. See the
[team workspace](../workspace.md#persona-notes) for how notes work.

- Run `trace-requirement --untested <phase>` before calling a phase's test
  plan complete. It also catches IDs that a range like "FR-10 to FR-14"
  already covers.
- A finding that needs a change in another doc gets an `X-` ID and is fixed
  in that doc's PR, as in the canvas portal docs review.
- Keyboard actions are not a requirement (NFR-31 was removed). Tests and
  specs shouldn't use shortcuts like Ctrl+Enter.
- Mark each test step with the phase it needs. A step that uses a later phase's
  feature (notes, the Archived view) blocks an earlier phase's exit criteria.
