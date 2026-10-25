# Cost log

What each thread actually cost, so Management can estimate new work from
real numbers. Management owns this file; every thread adds its own row.
How to add a row is in the [`log-cost` skill](../../.claude/skills/log-cost/SKILL.md),
and how estimates use it is in
[Management's cost plans](personas/management.md#cost-plans).

## Size units

Size a piece of work by what an agent can count:

- **Threads:** owner and reviewer threads it took.
- **PRs:** pull requests it opened.
- **Rounds:** review or feedback rounds, counting each batch of comments
  the owner answered with a push.
- **Files:** files changed across its PRs.

## Log

Tokens are in thousands (K) or millions (M). *Cache read* is context the
thread re-read on each turn, and is usually most of the cost.

| Date | PR | Thread | Persona | Threads / PRs / rounds / files | Output | Cache read | Cache write | Cost (USD) | Notes |
|------|----|--------|---------|--------------------------------|--------|------------|-------------|------------|-------|
| 2026-10-25 | #10, #11 | Owner | (none; set up the team) | 1 / 2 / ~14 / 25 | 89K | 22.6M | 0.25M | 10.13 | Snapshot while both PRs were still open. Long thread with many small rounds; docs and small scripts only, no app code. |
