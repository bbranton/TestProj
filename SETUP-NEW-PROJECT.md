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

1. **Branches:** create the repo with a README, so `main` has a first
   commit. Then create `develop` from `main`, and make `develop` the
   default branch (Settings > General).
2. **Ruleset on `main`** (Settings > Rules > Rulesets > New branch
   ruleset), with no bypass: *Restrict deletions*, *Block force pushes*,
   *Require a pull request before merging*.
3. **Merge settings:** as the
   [DevOps engineer notes](/team/Development/notes/devops-engineer.md)
   record them.
4. **Pages**, if the project has a website: Settings > Pages > Source:
   *GitHub Actions*. Then, since `develop` is the default branch, add
   `main` under Settings > Environments > github-pages > Deployment
   branches and tags, or the first deploy from `main` fails.
5. **Security** (Settings > Code security): turn on secret scanning,
   push protection, and Dependabot alerts. Under Settings > Actions >
   General, check that *Workflow permissions* is *Read repository
   contents*.
6. **Labels:** create `decision` and one `persona: <job-title>` label per
   persona, with a color and description. Threads can't rename or delete
   labels, so do any later relabeling here too.

## 4. Create the board

The [board](/team/workspace.md#the-board) is in the project's shared
files, not the repo. Create `team/board.md` there with `## Claims` and
`## Notes` headings.

## 5. Set up the local clone

1. Make only `~/dev/<owner>/<Repo>`. The clones in step 3 create its
   `main` and `develop` folders, each a full clone, not a worktree.
2. Ask the coordinator for a thread named, for example, "Set up local
   <Repo> clone", and ask it to work on your computer. Approve the Remote
   Control prompt for `~/dev/<owner>/<Repo>` only, not a parent folder, so
   the thread can't read your other repos.
3. Ask it to clone. For a public repo, use HTTPS, which needs no
   credentials:

   ```sh
   git clone https://github.com/<owner>/<repo>.git ~/dev/<owner>/<Repo>/main
   git clone -b develop https://github.com/<owner>/<repo>.git ~/dev/<owner>/<Repo>/develop
   ```

   For a private repo, add a read-only deploy key for that one repo
   (Settings > Deploy keys) and clone over SSH with it, rather than your
   own SSH key, which can push to every repo you own. The `gh` command
   isn't needed.
4. Give it the standing OK in that thread, in these words: "you have my
   standing OK to run `git fetch` and `git pull --ff-only` on `develop` in
   `~/dev/<owner>/<Repo>/develop` when asked". Anything else still needs your OK each time.
5. Put the thread's title and the `develop` path into the last project
   instruction from step 2.

The Remote Control session runs as your own user, with your local
credentials. The standing OK is an instruction to Claude, not a technical
limit, so keep secrets such as `.env` files and tokens out of the approved
folder.

Don't edit files in the `develop` folder by hand, so every pull
fast-forwards. Pulls wait while your computer is offline, and one pull
catches up on every merge.

## 6. Copy the team files

Copy `CLAUDE.md`, `team/`, `.claude/skills/`, and
`.github/pull_request_template.md` into the new repo in one PR into
`develop`. Leave out the daily logs and cost-log rows, and start each
persona's notes file empty, except for the
[Security register](/team/QA/notes/cybersecurity-engineer.md#security-register)
heading, intro, and empty table.

The process also lives in two docs under `docs/canvas-portal/`. Start a
roadmap with empty *Open decisions*, *Risks*, *Backlog*, and *Change log*
sections, as in [01-roadmap.md](/docs/canvas-portal/01-roadmap.md), copy
the [glossary](/docs/canvas-portal/glossary.md)'s layout with no terms,
and update the links that point at `docs/canvas-portal/`.

Don't copy `.github/workflows/`, since workflows depend on the product.
Write new ones using this repo's as the pattern, and deploy only from
`main`.

Then search for `TestProj`,
`bbranton`, `canvas`, `FR-`, and `student`, and change each hit for the
new product.
