# Glossary

**Status:** Draft · **Owner:** Requirements engineer · **Last updated:** 2026-10-26

The words the team uses for the portal, the docs, and the way we work, each
explained once. Other docs link here instead of defining a term again.

A term marked with a later phase, such as *(Phase 5)*, is described so the
docs read clearly. It is not in scope until its phase starts, as the
[requirements by phase](02-requirements.md#requirements-by-phase) say.

## Keeping it up to date

- **The requirements engineer owns what each term means.** A meaning changes in the
  same PR as the requirement it comes from.
- **UI/UX keeps the screen words in step.** The exact words on screen
  live in the [UI specification](04-ui-specification.md). A PR that changes
  a screen word changes its entry here too.
- **Management keeps the team process terms in step** with the
  [review protocol](../../team/review-protocol.md) and the
  [team README](../../team/README.md).
- **Every persona checks the glossary** before naming something new in a
  doc, and adds the term here in the same PR when it's missing.
- **When a doc and the glossary disagree,** the requirements decide what a
  term means and the UI specification decides how it's written on screen.
  The reviewer who spots it logs an `X-` finding, as the
  [review protocol](../../team/review-protocol.md#findings-table) says.

## The board

The portal follows [Trello](https://trello.com)'s words (goal G-3): a
*board* holds *lists*, lists hold *cards*, and opening a card shows its
*card back*.

| Term | Meaning | Defined in |
|------|---------|------------|
| Board | The home screen, titled "My assignments": four lists of cards, one card per Canvas assignment. In Phase 1 it's read only. Not the [team board](#team-process). | FR-60, S-4 |
| List | One of the board's four columns, always in this order: Backlog, To do, In progress, Done. Older requirements say "column"; it means the same. | FR-31 |
| Backlog | The first list. New Canvas assignments land here until the student moves them. In Phase 1 every card is in Backlog. Not the `backlog` [issue label](#team-process). | FR-31, FR-34 |
| To do, In progress, Done | The other three lists. Cards only move into them when the student drags them *(Phase 2)*. | FR-31, FR-32 |
| Card | One Canvas assignment on the board. Until Phase 5, selecting it opens the assignment in Canvas, in a new tab. | FR-26, FR-65 |
| Card front | What a card shows on the board: the label strip, the title, the due badge, the points, the submission types, and the [card status](#card-status). | FR-65 |
| Card back *(Phase 5)* | The detailed view of a card, opened as a dialog over the board. | FR-28, S-5 |
| Minimized list | A list shrunk to a narrow strip showing its title and card count. Each time the board loads or refreshes, empty lists start minimized. | FR-80 |
| Course | One of the student's active Canvas courses. The docs say "course", never "label". | FR-20 |
| Course button | The button above the lists that shows or hides one course's cards: ● when shown, ○ when hidden. A hidden course's cards keep their list. | FR-78 |
| Label strip | The colored bar on a card that shows its course, in the course's automatic color. | FR-65, FR-66 |
| Orphaned card | A card whose assignment the teacher deleted or unpublished in Canvas. The portal keeps it, with its last Canvas details, and never deletes it. It's hidden by default; the filter menu's show/hide option for cards removed from Canvas shows it grayed out in its list. If the assignment comes back, the card returns to its old list. From Phase 3 a complete Refresh marks it archived. From Phase 5 the student can delete a shown orphaned card for good, with its notes, after confirming. Not the same as an [archived card](#the-board), and say "orphaned" or "removed from Canvas" for it, not "missing", which is a [card status](#card-status). | FR-45, FR-74 |
| Archived card *(Phase 5)* | A card or list the student archived. The filter menu's *Archived* option shows them grayed out, each with a way to restore it. Orphaned cards are never mixed in with them. | FR-74 |

## Refresh and sync

| Term | Meaning | Defined in |
|------|---------|------------|
| Refresh | Fetching the latest courses and assignments from Canvas. Only the student starts one; the portal never refreshes on its own. The action is always called "Refresh". | FR-13, FR-15 |
| Synced time | The header's "Synced Oct 25, 10:42 AM": when the last complete Refresh finished. | FR-13 |
| Complete Refresh | A Refresh where every course arrived. Only a complete Refresh replaces the saved data or archives a card. | FR-14, FR-45 |
| Last complete copy | The Canvas data saved from the last complete Refresh, shown on every load so the board never waits on Canvas. | FR-14 |
| Refresh progress | The panel that shows each course's progress during a Refresh, and the last Refresh's log afterwards. | FR-16, S-10 |
| Refresh incomplete | The summary when a course failed or timed out. The last complete copy stays on the board. | FR-16, NFR-20 |
| Warning banner | The board's message after a failed Refresh, "Couldn't refresh from Canvas. Showing data from ...", which stays until a Refresh completes. | NFR-20, S-4 |

## Card status

Each status comes from the student's own Canvas submission, with nothing
compared to the clock. The exact Canvas fields are in FR-23. Statuses based
on the clock, such as *Due soon*, are FR-27 *(Phase 5)*.

| Term | Meaning | Defined in |
|------|---------|------------|
| Submitted, Not submitted | Whether the student's own submission has a submitted date. | FR-23 |
| Graded, Not graded | Whether the student's current submission has been graded. A resubmission after grading is Not graded until it's graded again. | FR-23 |
| Missing | Canvas marks the assignment missing. The card has a red border, a red "⚠ MISSING" bar, and a red due badge. | FR-23, FR-65 |
| Late, Excused | Tags shown when Canvas marks the submission late or the student excused. They can appear with Submitted and Graded. | FR-23 |
| Due badge | The due date and time, in the device's time zone. Red when Missing, otherwise green with ✓ when Submitted or Graded, otherwise plain. | FR-22, FR-65 |
| Points | The points the assignment is worth, such as "20 pts". | FR-22 |
| Submission type | How the student hands the work in, such as a file upload or on paper, from Canvas's `submission_types`. How each type is written on a card is in the [UI specification's S-4](04-ui-specification.md#s-4-board-home-screen). | FR-23 |

## Screen words

| Term | Meaning | Defined in |
|------|---------|------------|
| Screen ID | An ID for each screen, such as `S-4` for the board. | [UI specification](04-ui-specification.md) |
| Button ID | A name for a button in capitals with underscores, such as `REFRESH`, used in logs, docs, code, and tests. The full list is in the [UI specification's conventions](04-ui-specification.md#conventions-on-every-screen). | UI specification |
| Label | A button's name in plain words, such as "Refresh from Canvas". Screen readers announce it, and icon buttons have no other name. | UI specification |
| Dialog (modal) | A box that opens over the page and must be closed before using the page behind it, like a QML `Dialog`. The card back *(Phase 5)* is one. | S-5 |

## Document terms

| Term | Meaning |
|------|---------|
| Phase | A stage of the [roadmap](01-roadmap.md), from Phase 0 (decisions and setup) to Phase 4 (polish and deploy). Phase 5 holds later ideas that aren't committed. The current phase is set in [CLAUDE.md](../../CLAUDE.md). |
| Future feature | A Phase 5 idea. The docs may sketch it, but nobody builds it until the Team Lead plans it into a phase. |
| Requirement ID | `FR-` for a functional requirement (what the app does) and `NFR-` for a non-functional one (how well it does it), in the [requirements](02-requirements.md). |
| Must, Should, Could | A requirement's priority: required for its phase, expected but not blocking, or nice to have. |
| Other IDs | `G-` a goal and `D-` a decision (roadmap); `A-` an assumption, `C-` a constraint, and `Q-` an open question (requirements); `S-` a screen (UI specification); `TP-` a test procedure (test plan). |
| Traceability | The chain from each requirement to the design part that builds it and the test that checks it, by requirement ID. |

## Team process

| Term | Meaning |
|------|---------|
| Team Lead | The project owner. Has the final say on every decision, and is the only one who approves or merges a PR. |
| Persona | A role an agent takes on, such as UI/UX or Security, with its own area and review checklist. The list is in the [team README](../../team/README.md). |
| Owner | The persona that writes a piece of work and answers its findings. |
| Recommended, optional, and confirmed reviewers | Who the [review protocol](../../team/review-protocol.md#who-reviews-what) suggests for a PR, who joins when the change touches their area, and who the Team Lead keeps. |
| Cross-review | A review where each confirmed reviewer runs in its own fresh thread. |
| Finding | One problem a reviewer raises, with an ID such as `F-1`, or `X-1` when the fix is in another doc. |
| Verdict | A reviewer's sign-off: Recommend, Recommend with notes, or Changes needed. |
| Potential data breach | A finding that could expose a token, a session, or a student's data to anyone else. Always critical and must-fix. |
| Team board | The shared file where threads claim work and leave handoff notes, as the [team workspace](../../team/workspace.md#the-board) says. Not the portal's board. |
| Follow-up issue | A GitHub issue for work a review uncovered outside the PR, labeled with its persona and `needs-triage` until Management triages it. |
| `backlog` label | An issue label for work that's useful but not planned into a phase. Not the Backlog list. |

## Web terms

These come up often in the docs. Each has a Qt comparison where one helps.

| Term | Meaning |
|------|---------|
| Frontend | The code that runs in the browser and draws the page. Comparable to the QML layer of a Qt app. |
| Backend | A program that runs on a server, not in the browser. Comparable to the C++ side of a Qt app, but on another machine reached over the network. |
| API | A set of URLs a program can call to get or change data. Canvas has a REST API: you request `https://school.instructure.com/api/v1/courses` and get JSON back. |
| JSON | The text format APIs use for data, like `{"name": "Biology", "id": 42}`. |
| REST | A common style of API where each URL is a thing (a course, an assignment) and HTTP verbs say what to do with it: `GET` reads, `POST` creates, `PUT`/`PATCH` changes, `DELETE` removes. |
| CORS | "Cross-Origin Resource Sharing". A browser rule: a page from site A may only call site B's API if site B explicitly allows it. Canvas does not allow arbitrary sites, which is why this project needs its own backend. |
| Access token | A long secret string that acts like a password for an API. Canvas lets a user generate a *personal access token* in their account settings. |
| OAuth | The "Log in with ..." flow. The user signs in on Canvas itself and Canvas hands the app a token. Needs the school to register the app. |
| Local storage | A small key-value store inside the browser, private to one site on one device. Like `QSettings`, but per browser. |
| Database | Structured storage on the server, shared across the user's devices. SQLite (one file) or Postgres (a database server). |
| Kanban | A board of columns (such as To do, Doing, Done) with cards you drag between them. The portal's [board](#the-board) is one. |
| Component | A reusable piece of UI, like a QML component file. React and Svelte are both built around components. |
| Deploy / hosting | Putting the app on a server on the internet so others can open it. |
| CI | "Continuous integration": GitHub Actions running builds and tests on every push. |

## Change log

| Date | Change |
|------|--------|
| 2026-10-26 | Created from the README's "Web terms used in these docs" table, from the Team Lead's review of PR #8. Added the board (including orphaned cards, from the Team Lead's review of PR #8), Refresh, card status, screen, document, and team process terms. |
