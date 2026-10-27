# Team workspace

Personas often run in parallel threads that can't see each other. This is
how they share what they know and avoid stepping on each other's work.

There are six places, for six kinds of information:

| What | Where | Why there |
|------|-------|-----------|
| Each persona's lasting notes and daily logs | The [notes folder](#persona-notes), in the project's shared files | No PR; one file per writer |
| Scripts a team runs often | `team/<Team>/scripts/`, called from a skill in `.claude/skills/` | The script lives with its team; every agent session loads skills automatically |
| Who is working on what right now, and handoffs | The board, in the project's shared files | Instant, no PR needed |
| What each thread cost | The cost log and row files, in the project's shared files | No PR; one file per row, as the [CFO persona](/team/Management/personas/cfo.md#role) says |
| Process ideas waiting for the next retro | The [ideas file](#process-ideas), in the project's shared files | No PR or review for a one-line idea |
| Each disagreement between an owner and a reviewer | Library: `disagreements/`, one file per disagreement, as [Logging a disagreement](/team/review-protocol.md#logging-a-disagreement) says | No PR; the retro reads them |

## Team folders

Each team has a folder under `team/`, with two subfolders:

- `personas/`: one file for each persona that can work on the team, named
  after the job title, such as `architect.md`.
- `scripts/`: reusable scripts for jobs the team repeats often.

A file a team keeps as a record, such as the QA team's
[security register](/team/QA/security-register.md), sits in the team's
folder itself.

Changes to these folders go through a PR like any other change, reviewed
as [Who reviews what](/team/review-protocol.md#who-reviews-what) says.

## Persona notes

Persona notes and daily logs live in Library: `notes/`, in the
project's shared files, not in the repo (Team Lead, 2026-10-27,
[#127](https://github.com/bbranton/TestProj/issues/127)). They need no PR.

Each persona has a lasting notes file there, named after its job title
like its persona file, such as Library: `notes/test-engineer.md`.
Before starting work as a persona, read its notes. When you learn something
the next thread would otherwise have to rediscover, add it while you work.
Only threads of that persona change its notes file.

The folder keeps no history, and the last write wins, so treat it like the
[board](#the-board):

- Read a file just before you change it, and change only your own lines.
- Re-read it about ten seconds after writing, to check your change survived.
- **No secrets:** never write a Canvas token, cookie, secret, or student
  data in a notes file or daily log. Link to the evidence instead.

A session outside this project, such as the Team Lead's local clone, can't
see the notes folder. It works from the repo and says that it had no notes.

A lasting note is one or two lines: the rule, then why. Notes that turn out wrong
are deleted, not left with a correction. A note that every persona needs
belongs in [CLAUDE.md](/CLAUDE.md) instead.

## Daily notes

Each thread keeps its own daily log for each day it works, in
Library: `notes/daily/`, named
`YYYY-MM-DD-<persona>-<pr>.md` with the persona's file name and the PR it
works on, such as `2026-10-28-devops-engineer-pr130.md`. A thread with no
PR uses its issue number or a short task name instead.

- **One file per thread per day.** No two threads write the same file, so
  nothing is lost when the last write wins. Two DevOps engineer threads on
  PRs #130 and #131 write `2026-10-28-devops-engineer-pr130.md` and
  `2026-10-28-devops-engineer-pr131.md`; a reviewer thread adds
  `-review`, such as `2026-10-28-architect-pr130-review.md`.
- **Only on days with work.** Don't create a log for a day the thread had
  no tasks.
- **Open to everyone.** Logs aren't private. Any persona, in any team, can
  read any other persona's logs when it helps.

Start each entry with a heading naming the thread's task and its PR, then
short bullets on what was done.

Decisions are recorded in the PR, where reviewers see them: the owner adds
each one to the *Decisions* section of the PR description before merging,
as [Close out](/team/review-protocol.md#close-out) says. A Team Lead
decision also has its `decision` issue. Use this form, so a search for
`Decision:` finds every one:

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
| `trace-requirement` | Finds a requirement ID in the design, UI spec, test plan, and code; lists requirements with no test. Script: [`QA/scripts/trace.py`](/team/QA/scripts/trace.py) | Requirements engineer, Test engineer, Developer |
| `ci-paths` | Says which workflows a branch's changes will trigger. Script: [`Development/scripts/ci_paths.py`](/team/Development/scripts/ci_paths.py) | DevOps engineer |
| `log-cost` | Writes a thread's real token use and cost to its own row file in the Library for the CFO's cost log, as the [CFO persona](/team/Management/personas/cfo.md#role) says | Every thread, when its work is done |
| `cross-review` | Steps for the owner and for each fresh reviewer thread in a cross-review | Owner and reviewer threads |
| `retro` | Steps for a team retro the Team Lead calls: each persona's feedback, and the project manager's note in `team/retros/` | Coordinator, every persona, project manager |

To add a skill, copy an existing folder, write a `SKILL.md` whose
`description` says when to use it, put any script in the owning team's
`scripts/` folder, and add a row here. Scripts use only the
standard library, so they run anywhere without installing anything.

## PR template

[`.github/pull_request_template.md`](/.github/pull_request_template.md)
fills in every new PR's description with the sections the
[review protocol](/team/review-protocol.md) needs: the files that state a changed process
rule, requirement IDs, the owner, the reviewers the author picked and why,
verdicts, findings, deferred findings, testing, and screenshots. Keep its sections in step with the protocol.

## The board

The board is Library: `team/board.md`, in the project's shared
files. It isn't in the repo, so updating it needs no PR. Every thread in the
project can read and write it. The file keeps no history, and the last write
wins, so:

- Read the board just before you change it, and change only your own lines.
- Re-read it about ten seconds after writing, to check your line survived.

Each line is one claim or one note:

```
- [claim] Architect · editing 03-design.md for FR-20 · PR #12 · 2026-10-25
- [note] DevOps engineer → Architect · new backend env var CANVAS_TIMEOUT needs a default · 2026-10-25
- [posting] DevOps engineer · review of PR #12 · 2026-10-25 21:30
```

A `[posting]` line holds the PR's one GitHub draft review while a reviewer
posts, as [Posting reviews one at a time](/team/review-protocol.md#posting-reviews-one-at-a-time)
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
   picks up a persona next, or a
   [wording-only change](/team/review-protocol.md#wording-only-changes-notify-the-persona)
   to its persona file. The persona it's for deletes the note once
   handled. Anything lasting moves into that persona's notes file.

A session outside this project has no board. It should check open PRs for
the same doc instead.

## Process ideas

Process changes wait for the next [retro](/.claude/skills/retro/SKILL.md),
not a PR of their own (Team Lead, 2026-10-27,
[#98](https://github.com/bbranton/TestProj/issues/98)). When an idea
comes up, any thread adds it to Library: `retros/process-ideas.md`,
in the project's shared files. It isn't in the repo, so it needs no PR,
and the Team Lead can read it in the project's Library at any time.

- **One line per idea:** who, the date, the idea, and a link to what
  prompted it, such as a PR, review, or log entry.
- **No secrets:** never write a Canvas token, cookie, secret, or student
  data in it. Anyone in the project can read it and it keeps no history,
  so link to the evidence instead.
- **Same care as the board:** read the file just before you change it, add
  only your own lines, and re-read it about ten seconds after writing.
- **The retro uses it.** Each persona reads it when a retro starts, and
  the project manager removes the ideas the retro note covered once the
  note merges.

A change needed to unblock work right now is still a decision request to
the Team Lead, not an idea for later.

## One thread per PR

Every PR gets its own fresh owner thread (Team Lead, 2026-10-27,
[#95](https://github.com/bbranton/TestProj/issues/95)). Long, reused
threads were most of the team's bill, and a fresh thread for one small PR
costs about $1 to $2.

- **A thread carries one PR to the end.** Its review rounds, fixes, and
  daily log entries stay in that thread.
- **At about $10, ask the Team Lead about a hand-off.** After each Team
  Lead round, an owner thread checks its cost as the `log-cost` skill's
  *Checking cost mid-thread* says. Once it passes about $10, it asks the
  Team Lead whether now is a good time to hand off; there's no hard cap,
  and the Team Lead may say carry on. If `get_session` has no
  `external_metadata.usage.cost_usd`, ask after about four Team Lead
  rounds instead, and say the thread can't read its cost. On a yes, the
  thread:
  1. adds a hand-off note to its daily log: the PR and branch, what's
     done, what's left, open findings, decisions waiting on the Team
     Lead, and the files to read first;
  2. leaves a board `[note]` for the next thread of its persona that
     points to that log entry, and hands over its board claim;
  3. reports its cost with the `log-cost` skill;
  4. asks the coordinator for a fresh thread of the same persona, linking
     the note, and unsubscribes from the PR's GitHub activity, since
     events reach only one thread per PR.

  The fresh thread subscribes to the PR, checks the PR for reviews and CI
  results it missed in between, tells the open reviewer threads it is now
  the owner, deletes the board note, and carries on.
- **Once the PR merges or closes, the thread is done.** It reports its
  cost with the `log-cost` skill and takes no new work.
- **New work goes to a new thread.** Only the coordinator starts threads.
  The coordinator also starts the CFO's daily batch thread, as
  [Daily batch thread](/team/Management/personas/cfo.md#daily-batch-thread)
  says. When the Team Lead asks a thread for work outside its PR, or follow-up
  work after its PR has merged, the thread asks the coordinator for a
  fresh thread of the persona that owns the work, attaching the Team
  Lead's message, and tells the Team Lead in one line. The new thread
  starts from the persona's notes, the old thread's daily log, and the
  PR, not from the old thread.
- **Reviewers already work this way:** each reviewer is a fresh thread, as
  the [review protocol](/team/review-protocol.md#one-thread-per-reviewer)
  says.
