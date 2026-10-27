---
name: log-cost
description: Report what this thread cost, from the session's own usage data, by writing its row file to the cost folder in the project's Library for the CFO. Use when a thread's PR merges or closes, when an owner thread hands off, when a reviewer thread finishes, or when asked what a thread cost.
---

# Report a thread's cost

Write your row to a file of your own instead of adding it to the cost log
yourself, as the [CFO persona](/team/Management/personas/cfo.md#role) says.

1. Look up this session's usage: call the `get_session` tool of the
   `claude-code-remote` server with no `session_id`. The numbers are under
   `external_metadata.usage`: `output_tokens`, `cache_read_tokens`,
   `cache_write_tokens`, `input_tokens`, and `cost_usd`. If the tool isn't
   available, or the session has no `external_metadata.usage` (many
   don't), write `n/a` in the number columns, say why in the notes, and
   don't guess.
2. Count the [size units](/team/Management/personas/cfo.md#size-units):
   threads, PRs, review rounds, and files changed.
3. Write the row in the [column order](/team/Management/personas/cfo.md#columns).
4. Save it as a new row file in the project's Library, named as the CFO
   persona's [How it works](/team/Management/personas/cfo.md#how-it-works)
   says, such as
   Library: `costs/2026-10-27-devops-engineer-pr115-reviewer.md`.
   The file holds the one row and nothing else. Never change an existing
   file there. Re-read your file about ten seconds after writing it.

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
`After hand-off`.

## Checking cost mid-thread

The same lookup as step 1 gives an owner thread its cost for the
hand-off check in [One thread per PR](/team/workspace.md#one-thread-per-pr):
read `external_metadata.usage.cost_usd`. Don't report a row for a
mid-thread check. If there's no `cost_usd`, follow that section's rule for
when the cost can't be read.

## As the CFO

Add the row files to the combined table as the CFO persona's
[Daily batch thread](/team/Management/personas/cfo.md#daily-batch-thread)
says.
