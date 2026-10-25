# Architecture notes

Lasting lessons for the Architecture persona. See the
[team workspace](../workspace.md#persona-notes) for how notes work.

- Build only what the *Design by phase* table lists for the current phase,
  even when later sections already describe more.
- The Canvas API is read-only (NFR-13, C-3). A query-only `POST`, such as
  GraphQL, needs the Team Lead's call first.
