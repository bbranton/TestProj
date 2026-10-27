---
name: retro
description: Run a team retrospective on how the personas work together, when the Team Lead calls one ("run a retro"), optionally for a window or topic. Use as the coordinator starting it, as a persona writing its feedback, or as the project manager combining the feedback into team/retros/.
---

# Team retro

The Team Lead calls a retro in the project chat, such as "run a retro" or
"run a retro on reviews since the last release". It gathers feedback on how
well the team works together and suggestions for process changes. A retro
changes nothing by itself: each suggestion becomes a
[decision request](/team/review-protocol.md#decisions-are-separate-from-merging),
and the Team Lead picks which to make.

**Window.** What the Team Lead names, or else since the date of the newest
note in `team/retros/`, or the project's start when there is none. A topic,
if given, narrows what each persona looks at.

## As the coordinator

1. Start one fresh thread per persona in the [team README](/team/README.md),
   in parallel, each told the window, the topic, and the retro's date (the
   day it was called). A full retro is about eleven threads (each persona,
   the project manager, and the note's reviewer), roughly $12 to $20 from
   recent cost log rows (Library: `costs/cost-log.md`), so the Team Lead
   can name fewer personas to save cost.
2. When every persona has replied, start a project manager thread to
   combine the feedback.
3. Post the retro note's PR and its decision requests in the project chat.

## As a persona

1. Read your persona file and notes
   (Library: `notes/<persona>.md`), then gather evidence from the
   window: your daily logs (Library: `notes/daily/`), the PRs
   and reviews you took part in, and your rows in the cost log
   (Library: `costs/cost-log.md`) plus any of your row files
   beside it that aren't logged yet. Also read the
   [process ideas](/team/workspace.md#process-ideas) folder, and take up any
   idea in your area that the evidence supports.
2. Write about five bullets in all, under three headings: **What worked**,
   **What got in the way**, and **One suggested change**. Link each bullet to
   its evidence: a PR, a review, a log entry, or a cost row. The suggestion
   names the file it would change, and is a recommendation, not an edit.
   Never quote a Canvas token, cookie, secret, or student data.
3. Save it as Library: `retros/<retro date>/<persona>.md`, with the
   persona's file name, such as `devops-engineer.md`. It isn't in the repo,
   so it needs no PR, and no daily log entry: the file and the retro note
   are the record. Reply in your thread with a one-line summary.
4. Report your cost with the `log-cost` skill.

## As the project manager

1. Read every persona's file in Library: `retros/<retro date>/`,
   the previous note in `team/retros/`, and the
   [process ideas](/team/workspace.md#process-ideas) folder.
2. Write `team/retros/<retro date>.md` with these sections:
   - **Window and topic**, and which personas took part.
   - **Did the last changes help?** For each change made from the previous
     retro, what the feedback and logs show since.
   - **Themes**: points raised by more than one persona, grouped, naming
     who raised each and linking the evidence.
   - **Suggestions**: each suggested change, merged where personas
     suggested the same thing, with a link to its decision request. Add
     any idea from the process ideas folder that no persona took up, naming
     who logged it.

   As in the feedback, link evidence and never quote a Canvas token,
   cookie, secret, or student data.
3. Raise one decision request per suggestion, as a GitHub issue labeled
   `decision`, with your recommendation and the files it changes. Open a
   PR with the note, reviewed as the [review protocol](/team/review-protocol.md#who-reviews-what)
   says. Once it merges, clear the ideas it covered, as
   [Process ideas](/team/workspace.md#process-ideas) says.
4. Once the Team Lead answers, the persona that owns each file makes an
   approved change in its own PR, citing the decision. List those PRs under
   the suggestion in the next retro's note, so it can check whether they
   helped.
