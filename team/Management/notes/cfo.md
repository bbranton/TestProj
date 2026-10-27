# CFO notes

Lasting lessons for the CFO persona. See the
[team workspace](/team/workspace.md#persona-notes) for how notes work.

- Before the CFO existed, every thread appended its own row, so cost-log
  PRs conflicted with each other. Keep one open cost-log PR at a time.
- Some sessions have no `external_metadata.usage`. Log the row with `n/a`
  and say so in the notes, rather than leaving the thread out.
- The hand-off check in [One thread per PR](/team/workspace.md#one-thread-per-pr)
  reads `cost_usd` mid-thread, but on 2026-10-27 this CFO thread's own
  `get_session` had no `usage` at all. Expect the round-count fallback to
  be the common case, and expect `n/a` rows from handed-off threads.
