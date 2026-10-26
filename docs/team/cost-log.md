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
| 2026-10-25 | #10, #11 | Owner | (none; set up the team) | 1 / 2 / ~16 / 27 | 95K | 25.9M | 0.27M | 11.08 | Taken just before merge. Long thread with many small rounds; docs and small scripts only, no app code. |
| 2026-10-25 | #4 (and #5, handed off) | Owner | Management | 1 / 2 / 4 / 3 | 57K | 10.6M | 0.39M | 7.31 | Taken before review, so review rounds aren't included yet. Read all five docs up front; also opened the requirements PR (#5) before the switch to one thread per doc, then handed it off. Docs only. |
| 2026-10-25 | #12 | Owner | Management | 1 / 1 / 0 / 7 | n/a | n/a | n/a | n/a | Usage numbers weren't in the session data (`external_metadata.usage` missing), so none are logged. Docs only. |
| 2026-10-25 | (this PR) | Owner | Management | 1 / 1 / 0 / 14 | n/a | n/a | n/a | n/a | Usage numbers weren't in the session data (`external_metadata.usage` missing). Docs only, plus 8 follow-up issues (#16 to #23) from reading the open doc PRs. |
| 2026-10-26 | #4 | Owner | Management | 5 / 1 / 4 / 3 | 111K | 32.1M | 0.46M | 13.77 | Change since the 2026-10-25 #4 row (whole thread: 168K / 42.7M / 0.85M / $21.08). Long thread: a mid-review scope change (deploy every phase), hosting cost research with DevOps (Pages, Pipedream, Neon, free hosts), two decision cards, a Security review added at the end, and two master merges. Threads count the owner plus four reviewers; their rows are added below when they send them. Docs only. |
