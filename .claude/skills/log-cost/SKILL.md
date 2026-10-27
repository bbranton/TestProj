---
name: log-cost
description: Report what this thread cost to the CFO, from the session's own usage data, so it lands in team/Management/cost-log.md. Use when a thread's PR merges or closes, when a reviewer thread finishes, or when asked what a thread cost.
---

# Report a thread's cost

Only the [CFO persona](../../../team/Management/personas/cfo.md) edits
`team/Management/cost-log.md`. Every other thread reports its row and doesn't
open a cost-log PR or add rows to its own PR.

1. Look up this session's usage: call the `get_session` tool of the
   `claude-code-remote` server with no `session_id`. The numbers are under
   `external_metadata.usage`: `output_tokens`, `cache_read_tokens`,
   `cache_write_tokens`, `input_tokens`, and `cost_usd`. If the tool isn't
   available, say so and don't guess.
2. Count the size units, as defined in
   [the cost log](../../../team/Management/cost-log.md#size-units): threads, PRs,
   review rounds, and files changed.
3. Write the row in the log's column order, with a note for anything that
   made the cost unusual, such as a long thread, CI failures, or a design
   change partway through.
4. Report it: add a note to the [team board](../../../team/workspace.md#the-board),
   in this form, and message the CFO thread if one is open:

   ```
   - [cost] <Persona> → CFO · | <Date> | <PR> | <Owner or Reviewer> | <Persona> | <T / P / R / F> | <Output> | <Cache read> | <Cache write> | <Cost> | <Notes> | · <date>
   ```

Usage is the whole session so far. Report it once, when the thread's work
is done. If a thread is reused for later work, report only the change since
its last row and say so in the notes.

## As the CFO

Collect the `[cost]` notes from the board and any rows sent to you, and
add them all in one PR, as the
[CFO persona](../../../team/Management/personas/cfo.md#how-it-works) says. Add
your own row with them. After the PR merges, delete the notes it added.
