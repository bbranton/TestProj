# Team workspace

Personas often run in parallel threads that can't see each other. This is
how they share what they know and avoid stepping on each other's work.

There are three places, for three kinds of information:

| What | Where | Why there |
|------|-------|-----------|
| Lasting knowledge, daily notes, and findings | `team/<Team>/notes/` | Versioned in PRs, owned by the team |
| Scripts a team runs often | `team/<Team>/scripts/`, called from a skill in `.claude/skills/` | The script lives with its team; every agent session loads skills automatically |
| Who is working on what right now, and handoffs | The board, in the project's shared files | Instant, no PR needed |

## Team folders

Each team has a folder under `team/`, with three subfolders:

- `notes/`: daily notes and important findings.
- `personas/`: one file for each persona that can work on the team.
- `scripts/`: reusable scripts for jobs the team repeats often.

Each team may freely update its own folder as needed, through a PR like
any other change; see the *A team's own folder* row of the
[review protocol](review-protocol.md#who-reviews-what). Shared files at the
top of `team/` and other teams' folders are not the team's to change alone.

## Persona notes

Each persona has a lasting notes file in its team's `notes/` folder, named
after the persona, such as `QA/notes/product-qa.md`. Before starting work as
a persona, read its notes. When you learn something the next thread would
otherwise have to rediscover, add it in the same PR as your work.

Daily notes go in the same folder as `YYYY-MM-DD.md`, only on days the team
had tasks. Don't create a daily file for a day with no work.

A note is one or two lines: the rule, then why. Notes that turn out wrong
are deleted, not left with a correction. A note that every persona needs
belongs in [CLAUDE.md](../CLAUDE.md) instead.

## Team skills

Skills live in `.claude/skills/<name>/SKILL.md`, so every session finds
them. A skill's script lives in the `scripts/` folder of the team that owns
it, and the `SKILL.md` says how to run it.

| Skill | What it does | Mostly used by |
|-------|--------------|----------------|
| `trace-requirement` | Finds a requirement ID in the design, UI spec, test plan, and code; lists requirements with no test. Script: [`QA/scripts/trace.py`](QA/scripts/trace.py) | Product and QA, Developer |
| `ci-paths` | Says which workflows a branch's changes will trigger. Script: [`DevOps/scripts/ci_paths.py`](DevOps/scripts/ci_paths.py) | DevOps |
| `log-cost` | Reports a thread's real token use and cost to the CFO, who adds it to the [cost log](Finance/cost-log.md) | Every thread, when its work is done |
| `cross-review` | Steps for the owner and for each fresh reviewer thread in a cross-review | Owner and reviewer threads |

To add a skill, copy an existing folder, write a `SKILL.md` whose
`description` says when to use it, put any script in the owning team's
`scripts/` folder, and add a row here. Scripts use only the
standard library, so they run anywhere without installing anything.

## PR template

[`.github/pull_request_template.md`](../.github/pull_request_template.md)
fills in every new PR's description with the sections the
[review protocol](review-protocol.md) needs: requirement IDs, the owner, the
recommended reviewers for the Team Lead to confirm, verdicts, findings,
follow-up issues, testing, and screenshots. Keep its sections in step with the protocol.

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
- [posting] DevOps · review of PR #12 · 2026-10-25 21:30
```

A `[posting]` line holds the PR's one GitHub draft review while a reviewer
posts, as [Posting reviews one at a time](review-protocol.md#posting-reviews-one-at-a-time)
says.

Rules:

1. **Claim before you edit a doc or start a cross-review.** The owner
   thread claims a cross-review; its reviewer threads don't claim anything.
   If someone else has claimed it, don't start. Tell the Team Lead, or message that thread when
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
