# Set up a new project like this one

How to recreate this project in a new Claude project and GitHub repo. This
guide covers only the setup that was done by hand, in the Claude project
or on GitHub's web pages, and isn't recorded anywhere else in the repo.
The team rules themselves are in [CLAUDE.md](/CLAUDE.md) and
[team/](/team/README.md): copy those into the new repo.

In the examples, `<owner>/<repo>` is the new GitHub repo and `<Repo>` its
folder on your computer.

## 1. Give Claude access to the repo

1. Open [Connect GitHub](https://claude.ai/connect-github) and approve.
2. [Install the Claude GitHub app](https://github.com/apps/claude/installations/select_target)
   on your account, choose *Only select repositories*, and add the new
   repo. Without this, threads can read the repo but not push.
3. Add the repo to the project in the project's settings.

## 2. Paste the project instructions

These live in the project's settings, not the repo. Paste them, and fill
in the two placeholders once step 5 is done.

```text
Prefer Markdown for documents, lists, and write-ups. Only use HTML pages when something specifically needs it, such as interactivity, charts, or running an app in the browser.

Any PR that changes the UI must include screenshots of the changed pages or screens in the PR description or a PR comment.

Never use the project owner's first name in the repo (files, docs, commits, code comments). Refer to them as "Team Lead".

Coordinator: post one line in the project chat, with links, in real time whenever a PR merges into develop or a decision request for the Team Lead is raised.

Coordinator: after each merge into develop, ask the "<local clone thread title>" Remote Control thread to run `git pull --ff-only` in <path to your local develop folder> (the Team Lead gave standing OK for fetch and pull on develop).
```

Project memory is off in this project, so anything a later thread needs
must be in these instructions or in the repo.

## 3. Set up GitHub in the web page

Threads can read these settings but can't change them, so you set them on
github.com:

1. **Branches:** create `develop` from `main`, and make `develop` the
   default branch (Settings > General).
2. **Ruleset on `main`** (Settings > Rules > Rulesets > New branch
   ruleset), with no bypass: *Restrict deletions*, *Block force pushes*,
   *Require a pull request before merging*.
3. **Merge settings** (Settings > General > Pull Requests): turn on
   *Automatically delete head branches*, and set merge commits to use the
   PR title and description.
4. **Pages**, if the project has a website: Settings > Pages > Source:
   *GitHub Actions*.
5. **Labels:** create `decision` and one `persona: <job-title>` label per
   persona, with a color and description. Threads can't rename or delete
   labels, so do any later relabeling here too.

## 4. Create the board

The [board](/team/workspace.md#the-board) is in the project's shared
files, not the repo. Create `team/board.md` there with `## Claims` and
`## Notes` headings.

## 5. Set up the local clone

1. Make a folder per branch, such as `~/dev/<owner>/<Repo>/main` and
   `~/dev/<owner>/<Repo>/develop`. Each is a full clone, not a worktree.
2. Ask the coordinator for a thread named, for example, "Set up local
   <Repo> clone", and ask it to work on your computer. Approve the Remote
   Control prompt for the parent folder, such as `~/dev/<owner>`.
3. Ask it to clone over SSH:

   ```sh
   git clone git@github.com:<owner>/<repo>.git ~/dev/<owner>/<Repo>/main
   git clone -b develop git@github.com:<owner>/<repo>.git ~/dev/<owner>/<Repo>/develop
   ```

   If you already clone other repos over SSH, git needs no more setup.
   The `gh` command isn't installed and isn't needed.
4. Give it the standing OK in that thread, in these words: "you have my
   standing OK to run `git fetch` and `git pull --ff-only` on `develop`
   when asked". Anything else still needs your OK each time.
5. Put the thread's title and the `develop` path into the last project
   instruction from step 2.

Don't edit files in the `develop` folder by hand, so every pull
fast-forwards. Pulls wait while your computer is offline, and one pull
catches up on every merge.

## 6. Copy the team files

Copy `CLAUDE.md`, `team/`, `.claude/skills/`, and
`.github/pull_request_template.md` into the new repo in one PR into
`develop`. Leave out the daily logs and cost-log rows, and start each
persona's notes file and the glossary empty. Then search for `TestProj`,
`bbranton`, `canvas`, `FR-`, and `student`, and change each hit for the
new product.
