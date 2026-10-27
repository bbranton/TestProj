---
name: log-cost
description: Report what this thread cost to the CFO, from the session's own usage data, so it lands in team/Management/cost-log.md. Use when a thread's PR merges or closes, when an owner thread hands off, when a reviewer thread finishes, or when asked what a thread cost.
---

# Report a thread's cost

Report your row to the [CFO persona](/team/Management/personas/cfo.md)
instead of opening a cost-log PR or adding rows to your own PR. The CFO adds
reported rows to `team/Management/cost-log.md` in batches, so parallel PRs
don't conflict on the log.

1. Look up this session's usage: call the `get_session` tool of the
   `claude-code-remote` server with no `session_id`. The numbers are under
   `external_metadata.usage`: `output_tokens`, `cache_read_tokens`,
   `cache_write_tokens`, `input_tokens`, and `cost_usd`. If the tool isn't
   available, or the session has no `external_metadata.usage` (many
   don't), write `n/a` in the number columns, say why in the notes, and
   don't guess.
2. Count the size units, as defined in
   [the cost log](/team/Management/cost-log.md#size-units): threads, PRs,
   review rounds, and files changed.
3. Write the row in the log's column order, with a note for anything that
   made the cost unusual, such as a long thread, CI failures, or a design
   change partway through.
4. Report it: add a note to the [team board](/team/workspace.md#the-board),
   in this form, and message the CFO thread if one is open:

   ```
   - [cost] <Persona> → CFO · | <Date> | <PR> | <Owner or Reviewer> | <Persona> | <T / P / R / F> | <Output> | <Cache read> | <Cache write> | <Cost> | <Notes> | · <date>
   ```

Usage is the whole session so far. Report it once, when the thread's work
is done. If a thread is reused for later work, report only the change since
its last row and say so in the notes.

## At a hand-off

An owner thread that hands its PR to a fresh thread, as
[One thread per PR](/team/workspace.md#one-thread-per-pr) says, reports
its row before asking for the new thread. Its work on the PR isn't done,
so start the notes with `Hand-off 1 of the PR` (2, 3, ... for later
hand-offs) and count only the rounds and files this thread did. The fresh
thread reports its own row when the PR merges, and its notes say
`After hand-off`. The CFO adds the rows for one PR together.

## Checking cost mid-thread

The same lookup as step 1 tells an owner thread when it's near the
hand-off check of about $10: read `external_metadata.usage.cost_usd`.
Don't report a row for a mid-thread check. If there's no `cost_usd`,
count Team Lead rounds instead, as the workspace rule says, and tell the
Team Lead the cost can't be read when you ask about a hand-off.

## As the CFO

Collect the `[cost]` notes from the board and any rows sent to you, and
add them all in one PR, as the
[CFO persona](/team/Management/personas/cfo.md#how-it-works) says. Add
your own row with them. After the PR merges, delete the notes it added.
