# CFO notes

Lasting lessons for the CFO persona. See the
[team workspace](/team/workspace.md#persona-notes) for how notes work.

- Library files keep no history and the last write wins, so a file every
  thread appends to can silently lose rows (#125). Keep one file per row,
  and keep the logged row files: they are the only backup of the table.
- Some sessions have no `external_metadata.usage`. Log the row with `n/a`
  and say so in the notes, rather than leaving the thread out.
- The hand-off check in [One thread per PR](/team/workspace.md#one-thread-per-pr)
  reads `cost_usd` mid-thread, but on 2026-10-27 this CFO thread's own
  `get_session` had no `usage` at all. Expect the round-count fallback to
  be the common case, and expect `n/a` rows from handed-off threads.
- Board `[cost]` notes were cut off by concurrent writes before #125.
  Check every row file has all ten cells before adding it; rebuild a cut
  row from the reporter's daily log, or ask.
