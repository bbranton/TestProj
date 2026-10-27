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

- `notes/`: each persona's lasting notes (`<persona>.md`) and daily logs
  (`YYYY-MM-DD-<persona>.md`).
- `personas/`: one file for each persona that can work on the team, named
  after the job title, such as `architect.md`.
- `scripts/`: reusable scripts for jobs the team repeats often.

Each persona may freely update its own files in its team's folder (its
persona file, notes, and daily log), through a PR like any other change;
see the *Only your own persona's area* row of the
[review protocol](review-protocol.md#who-reviews-what). Another persona's
files, even in the same team, get that persona's review, and a team script
or skill gets a review from the other personas who use it. Shared files at
the top of `team/` and other teams' folders are not a persona's to change
alone.

## Persona notes

Each persona has a lasting notes file in its team's `notes/` folder, named
after its job title like its persona file, such as
`QA/notes/test-engineer.md`. Before starting work as
a persona, read its notes. When you learn something the next thread would
otherwise have to rediscover, add it in the same PR as your work.

A lasting note is one or two lines: the rule, then why. Notes that turn out wrong
are deleted, not left with a correction. A note that every persona needs
belongs in [CLAUDE.md](../CLAUDE.md) instead.

## Daily notes

Each persona keeps one daily log per day, in its team's `notes/` folder,
named `YYYY-MM-DD-<persona>.md` with the persona's file name, such as
`Development/notes/2026-10-27-devops-engineer.md`.

- **One file per day per persona.** Every thread working as that persona
  that day adds to the same file. Two DevOps engineer threads share
  `2026-10-27-devops-engineer.md`; a Developer thread writes to
  `2026-10-27-developer.md`, never to another persona's log.
- **Only on days with work.** Don't create a log for a day the persona had
  no tasks.
- **Add, don't rewrite.** Read the file just before you change it, add your
  entries at the end, and leave other threads' entries as they are. Logs
  go in through a PR like any other change; if two PRs add to the same log,
  keep both sets of entries when you merge.
- **Open to everyone.** Logs aren't private. Any persona, in any team, can
  read any other persona's logs when it helps.

Start each entry with a heading naming the thread's task and its PR, then
short bullets on what was done. Record each decision in this form, so a
search for `Decision:` finds every one:

```markdown
### Decision: <one-line summary>

- **Date:** YYYY-MM-DD
- **Decided by:** Team Lead, or the persona that owns the call
- **Options:** each option considered, in a few words
- **Recommendation:** what the persona recommended, and why
- **Outcome:** what was decided, if it differs from the recommendation
- **Links:** PR, issue, thread, or doc sections
```

Lessons that will matter beyond the day go in the persona's lasting notes
file, not only in the daily log.

## Team skills

Skills live in `.claude/skills/<name>/SKILL.md`, so every session finds
them. A skill's script lives in the `scripts/` folder of the team that owns
it, and the `SKILL.md` says how to run it.

| Skill | What it does | Mostly used by |
|-------|--------------|----------------|
| `trace-requirement` | Finds a requirement ID in the design, UI spec, test plan, and code; lists requirements with no test. Script: [`QA/scripts/trace.py`](QA/scripts/trace.py) | Requirements engineer, Test engineer, Developer |
| `ci-paths` | Says which workflows a branch's changes will trigger. Script: [`Development/scripts/ci_paths.py`](Development/scripts/ci_paths.py) | DevOps |
| `log-cost` | Reports a thread's real token use and cost to the CFO, who adds it to the [cost log](Management/cost-log.md) | Every thread, when its work is done |
| `cross-review` | Steps for the owner and for each fresh reviewer thread in a cross-review | Owner and reviewer threads |

To add a skill, copy an existing folder, write a `SKILL.md` whose
`description` says when to use it, put any script in the owning team's
`scripts/` folder, and add a row here. Scripts use only the
standard library, so they run anywhere without installing anything.

## PR template

[`.github/pull_request_template.md`](../.github/pull_request_template.md)
fills in every new PR's description with the sections the
[review protocol](review-protocol.md) needs: requirement IDs, the owner, the
reviewers the author picked and why, verdicts, findings,
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
