# Set up a new project like this one

Steps to recreate this repo's way of working in a new Claude project and
GitHub repo. The rules themselves live in the files linked below; this
guide only says what to set up, what to copy, and what to change. In the
examples, `<owner>/<repo>` is the new GitHub repo and `<Repo>` its folder
on your computer.

## 1. GitHub repo

1. Create the repo with a first commit on `main`, then create `develop`
   from it and make `develop` the default branch.
2. Add a ruleset on `main` with no bypass: restrict deletions, block force
   pushes, require a pull request.
3. Set the merge settings in the [DevOps engineer notes](/team/Development/notes/devops-engineer.md).
4. Create the `decision` label and one `persona: <job-title>` label per
   persona, each with a color and description.
5. Copy [`.github/pull_request_template.md`](/.github/pull_request_template.md),
   and use [`canvas-portal-ci.yml`](/.github/workflows/canvas-portal-ci.yml)
   as the pattern for CI. Deploy only from `main`, as
   [`pages.yml`](/.github/workflows/pages.yml) does.

## 2. Claude project

Create the project, add the repo, and paste these project instructions
into its settings. Fill in the two placeholders once step 4 is done.

```text
Prefer Markdown for documents, lists, and write-ups. Only use HTML pages when something specifically needs it, such as interactivity, charts, or running an app in the browser.

Any PR that changes the UI must include screenshots of the changed pages or screens in the PR description or a PR comment.

Never use the project owner's first name in the repo (files, docs, commits, code comments). Refer to them as "Team Lead".

Coordinator: post one line in the project chat, with links, in real time whenever a PR merges into develop or a decision request for the Team Lead is raised.

Coordinator: after each merge into develop, ask the "<local clone thread title>" Remote Control thread to run `git pull --ff-only` in <path to your local develop folder> (the Team Lead gave standing OK for fetch and pull on develop).
```

## 3. Team files

Copy these from `develop` in one PR, then change what's listed:

| Copy | Change |
|------|--------|
| [`CLAUDE.md`](/CLAUDE.md) | Replace *Canvas portal phases* with the new product's phases, or drop it |
| [`team/README.md`](/team/README.md) | The persona table if it changes; *Security is everyone's job* for what the new product must protect |
| [`team/review-protocol.md`](/team/review-protocol.md) | Doc file names in *Who reviews what*, and the decision register and backlog links |
| [`team/workspace.md`](/team/workspace.md) | The *Team skills* table |
| `team/<Team>/personas/` | Product-specific checklist items |
| `team/<Team>/notes/<persona>.md` | Keep only each file's heading and intro. Don't copy the daily logs |
| `team/<Team>/scripts/` and [`.claude/skills/`](/.claude/skills/) | Doc paths and workflow names. Drop `trace-requirement` if there are no requirement IDs |
| [`team/Management/cost-log.md`](/team/Management/cost-log.md) | Delete the rows |
| [`docs/canvas-portal/glossary.md`](/docs/canvas-portal/glossary.md) | Keep the layout, empty the terms |

Then search for `TestProj`, `bbranton`, `canvas`, `FR-`, and `student`,
and fix each hit.

Create the [board](/team/workspace.md#the-board) as `team/board.md` in the
project's shared files, with `## Claims` and `## Notes` headings.

## 4. Local clone

1. Ask the coordinator for a thread such as "Set up local <Repo> clone",
   and in it ask Claude to work on your computer. Approve the Remote
   Control prompt for the parent folder, such as `~/dev/<owner>`.
2. Ask it to clone over SSH, one full clone per branch:

   ```sh
   git clone git@github.com:<owner>/<repo>.git ~/dev/<owner>/<Repo>/main
   git clone -b develop git@github.com:<owner>/<repo>.git ~/dev/<owner>/<Repo>/develop
   ```

   If you already clone other repos over SSH, git needs no more setup.
3. Give it the standing OK in the thread: "you have my standing OK to run
   `git fetch` and `git pull --ff-only` on `develop` when asked". Anything
   else still needs your OK each time.
4. Put the thread's title and the `develop` path into the last project
   instruction from step 2.

Don't edit files in the `develop` folder by hand, so every pull
fast-forwards. Pulls wait while your computer is offline, and one pull
catches up on every merge.

## Known limits

- Cloud threads can't rename or delete GitHub labels, and setting a
  missing label creates it grey with no description. Manage labels on
  GitHub yourself.
- Threads can read repo settings and rulesets but not change them.
- `gh` isn't installed on the computer with the local clone, so that
  thread only fetches and pulls with git.
