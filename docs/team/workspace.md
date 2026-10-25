# Team workspace

Personas often run in parallel threads that can't see each other. This is
how they share what they know and avoid stepping on each other's work.

There are two places, for two kinds of information:

| What | Where | Why there |
|------|-------|-----------|
| Lasting knowledge: conventions, lessons, gotchas | [`docs/team/notes/`](notes/), one file per persona | Versioned and reviewed in PRs |
| Scripts a persona uses often | `.claude/skills/`, one folder per skill | Every agent session loads skills automatically |
| Who is working on what right now, and handoffs | The board, in the project's shared files | Instant, no PR needed |

## Persona notes

Each persona has a notes file in [`notes/`](notes/). Before starting work as
a persona, read its notes. When you learn something the next thread would
otherwise have to rediscover, add it in the same PR as your work.

A note is one or two lines: the rule, then why. Notes that turn out wrong
are deleted, not left with a correction. A note that every persona needs
belongs in [CLAUDE.md](../../CLAUDE.md) instead.

## Team skills

Skills live in `.claude/skills/<name>/SKILL.md`, with any script beside it.

| Skill | What it does | Mostly used by |
|-------|--------------|----------------|
| `trace-requirement` | Finds a requirement ID in the design, UI spec, test plan, and code; lists requirements with no test | Product and QA |
| `ci-paths` | Says which workflows a branch's changes will trigger | DevOps |
| `cross-review` | Runs a cross-review by the [review protocol](review-protocol.md) | Anyone asked to cross-review |

To add a skill, copy an existing folder, write a `SKILL.md` whose
`description` says when to use it, and add a row here. Scripts use only the
standard library, so they run anywhere without installing anything.

## The board

The board is `/mnt/project-files/team/board.md`, in the project's shared
files. It isn't in the repo, so updating it needs no PR. Every thread in the
project can read and write it. The file keeps no history, and the last write
wins, so:

- Read the board just before you change it, and change only your own lines.
- Re-read it about ten seconds after writing, to check your line survived.

Each line is one claim or one note:

```
- [claim] Architecture · editing 03-design.md for FR-20 · PR #12 · 2026-10-25
- [note] DevOps → Architecture · new backend env var CANVAS_TIMEOUT needs a default · 2026-10-25
```

Rules:

1. **Claim before you edit a doc or start a review.** If someone else has
   claimed it, don't start. Tell the Team Lead, or message that thread when
   your work depends on theirs.
2. **Release when done.** Delete your claim when the PR merges or the work
   stops.
3. **Stale claims.** A claim older than two days with no open PR can be
   removed by anyone. Say so in your thread.
4. **Notes are for handoffs**, such as advice or a question for whoever
   picks up a persona next. The persona it's for deletes the note once
   handled. Anything lasting moves into that persona's notes file.

A session outside this project has no board. It should check open PRs for
the same doc instead.
