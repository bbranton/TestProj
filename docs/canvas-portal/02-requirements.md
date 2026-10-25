# Requirements

**Status:** Draft · **Owner:** Team Lead · **Last updated:** 2026-10-25

## 1. Purpose and scope

This document lists what the Canvas Assignments Portal must do (*functional
requirements*, `FR`) and how well it must do it (*non-functional
requirements*, `NFR`). Each requirement has an ID that the design and test
documents refer back to.

**In scope:** reading a student's courses and assignments from Canvas,
showing them, arranging them on a kanban board that looks and behaves like
Trello (goal G-3 in the [roadmap](01-roadmap.md#1-project-goals)), and keeping
private notes.

This document uses Trello's words where they apply: a **board** holds
**lists** (the columns), lists hold **cards**, and opening a card shows its
**card back** (the detailed view). Earlier requirements say "column"; it
means the same as list.

**Out of scope:** submitting work, changing anything in Canvas, teacher or
admin features, grades analytics (possibly Phase 5).

### Priority and phase

- **Must**: required for the phase to be done.
- **Should**: expected, but the phase can ship without it.
- **Could**: nice to have.

The *Phase* column matches the [roadmap](01-roadmap.md).

## 2. Users

| User | Description | Main goal |
|------|-------------|-----------|
| Student | Enrolled in one or more Canvas courses at a school | See everything due and plan their work |
| Parent (observer) | A Canvas *observer* account linked to one or more students; sees their courses and assignments with limited access | Keep track of a student's work (Phase 5, see Q-5) |
| Developer (Team Lead) | Builds and runs the portal | Test against real and sample Canvas data |

## 3. Assumptions and constraints

- **A-1** The student can create a Canvas personal access token at their
  school (*Account → Settings → Approved Integrations → New Access Token*).
  Some schools disable this; see risk R-1. The Team Lead's school allows it, and
  the Team Lead has a student token and a parent (observer) token for testing.
- **A-2** Each school has its own Canvas address, such as
  `https://myschool.instructure.com`, so the address is a user setting.
- **A-3** Test tokens are real credentials. They are kept out of the
  repository, chat, and screenshots, and are loaded from a local file that git
  ignores.
- **C-1** Browsers block pages from calling the Canvas API directly from
  another site (CORS, see the [glossary](README.md#web-terms-used-in-these-docs)).
  All Canvas calls go through the portal's backend.
- **C-2** Canvas returns long lists in pages (for example 10 to 100 items at a
  time) and limits how fast one token can make requests. The backend must
  follow page links and back off when limited.
- **C-3** The portal uses only Canvas *read* endpoints.
- **C-4** "Like Trello" means Trello's layout, interactions, and keyboard
  habits. The portal does not use the Trello name or logo, Trello's icons,
  illustrations, or fonts, or copy Trello's stylesheets. Colors and icons are
  our own, chosen to give a similar feel. (Trello is a trademark of
  Atlassian.)

## 4. Functional requirements

### 4.1 Connecting to Canvas

| ID | Requirement | Priority | Phase |
|----|-------------|----------|-------|
| FR-1 | The user can enter their school's Canvas address and a personal access token. | Must | 1 |
| FR-2 | The portal checks the token by fetching the user's Canvas profile and shows their name on success. | Must | 1 |
| FR-3 | The connect screen explains, with steps, how to create a token in Canvas. | Should | 1 |
| FR-4 | The user can disconnect, which removes the token from the portal. | Must | 1 |
| FR-5 | The portal remembers the connection between visits until the user disconnects. From Phase 2 the connection is stored with the user's portal account, so it works on any device they sign in from. | Should | 1 |
| FR-6 | If Canvas rejects the token (wrong, expired, or revoked), the portal says so and returns to the connect screen without losing board layout or notes. | Must | 1 |

### 4.2 Fetching data from Canvas

| ID | Requirement | Priority | Phase |
|----|-------------|----------|-------|
| FR-10 | The backend fetches the user's active course enrollments (`GET /api/v1/courses?enrollment_state=active`). | Must | 1 |
| FR-11 | The backend fetches assignments for each active course, including the user's submission status (`GET /api/v1/courses/:id/assignments?include[]=submission`). | Must | 1 |
| FR-12 | The backend follows Canvas paging so no courses or assignments are missed. | Must | 1 |
| FR-13 | The user can refresh data on demand; the page shows when data was last fetched. | Must | 1 |
| FR-14 | The backend caches Canvas responses for a short time (default 5 minutes) to stay inside rate limits. | Should | 1 |

### 4.3 Viewing courses and assignments

| ID | Requirement | Priority | Phase |
|----|-------------|----------|-------|
| FR-20 | The dashboard lists the user's active courses by name and course code. | Must | 1 |
| FR-21 | The dashboard lists assignments across all courses, sorted by due date, soonest first; assignments with no due date come last. | Must | 1 |
| FR-22 | Each assignment shows: name, course, due date and time in the user's time zone, points possible, and status. | Must | 1 |
| FR-23 | Status is shown exactly as Canvas reports it, with nothing worked out by the portal. The submission state (Canvas field `workflow_state`) is one of *Not submitted*, *Submitted*, *Graded*, or *Pending review*. Canvas's own *Late*, *Missing*, and *Excused* flags (fields `late`, `missing`, `excused`) show as separate tags, because they can apply at the same time as a state, such as Graded and Late. | Must | 1 |
| FR-27 | Statuses the portal works out by combining Canvas fields or comparing with the clock, such as *Upcoming*, *Due soon* (for example within 48 hours, with a yellow badge), and *Overdue*. They need clear rules for cases that overlap. | Could | 5 |
| FR-28 | The card back shows the assignment's description (its instructions) exactly as Canvas has it, with Canvas's formatting. It is read only: the portal never edits it, and it is not a note. | Must | 2 |
| FR-24 | The user can filter by course, by Canvas submission state and flags (FR-23), and search by assignment name. | Should | 1 |
| FR-25 | The user can hide assignments, for example those Canvas reports as *Graded* or *Excused*. | Could | 5 |
| FR-26 | Each assignment links to its page in Canvas, opening in a new tab. | Must | 1 |

### 4.4 Kanban board

| ID | Requirement | Priority | Phase |
|----|-------------|----------|-------|
| FR-30 | *(Removed: there is no table view; the board is the only view. From the Team Lead's review.)* | n/a | n/a |
| FR-31 | The board has four lists, in this order: *Backlog*, *To do*, *In progress*, *Done*. *Backlog* holds Canvas assignments the student hasn't sorted yet. | Must | 2 |
| FR-32 | The user can drag a card to another list. Cards cannot be reordered by hand within a list (FR-38). | Must | 2 |
| FR-33 | The board layout (which list each card is in) is saved and restored on the next visit. | Must | 2 |
| FR-34 | Assignments that are new since the last visit appear in *Backlog*, in their due date place (FR-38). When the board is first created, every assignment starts in *Backlog*. | Must | 2 |
| FR-38 | Within every list, assignments are always sorted by due date, earliest at the top. Assignments with no due date come last, then by name. A card dropped into a list slots into its due date place, and a changed due date in Canvas moves the card to its new place. | Must | 1 (table), 2 (board) |
| FR-35 | Cards are matched to assignments by Canvas assignment ID, so a renamed or rescheduled assignment keeps its place. | Must | 2 |
| FR-36 | The user can archive a list, as in Trello. Its cards go with it and can be restored together. | Could | 5 |
| FR-37 | *(Removed: no "Move to Done?" hint. The student drags cards to Done; the due badge turning green already shows the assignment is submitted, FR-65.)* | n/a | n/a |

### 4.5 Trello-style look and behavior (goal G-3)

| ID | Requirement | Priority | Phase |
|----|-------------|----------|-------|
| FR-60 | The board is the home screen and the only view, as a Trello board is. In Phase 1 it is read only: every card sits in Backlog and cannot be dragged. | Must | 1 (read only), 2 |
| FR-61 | Lists sit side by side at a fixed width and the board scrolls sideways. Dragging empty board background also scrolls it. | Must | 2 |
| FR-62 | The user can drag a list by its header to reorder the lists. | Could | 5 |
| FR-63 | Clicking a list title edits it in place. Enter or clicking away saves, and Escape cancels. | Could | 5 |
| FR-64 | An "+ Add another list" control after the last list adds a list. | Could | 5 |
| FR-65 | Card fronts show: the course as a colored label strip, the title, and badges for the due date, the number of notes (FR-43), and, from Phase 5, checklist progress (FR-70). The due date badge is green when Canvas reports *Submitted* or *Graded*, red when Canvas flags it *Missing*, and plain otherwise. Yellow for *Due soon* comes with FR-27 in Phase 5. | Must | 1 |
| FR-66 | Each course gets a label color automatically. The user can change a course's color and name its label. | Should | 2 |
| FR-67 | Clicking a card opens its card back in a dialog over the board, which stays visible behind it. The browser address changes to the card's own link, so reloading or sharing the link reopens the card, and Back closes it. | Must | 2 |
| FR-68 | The card back shows: the title; "in list *name*" (clicking it moves the card); labels; due date; points and status; an "Open in Canvas" button; *Description*, from Canvas and read only (FR-28); *Notes*, private (FR-40); and *Archive*. Checklists are added in Phase 5 (FR-70). | Must | 2 (3 for notes) |
| FR-69 | Hovering a card shows an edit (pencil) button; it and right-click open a quick edit menu: Open card, Move, Change label color, Open in Canvas, Archive. | Could | 5 |
| FR-70 | A card back can hold one or more checklists of items that can be checked off. The card front shows progress such as 2/5 (2 of 5 items done). | Could | 5 |
| FR-71 | "+ Add a card" at the bottom of each list creates a personal card that isn't a Canvas assignment. It supports everything a card back has except the Canvas details. | Could | 5 |
| FR-72 | A Filter button at the start of the course button row (FR-78), under the header, opens a menu that filters cards by course, by due date (due date passed, due in the next day, next week, next month, no due date), by Canvas submission state and flags (FR-23), and by keyword. When a filter is on, the course row says so and offers "Clear". | Must | 2 |
| FR-73 | Keyboard shortcuts follow Trello's where the action exists, including: arrow keys move between cards, Enter opens a card, Escape closes, `f` filter, `x` clear filters, `?` shows the shortcut list. The final list is checked against Trello's own shortcut page during design. | Should | 2 |
| FR-74 | Archived cards (and, from Phase 5, lists) are found under "Archived items" in the board menu, where they can be restored. | Must | 2 |
| FR-75 | A board menu opens as a panel from the right edge with: board background color, labels, archived items. | Could | 5 |
| FR-76 | The user can have more than one board. | Could | 5 |
| FR-77 | Dragging feels like Trello: the card tilts slightly and lifts while dragged, the list under it is highlighted and a gray gap shows the due date spot where it will land, and the board scrolls when the card nears an edge. | Should | 2 |
| FR-78 | Between the header and the board, a row of show/hide buttons has one button per active course, in the course's label color. Tapping a button hides or shows that course's cards; "Show all" and "Hide all" buttons show or hide every course at once. When every course is hidden, the board says so and offers Show all. Hidden cards keep their list. From Phase 2 the choice is saved with the user's account so it follows them between devices. | Must | 1 (2 for saving) |
| FR-79 | Help the student see which assignments are new or have changed in Canvas (for example a new due date or new instructions) since they last looked, such as with a badge on the card and a way to clear it. | Could | 5 |

### 4.6 Private notes

| ID | Requirement | Priority | Phase |
|----|-------------|----------|-------|
| FR-40 | The user can add any number of plain-text notes to an assignment, like comments on a Trello card. Each note is stamped with the date and time it was added, and the card back lists them newest first. Notes are separate from the Canvas description (FR-28). | Must | 3 |
| FR-41 | The user can edit or delete each note. An edited note keeps its original date and says "(edited)". Deleting asks for confirmation first. | Must | 3 |
| FR-42 | A note is saved when the user presses Save or Ctrl+Enter. If saving fails, the text stays in the box; closing the card with unsaved text warns first. | Must | 3 |
| FR-43 | A card with notes shows a badge with the number of notes; opening the card shows them all. | Must | 3 |
| FR-44 | Notes are never sent to Canvas. | Must | 3 |
| FR-45 | If an assignment disappears from Canvas, its card and notes move to an *Archived* area rather than being deleted. | Should | 3 |
| FR-46 | Notes support simple formatting (bold, lists, links). | Could | 3 |

### 4.7 Accounts, sync, and data control

| ID | Requirement | Priority | Phase |
|----|-------------|----------|-------|
| FR-50 | The user can sign in to the portal so their board and notes are tied to them on the server. | Must | 2 |
| FR-51 | Board and notes stored on the server appear on any device where the user signs in. | Must | 2 |
| FR-52 | *(Removed: board and notes are on the server from the start, so there is no browser data to import.)* | n/a | n/a |
| FR-53 | The user can export their board and notes as a JSON file. | Should | 4 |
| FR-54 | The user can delete all their data from the portal. | Must | 4 |
| FR-55 | A student can connect more than one school (more than one Canvas address and token), for example a high school and a community college during dual enrollment. Courses from every school appear on the same board, and each course button and card shows which school it comes from. | Could | 5 |

## 5. Non-functional requirements

### 5.1 Performance

| ID | Requirement | Phase |
|----|-------------|-------|
| NFR-1 | With cached data, the dashboard is usable within 2 seconds of opening. | 1 |
| NFR-2 | For an account with 8 courses and 200 assignments, a full refresh from Canvas completes within 15 seconds, with courses appearing as they arrive. | 1 |
| NFR-3 | Dragging a card responds within 100 ms. | 2 |

### 5.2 Security and privacy

| ID | Requirement | Phase |
|----|-------------|-------|
| NFR-10 | The Canvas token is never written to logs, error messages, or the page's address (URL). | 1 |
| NFR-11 | If the token is stored on the server it is encrypted at rest; all traffic uses HTTPS. | 1 |
| NFR-12 | Notes and board data are visible only to the user who created them. | 3 |
| NFR-13 | The portal calls only Canvas read (`GET`) endpoints. | 1 |
| NFR-14 | Student data is handled with care for privacy rules such as FERPA (US student records law): no analytics or third-party trackers that see course data. | 1 |

### 5.3 Reliability

| ID | Requirement | Phase |
|----|-------------|-------|
| NFR-20 | When Canvas is slow, down, or rate limiting, the page shows a clear message and the last cached data rather than an empty screen. | 1 |
| NFR-21 | No user action or Canvas change can silently delete a note. | 3 |

### 5.4 Usability and accessibility

| ID | Requirement | Phase |
|----|-------------|-------|
| NFR-30 | Works in current Chrome, Firefox, Safari, and Edge. | 1 |
| NFR-31 | Every action, including moving cards, can be done with the keyboard alone. | 2 |
| NFR-32 | Meets WCAG 2.2 level AA (the standard web accessibility guideline) for contrast, labels, and focus. | 4 |
| NFR-33 | Usable on a phone-width screen. As in Trello's mobile layout, one list fills the screen and the user swipes between lists. | 4 |
| NFR-34 | Visual style is close to Trello's within C-4: a colored board background, light gray lists with rounded corners, white cards with rounded corners and a soft shadow, and compact text. | 2 |
| NFR-35 | Board actions (open a card, show or hide a course, filter) need no more clicks than the same action in Trello. | 2 |

### 5.5 Maintainability

| ID | Requirement | Phase |
|----|-------------|-------|
| NFR-40 | Frontend and backend each have automated tests that run in CI on every pull request. | 0 |
| NFR-41 | The backend can run against recorded sample Canvas data, so tests don't need a real account. | 1 |
| NFR-42 | A new developer can run the app locally by following the README in under 15 minutes. | 0 |

## 6. Open questions

- **Q-1** Does the Team Lead's school allow personal access tokens? (Blocks Phase 1; see R-1.)
- **Q-2** When *Due soon* is added (FR-27, Phase 5), should it be 48 hours, or configurable?
- **Q-3** Should discussion posts and quizzes appear alongside assignments? Canvas exposes them as assignments in most cases, so the default is yes.
- ~~**Q-4** Is multi-device sync wanted, or is one browser enough?~~ Answered: yes, the user signs in from anywhere and sees their saved state (D-2).
- **Q-5** Should the portal support parent (observer) tokens? Canvas returns observed students' data through different options, so the views would need a student picker. Proposed for Phase 5.
- ~~**Q-6** Should personal cards (FR-71) come in Phase 3, or wait until later?~~ Answered: later. Students don't need to create their own cards or lists yet, so FR-64 and FR-71 are Phase 5 future features.

## Change log

| Date | Change |
|------|--------|
| 2026-10-25 | First draft. |
| 2026-10-25 | Server storage decided: FR-50 and FR-51 move to Phase 2, FR-52 removed. Added parent (observer) user, test tokens under A-1, A-3 token handling, Q-5. |
| 2026-10-25 | Trello goal (G-3): added Trello terms, constraint C-4, FR-60 to FR-77, NFR-34, NFR-35, Q-6. FR-30 and FR-36 changed, NFR-33 now follows Trello's phone layout. |
| 2026-10-25 | Added FR-78, course show/hide buttons, from the Team Lead's review. |
| 2026-10-25 | FR-78 gains Hide all. |
| 2026-10-25 | FR-37 ("Move to Done?" hint) removed, from the Team Lead's review. |
| 2026-10-25 | Checklists (FR-70) moved to Phase 5, ideas for later, from the Team Lead's review. |
| 2026-10-25 | FR-36, FR-64, and FR-71 (archive lists, add lists, add personal cards) moved to Phase 5; `n` shortcut dropped; Q-6 answered. From the Team Lead's review. |
| 2026-10-25 | Added FR-38: cards are always sorted by due date, earliest first, in every list and the table. FR-32, FR-33, FR-34, and FR-77 changed to match: no hand reordering within a list. From the Team Lead's review. |
| 2026-10-25 | Quick edit menu (FR-69) and its `e` shortcut moved to Phase 5, from the Team Lead's review. |
| 2026-10-25 | Added a *Backlog* list before *To do* for new, unsorted Canvas assignments (FR-31, FR-34), from the Team Lead's review. |
| 2026-10-25 | NEW badge removed from FR-34; added FR-79 (show new and updated assignments) as a Phase 5 future feature, from the Team Lead's review. |
| 2026-10-25 | *Due soon* status moved out of FR-23 into new FR-27, a Phase 5 future feature, from the Team Lead's review. |
| 2026-10-25 | FR-23 now shows only statuses that map to a single Canvas field (submission state plus Late, Missing, Excused flags). Upcoming and Overdue join Due soon in FR-27 as Phase 5 future features. FR-24, FR-25, FR-65, and FR-72 updated to match. From the Team Lead's review. |
| 2026-10-25 | Hiding assignments (FR-25) moved to Phase 5, from the Team Lead's review. |
| 2026-10-25 | FR-72: the Filter button sits in the course button row, not the header. |
| 2026-10-25 | FR-72 filters by course; the UI says "course", not "label". |
| 2026-10-25 | Notes are now dated, comment-style entries, any number per card (FR-40 to FR-43); new FR-28 shows the Canvas description read only. From the Team Lead's review. |
| 2026-10-25 | Renaming and reordering lists (FR-62, FR-63) moved to Phase 5, from the Team Lead's review. |
| 2026-10-25 | Added FR-55 (more than one school per student) as a Phase 5 future feature, from the Team Lead's review. |
| 2026-10-25 | Table view removed (FR-30); the board is the only view and appears read only in Phase 1 (FR-60, FR-65, FR-78). From the Team Lead's review. |
