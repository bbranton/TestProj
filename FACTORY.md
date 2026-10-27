# The Software Factory

This repo is a Software Factory: a team of AI personas, and the products it
builds side by side. This file says what the factory is for and how we'll
show it works. The team's rules are in [CLAUDE.md](/CLAUDE.md) and
[team/](/team/README.md).

## Goal

Build a reusable Software Factory: a process in which a team of AI personas
turns a brief into working, tested, maintainable software, and that gets
cheaper and better over time. First prove the process by building at least
one small product end to end. Then improve it by A/B testing: give two
teams the same brief, each with one small process change, and keep
whichever change scores better.

The product is the proof. The reusable process is the goal.

(Team Lead, 2026-10-27.)

## Repo layout

Each product and each team gets its own folder, so more of either can sit
side by side later.

| Folder | What it holds |
|--------|---------------|
| [team/](/team/README.md) | The team: personas, review protocol, workspace rules, team decision register, retros |
| [canvas-portal/](/canvas-portal/README.md) | The first product's code |
| [docs/canvas-portal/](/docs/canvas-portal/README.md) | The first product's roadmap, requirements, design, UI specification, and test plan |
| [qml-hello-wasm/](/qml-hello-wasm/) | The starting experiment: a QML hello world built to WebAssembly |
| [site/](/site/index.html) | The GitHub Pages landing page |

A product's docs don't mention the factory. The factory's plan lives here,
so a product can be built the same way whether or not it's part of an
experiment.

## Stages

Stages are the factory's; phases are a product's roadmap, as each
product's glossary says.

### Stage 1: One full product, end to end

Build the Canvas portal from brief to release, using the current process and
refining it as we go: through Phase 1 at least, with Phase 4 as a stretch
goal.

- **Record, don't judge yet.** Record the [scorecard](#scorecard) for every
  feature, but set no targets. This stage gives us the baseline.
- **Process changes are allowed** throughout, each logged with its reason
  as [Daily notes](/team/workspace.md#daily-notes) says.
- **Done when** the Canvas portal meets Phase 1's exit criteria (roadmap
  milestone [M2](/docs/canvas-portal/01-roadmap.md#4-milestones)) on its
  test deploy and is released to `main`, the Team Lead is happy with the
  process, and the process is frozen as **version 1**: an annotated git
  tag `process-v1` on `develop`, so later runs can name exactly which
  process they used. Process tags start with `process-`, so they can't be
  mistaken for product release tags on `main`.

A process version is the repo at its tag (`CLAUDE.md`, `team/`,
`.claude/skills/`, `.github/`) plus a copy of the persona notes taken when
it's tagged, since the Library keeps no history. How the notes are copied,
or whether A/B runs start with empty notes instead, is decided when Stage 1
ends.

### Stage 2, if needed: A second product

After Stage 1's retro, the Team Lead decides whether a second end-to-end
product is needed. Signs it is:

- Stage 1 changed the process so much that version 1 has never run start
  to finish unchanged.
- The process seems tied to the Canvas portal, for example to its stack or
  to its single external API.

The second product should be a different kind, such as a command-line tool
or a small back-end service, so it shows whether the process carries over.
It runs on version 1 with as few changes as possible, and ends with
version 2.

### Stage 3: A/B refinement

Once the process is stable, improve it in small steps.

1. **A benchmark set:** three to five small, fixed briefs, each with
   acceptance tests written up front by someone outside both teams.
2. **One change per experiment,** such as two reviewers instead of four,
   or a shorter persona file. Same model, same briefs.
3. **Repeat runs.** AI runs vary a lot, so run each team two or three
   times, or on several briefs, before trusting a result.
4. **Same input from the Team Lead.** Teams' questions are answered from a
   fixed FAQ, or each question counts as a cost.
5. **A stored baseline.** Score the current process once, then only the
   variant needs fresh runs. Rerun the baseline now and then to check for
   drift.
6. **Keep or drop.** A change is kept only if it wins on the scorecard
   without making any measure clearly worse.

Each experiment is recorded in the repo, with the process version (tag)
each team ran, the brief, the change, every run's scorecard, and the
result, so anyone can repeat it. The Team Lead decides where those records
go, on the project manager's recommendation, before Stage 3 starts.

## Scorecard

The same measures in every stage. In Stages 1 and 2 they're a record; in
Stage 3 they're how teams are compared, so they need no fixed targets.

| Quality | Measure | Source |
|---------|---------|--------|
| Quick | Time from brief to merged feature, and to release | PR and release times |
| Efficient | Cost per feature, and for the whole product | Cost log rows, matched to features by each PR's requirement IDs |
| Efficient | Share of spend on product vs process | Cost log's product-or-process column (not yet measured: a CFO PR adds it) |
| Efficient | Team Lead touches: decision requests, review comments, questions answered | GitHub and threads |
| High quality | Acceptance tests passed (Stage 3) | Benchmark tests |
| High quality | Bugs found after merge | Issues labeled bug |
| High quality | Review rounds before merge | PR history |
| Maintainable | Change test: a fresh thread makes a set change cold; its time, cost, and whether it passes | A timed, costed task |
| Maintainable | Lint clean, test coverage of new code | CI (coverage not yet measured) |

The project manager records the scorecard for each feature when it
merges, and copies each stage's totals into the repo when the stage ends.

The raw cost rows stay in the Library (Library: `costs/`), as the
[CFO persona](/team/Management/personas/cfo.md#role) says. Each stage's
totals are in the repo, so the results keep their history.
