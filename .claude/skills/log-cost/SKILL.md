---
name: log-cost
description: Record what this thread cost in docs/team/cost-log.md, from the session's own usage data. Use when a thread's PR merges or closes, when a reviewer thread finishes, or when asked what a thread cost.
---

# Log a thread's cost

1. Look up this session's usage: call the `get_session` tool of the
   `claude-code-remote` server with no `session_id`. The numbers are under
   `external_metadata.usage`: `output_tokens`, `cache_read_tokens`,
   `cache_write_tokens`, `input_tokens`, and `cost_usd`. If the tool isn't
   available, say so and don't guess.
2. Count the size units, as defined in
   [the cost log](../../../docs/team/cost-log.md#size-units): threads, PRs,
   review rounds, and files changed.
3. Add one row to the log in `docs/team/cost-log.md`, in the same PR as the
   work when you can. A reviewer thread that has no PR of its own asks the
   owner thread to add its row.
4. Use a note for anything that made the cost unusual, such as a long
   thread, CI failures, or a design change partway through.

Usage is the whole session so far. Log it once, when the thread's work is
done. If a thread is reused for later work, log only the change since its
last row and say so in the notes.
