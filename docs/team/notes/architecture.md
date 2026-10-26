# Architecture notes

Lasting lessons for the Architecture persona. See the
[team workspace](../workspace.md#persona-notes) for how notes work.

- Build only what the *Design by phase* table lists for the current phase,
  even when later sections already describe more.
- The Canvas API is `GET` only (NFR-13, C-3). The Team Lead kept it that way
  for Canvas GraphQL, which reads through `POST` (Q-10): a future idea at most.
- Card status follows FR-23's rules, not Canvas's `workflow_state`, and
  never `has_submitted_submissions`.
- Only a complete Refresh writes cards or the Canvas copy, and no `GET`
  endpoint writes anything. Keeps partial fetches harmless and fits
  `SameSite=Lax` cookies.
- A disconnect empties the token but keeps the `CANVAS_CONNECTION` row,
  since cards, labels, and cache point at it.
