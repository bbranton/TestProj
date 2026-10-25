# Requirements

**Status:** Draft · **Owner:** Team Lead · **Last updated:** 2026-10-25

## 1. Purpose and scope

This document lists what the Canvas Assignments Portal must do (*functional
requirements*, `FR`) and how well it must do it (*non-functional
requirements*, `NFR`). Each requirement has an ID that the design and test
documents refer back to.

**In scope:** reading a student's courses and assignments from Canvas,
showing them, arranging them on a kanban board that looks and behaves like
Trello (goal G-3 in the [roadmap](01-roadmap.md#1-project-goals)), keeping
it current with Canvas, and, as a future feature, keeping private notes.

This document uses Trello's words where they apply: a **board** holds
**lists** (the columns), lists hold **cards**, and opening a card shows its
**card back** (the detailed view).

**Out of scope:** submitting work, changing anything in Canvas, teacher or
admin features, grades analytics (possibly Phase 5).

Requirements say *what* the portal does, not *how*. Canvas endpoints,
tables, and component choices are in the [design](03-design.md); a
requirement names one only where it sets the scope.

### Requirements by goal

Every requirement serves one of the project goals in the
[roadmap](01-roadmap.md#1-project-goals), except the maintainability
requirements, which serve the developer, and the two listed under *No goal yet*.

| Goal | Requirements |
|------|--------------|
| G-1 One place for everything due | FR-1 to FR-3, FR-6, FR-10 to FR-16, FR-20 to FR-29, FR-31, FR-34, FR-38, FR-39, FR-45, FR-55, FR-79, NFR-1, NFR-2, NFR-4, NFR-20; notes FR-40 to FR-43, FR-46 |
| G-2 Read only toward Canvas | C-3, FR-28, FR-44, NFR-13 |
| G-3 Feels like Trello | FR-32, FR-36, FR-60 to FR-80, NFR-3, NFR-33 to NFR-36 |
| G-4 Follows the student everywhere | FR-5, FR-33, FR-35, FR-50, FR-51, FR-53, NFR-22 |
| G-5 Private and safe | FR-4, FR-54, NFR-10 to NFR-14, NFR-21 |
| No goal yet | NFR-30 (browsers), NFR-32 (accessibility): no roadmap goal says the portal works for every student whatever their browser or ability. See Q-11. |
| Developer | NFR-40 to NFR-42 |

### Priority and phase

- **Must**: required for the phase to be done.
- **Should**: expected, but the phase can ship without it.
- **Could**: nice to have.
- **—**: Phase 5 ideas have no priority until they are planned into a phase.

Non-functional requirements have no priority column: each one is required
for its phase to be done.

The *Phase* column matches the [roadmap](01-roadmap.md).

### Requirements by phase

This index lists every requirement by the phase that builds it, so it's
clear what is in scope at any time. Build only the requirements listed for
the current phase, which the repo's [CLAUDE.md](../../CLAUDE.md) names.
Anything listed for a later phase is out of scope, even where the design or
the User Interface Specification already describes it. When a
requirement's *Phase* column changes, update this index in the same PR.
Removed requirements are not listed.

**Phase 0: Decisions and setup**

- Maintainability: NFR-40, NFR-42

**Phase 1: Read-only viewer**

- Connecting to Canvas: FR-1, FR-2, FR-3, FR-4, FR-5, FR-6
- Fetching data from Canvas: FR-10, FR-11, FR-12, FR-13, FR-14, FR-15, FR-16
- Viewing courses and assignments: FR-20, FR-21, FR-22, FR-23, FR-26
- Kanban board: FR-31, FR-34, FR-35, FR-38, FR-45 (keeping cards of removed assignments)
- Trello-style look and behavior: FR-60 (read only), FR-61, FR-65, FR-66, FR-78, FR-80
- Accounts, sync, and data control: FR-50
- Performance: NFR-1
- Security and privacy: NFR-10, NFR-11, NFR-12, NFR-13, NFR-14
- Reliability: NFR-20
- Usability and accessibility: NFR-30, NFR-34
- Maintainability: NFR-41

**Phase 2: Dragging and sync**

- Kanban board: FR-32, FR-33, FR-38 (dropping into the due date place)
- Trello-style look and behavior: FR-60 (dragging), FR-77, FR-80 (dropping on a minimized list)
- Accounts, sync, and data control: FR-51
- Performance: NFR-3
- Reliability: NFR-22

**Phase 3: Performance and Canvas sync**

- Kanban board: FR-39, FR-45 (archiving)
- Performance: NFR-2

**Phase 4: Polish and deploy**

- Accounts, sync, and data control: FR-54
- Usability and accessibility: NFR-32

**Phase 5: Later ideas (not committed)**

- Viewing courses and assignments: FR-24, FR-25, FR-27, FR-28, FR-29
- Kanban board: FR-36
- Trello-style look and behavior: FR-62, FR-63, FR-64, FR-66 (changing colors), FR-67, FR-68, FR-69, FR-70, FR-71, FR-72, FR-74, FR-75, FR-76, FR-78 (saving the choice), FR-79
- Private notes: FR-40, FR-41, FR-42, FR-43, FR-44, FR-46
- Accounts, sync, and data control: FR-53, FR-55
- Performance: NFR-4
- Reliability: NFR-21
- Usability and accessibility: NFR-33, NFR-35, NFR-36

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
- **C-4** "Like Trello" means Trello's layout and interactions. The portal does not use the Trello name or logo, Trello's icons,
  illustrations, or fonts, or copy Trello's stylesheets. Colors and icons are
  our own, chosen to give a similar feel. (Trello is a trademark of
  Atlassian.)

## 4. Functional requirements

### 4.1 Connecting to Canvas

| ID | Requirement | Priority | Phase |
|----|-------------|----------|-------|
| FR-1 | The user can enter their school's Canvas address and a personal access token. If the address can't be reached, the portal says so and keeps what the user typed. | Must | 1 |
| FR-2 | The portal checks the token by fetching the user's Canvas profile and shows their name on success. | Must | 1 |
| FR-3 | The connect screen explains, with steps, how to create a token in Canvas. | Should | 1 |
| FR-4 | The user can disconnect, which removes the token from the portal. The board is kept, so reconnecting the same Canvas account brings it back (see Q-8 for a different account). | Must | 1 |
| FR-5 | The portal remembers the connection between visits until the user disconnects. The connection is stored with the user's portal account, so it works on any device they sign in from. | Must | 1 |
| FR-6 | If Canvas rejects the token (wrong, expired, or revoked), the portal shows a message saying the token no longer works and returns to the connect screen without losing the board layout. | Must | 1 |

### 4.2 Fetching data from Canvas

| ID | Requirement | Priority | Phase |
|----|-------------|----------|-------|
| FR-10 | The portal fetches the courses in which the user's Canvas enrollment is active. Ended (concluded) courses are not fetched. | Must | 1 |
| FR-11 | The portal fetches the assignments of each active course, with the user's own submission for each, from Canvas's assignments list (the design names the endpoint). No other kinds of course item, such as ungraded discussions, pages, or announcements, are fetched. Graded quizzes and graded discussions that Canvas returns in this same list show as ordinary assignments. | Must | 1 |
| FR-12 | The portal follows Canvas paging so no courses or assignments are missed. | Must | 1 |
| FR-13 | The user can refresh data on demand. The header always shows the date and time of the last complete Refresh, such as "Synced Oct 25, 10:42 AM". | Must | 1 |
| FR-14 | The portal keeps the last complete copy of the student's Canvas data and shows it on every load, so opening the board never waits on Canvas. | Must | 1 |
| FR-15 | The portal fetches from Canvas only when the student selects Refresh, or on the very first load when there is no data yet. It never starts a fetch on its own. When the data is more than an hour old, the Refresh button is highlighted. | Must | 1 |
| FR-16 | Every Refresh, including the first load, shows its progress: how many courses are done out of the total, and for each course whether it is waiting, being fetched, waiting on a Canvas rate limit, done (with its number of assignments), or failed (with the reason, such as a timeout or an error from Canvas). When the Refresh ends, a summary says what was synced; if anything failed, it says the previous data was kept and offers Retry. The log of the last Refresh can be reopened until the next one starts. | Must | 1 |

### 4.3 Viewing courses and assignments

| ID | Requirement | Priority | Phase |
|----|-------------|----------|-------|
| FR-20 | The board lists the user's active courses by name and course code. If the user has no active courses, or no assignments, the board says so instead of showing empty lists. | Must | 1 |
| FR-21 | The board shows the assignments of every active course together, in the order FR-38 sets. | Must | 1 |
| FR-22 | Each assignment shows: name, course, due date and time in the time zone of the device being used, points possible, and status. The due date is the one Canvas gives this student, including a date set just for them (a Canvas *override*). | Must | 1 |
| FR-23 | Status is shown exactly as Canvas reports it, with nothing worked out by the portal. The submission state (Canvas field `workflow_state`) is one of *Not submitted*, *Submitted*, *Graded*, or *Pending review*. Canvas's own *Late*, *Missing*, and *Excused* flags (fields `late`, `missing`, `excused`) show as separate tags, because they can apply at the same time as a state, such as Graded and Late. | Must | 1 |
| FR-24 | The user can filter by course, by Canvas submission state and flags (FR-23), and search by assignment name. | — | 5 |
| FR-25 | The user can hide assignments, for example those Canvas reports as *Graded* or *Excused*. | — | 5 |
| FR-26 | Each assignment links to its page in Canvas, opening in a new tab. | Must | 1 |
| FR-27 | Statuses the portal works out by combining Canvas fields or comparing with the clock, such as *Upcoming*, *Due soon* (for example within 48 hours, with a yellow badge), and *Overdue*. They need clear rules for cases that overlap. | — | 5 |
| FR-28 | The card back shows the assignment's description (its instructions) exactly as Canvas has it, with Canvas's formatting. It is read only: the portal never edits it, and it is not a note. | — | 5 |
| FR-29 | Quizzes and discussions as their own kinds of item, such as ungraded discussions and quiz details, with their own badges. Until then, only assignments are fetched (FR-11). | — | 5 |

### 4.4 Kanban board

| ID | Requirement | Priority | Phase |
|----|-------------|----------|-------|
| FR-30 | *(Removed: there is no table view; the board is the only view. From the Team Lead's review.)* | n/a | n/a |
| FR-31 | The board has four lists, in this order: *Backlog*, *To do*, *In progress*, *Done*. *Backlog* holds Canvas assignments the student hasn't sorted yet. | Must | 1 |
| FR-32 | The user can drag a card to another list. Cards cannot be reordered by hand within a list (FR-38). | Must | 2 |
| FR-33 | The board layout (which list each card is in) is saved and restored on the next visit. | Must | 2 |
| FR-34 | Assignments that are new since the last complete Refresh appear in *Backlog*, in their due date place (FR-38). When the board is first created, every assignment starts in *Backlog*. | Must | 1 |
| FR-35 | Cards are matched to assignments by Canvas assignment ID, so a renamed or rescheduled assignment keeps its place, and each assignment has exactly one card, even when two devices load the board at the same moment. | Must | 1 |
| FR-36 | The user can archive a list, as in Trello. Its cards go with it and can be restored together. | — | 5 |
| FR-37 | *(Removed: no "Move to Done?" hint. The student drags cards to Done; the due badge turning green already shows the assignment is submitted, FR-65.)* | n/a | n/a |
| FR-38 | Within every list, assignments are always sorted by due date, earliest at the top, and assignments with no due date come last. Cards with the same due date, and cards with no due date, are in name order. A changed due date in Canvas moves the card to its new place. From Phase 2, a card dropped into a list slots into its due date place. | Must | 1, 2 (dropping) |
| FR-39 | When a field changes in Canvas, the card shows the new value after the next refresh, and never changes list because of it. This covers a field being added later (such as a due date set after the assignment was created), changed, or cleared (such as a due date removed: the card moves to the end of its list with no due date). It applies to the name, due date, points, submission state, and the late, missing, and excused flags (and, once the card back shows it, the description, FR-28), including a state going backward (for example graded back to submitted after a resubmission). | Must | 3 |
| FR-45 | If an assignment disappears from Canvas (deleted or unpublished by the teacher), its card is marked archived rather than deleted, and leaves the board. Only a complete, successful refresh can archive a card; a failed or partial fetch changes nothing. If the assignment comes back (republished), the card returns to its old list. Viewing and restoring archived cards by hand comes with FR-74. Until Phase 3, a card whose assignment is missing from the last complete copy of Canvas data (FR-14) is not shown, but it is kept, never deleted. | Must | 1 (keeping cards), 3 (archiving) |

### 4.5 Trello-style look and behavior (goal G-3)

| ID | Requirement | Priority | Phase |
|----|-------------|----------|-------|
| FR-60 | The board is the home screen and the only view, as a Trello board is. In Phase 1 it is read only: every card sits in Backlog and cannot be dragged. | Must | 1 (read only), 2 (dragging) |
| FR-61 | Lists sit side by side and share the board's width (FR-80). If the window is too narrow for every expanded list to be at least 240 px wide, the board scrolls sideways; dragging empty board background also scrolls it. | Must | 1 |
| FR-62 | The user can drag a list by its header to reorder the lists. | — | 5 |
| FR-63 | Clicking a list title edits it in place. Enter or clicking away saves, and Escape cancels. | — | 5 |
| FR-64 | An "+ Add another list" control after the last list adds a list. | — | 5 |
| FR-65 | Card fronts show: the course as a colored label strip, the title, a due date badge, the points, and the Canvas status from FR-23 (the state and any Late, Missing, or Excused tags), so every field in FR-22 is visible before the card back exists. Phase 5 ideas add a note count (FR-43) and checklist progress (FR-70). The due date badge is red when Canvas flags it *Missing*, otherwise green when Canvas reports *Submitted* or *Graded*, and plain otherwise. Red wins because a teacher can mark a graded assignment missing. Yellow for *Due soon* comes with FR-27 in Phase 5. | Must | 1 |
| FR-66 | Each course gets a label color automatically, used on its cards and its course button. From Phase 5 the user can change a course's color and name its label. | Should | 1, 5 (changing colors) |
| FR-67 | Clicking a card opens its card back in a dialog over the board, which stays visible behind it. The browser address changes to the card's own link, so reloading or sharing the link reopens the card, and Back closes it. | — | 5 |
| FR-68 | The card back shows: the title; "in list *name*" (clicking it moves the card); labels; due date; points and status; an "Open in Canvas" button; *Description*, from Canvas and read only (FR-28); *Notes*, private (FR-40); and *Archive*. Checklists are added in Phase 5 (FR-70). | — | 5 |
| FR-69 | An edit (pencil) button on each card (shown on hover on desktop, always shown on touch screens), right-click, or a long press opens a quick edit menu: Open card, Move, Change label color, Open in Canvas, Archive. | — | 5 |
| FR-70 | A card back can hold one or more checklists of items that can be checked off. The card front shows progress such as 2/5 (2 of 5 items done). | — | 5 |
| FR-71 | "+ Add a card" at the bottom of each list creates a personal card that isn't a Canvas assignment. It supports everything a card back has except the Canvas details. | — | 5 |
| FR-72 | A Filter button at the start of the course button row (FR-78), under the header, opens a menu that filters cards by course, by due date (due date passed, due in the next day, next week, next month, no due date), by Canvas submission state and flags (FR-23), and by keyword. When a filter is on, the course row says so and offers "Clear". | — | 5 |
| FR-73 | *(Removed: no keyboard shortcuts. From the Team Lead's review.)* | n/a | n/a |
| FR-74 | Archived cards and lists are found under "Archived items" in the board menu, where they can be restored. | — | 5 |
| FR-75 | A board menu opens as a panel from the right edge with: board background color, labels, archived items. | — | 5 |
| FR-76 | The user can have more than one board. | — | 5 |
| FR-77 | Dragging feels like Trello: the card tilts slightly and lifts while dragged, the list under it is highlighted and a gray gap shows the due date spot where it will land, and the board scrolls when the card nears an edge. | Should | 2 |
| FR-78 | Between the header and the board, a row of show/hide buttons has one button per active course, in the course's label color. Tapping a button hides or shows that course's cards; "Show all" and "Hide all" buttons show or hide every course at once. When every course is hidden, the board says so and offers Show all. Hidden cards keep their list. Until Phase 5 the choice is kept in the browser, so it survives a reload on that device; from Phase 5 it is saved with the user's account so it follows them between devices. | Must | 1, 5 (saving the choice) |
| FR-79 | Help the student see which assignments are new or have changed in Canvas (for example a new due date or new instructions) since they last looked, such as with a badge on the card and a way to clear it. | — | 5 |
| FR-80 | Each list has a minimize/expand toggle in its header. A minimized list shrinks to a narrow strip showing its title and number of cards. Expanded lists share the whole width of the board and resize whenever a list is minimized or expanded. Each time the board loads or is refreshed, empty lists start minimized and the others start expanded; the minimized or expanded state is not saved. From Phase 2, dropping a card on a minimized list that is empty expands it; dropping on a minimized list that already has cards keeps it minimized and updates its count. | Must | 1, 2 (dropping) |

### 4.6 Private notes

| ID | Requirement | Priority | Phase |
|----|-------------|----------|-------|
| FR-40 | The user can add any number of plain-text notes to an assignment, like comments on a Trello card. Each note is stamped with the date and time it was added, and the card back lists them newest first. Notes are separate from the Canvas description (FR-28). | — | 5 |
| FR-41 | The user can edit or delete each note. An edited note keeps its original date and says "(edited)". Deleting asks for confirmation first. | — | 5 |
| FR-42 | A note is saved when the user presses Save. If saving fails, the text stays in the box; closing the card with unsaved text warns first. | — | 5 |
| FR-43 | A card with notes shows a badge with the number of notes; opening the card shows them all. | — | 5 |
| FR-44 | Notes are never sent to Canvas. | — | 5 |
| FR-46 | Notes support simple formatting (bold, lists, links). | — | 5 |

### 4.7 Accounts, sync, and data control

| ID | Requirement | Priority | Phase |
|----|-------------|----------|-------|
| FR-50 | The user can sign in to the portal so their Canvas connection and board (and, from Phase 5, notes) are tied to them on the server. They stay signed in on that browser between visits until they sign out, and they can sign out from any screen. | Must | 1 |
| FR-51 | The board layout stored on the server (and, from Phase 5, notes) appears on any device where the user signs in. | Must | 2 |
| FR-52 | *(Removed: board and notes are on the server from the start, so there is no browser data to import.)* | n/a | n/a |
| FR-53 | The user can export their board and notes as a JSON file. | — | 5 |
| FR-54 | The user can delete all their data from the portal. | Must | 4 |
| FR-55 | A student can connect more than one school (more than one Canvas address and token), for example a high school and a community college during dual enrollment. Courses from every school appear on the same board, and each course button and card shows which school it comes from. | — | 5 |

## 5. Non-functional requirements

### 5.1 Performance

| ID | Requirement | Phase |
|----|-------------|-------|
| NFR-1 | With saved data, the board shows every card and responds to clicks within 2 seconds of opening the portal, for an account of up to 8 courses and 200 assignments, however slow Canvas is. | 1 |
| NFR-2 | A full Refresh of the Team Lead's real account completes within a target set from the Phase 1 TP-14 baseline, with each course's progress shown as it arrives (FR-16). Until the baseline is recorded, the placeholder is 15 seconds for 8 courses and 200 assignments. The Team Lead writes the target here before Phase 3 starts. | 3 |
| NFR-3 | Dragging a card responds within 100 ms. | 2 |
| NFR-4 | Background sync (future): changes made in Canvas show on the board within 15 minutes without the student pressing Refresh, including refreshing while they are signed out. | 5 |

### 5.2 Security and privacy

| ID | Requirement | Phase |
|----|-------------|-------|
| NFR-10 | The Canvas token is never written to logs, error messages, or the page's address (URL). | 1 |
| NFR-11 | The token is stored encrypted on the server. All traffic uses HTTPS, except on a developer's own machine (`localhost`). | 1 |
| NFR-12 | A user's Canvas connection, cached Canvas data, and board are visible only to that user. | 1 |
| NFR-13 | The portal calls only Canvas read (`GET`) endpoints. | 1 |
| NFR-14 | Out of respect for student privacy rules such as FERPA (US student records law), the portal loads no analytics, advertising, or other third-party scripts, and sends course data only to the signed-in user's browser. Google sign-in (FR-50) sees only who the user is, never course data. | 1 |

### 5.3 Reliability

| ID | Requirement | Phase |
|----|-------------|-------|
| NFR-20 | When Canvas is slow, down, or rate limiting, the page keeps showing the last saved data with a message that says Canvas couldn't be reached and the time of the data shown. If there is no saved data yet (the first load), the page says so and offers Retry, never an empty or error page. | 1 |
| NFR-21 | No user action or Canvas change can silently delete a note. | 5 |
| NFR-22 | When the same account is open on more than one device or browser tab, a card moved on one shows in its new list on the others within 30 seconds, without a reload. If the same card is moved on two devices, every device ends up showing the move that reached the server last. A card is never lost or shown twice, even if two devices load the board at the same moment or a save fails. | 2 |

### 5.4 Usability and accessibility

| ID | Requirement | Phase |
|----|-------------|-------|
| NFR-30 | Works in the current release of Chrome, Firefox, Safari, and Edge on a laptop or desktop, checked when each phase is signed off. | 1 |
| NFR-31 | *(Removed: keyboard-only use is not a requirement. From the Team Lead's review.)* | n/a |
| NFR-32 | Meets WCAG 2.2 level AA (the standard web accessibility guideline) for contrast, labels, and focus. | 4 |
| NFR-33 | Usable on a phone-width screen. As in Trello's mobile layout, one list fills the screen and the user swipes between lists. The UI details are worked out before this is built. | 5 |
| NFR-34 | Visual style is close to Trello's within C-4: a colored board background, light gray lists with rounded corners, white cards with rounded corners and a soft shadow, and compact text. Checked against approved reference screenshots and the Trello comparison review (TP-13). | 1 |
| NFR-35 | Board actions (open a card, show or hide a course, filter) need no more clicks than the same action in Trello. | 5 |
| NFR-36 | Nothing depends on hovering. Once phones are supported, every action and every piece of information can be reached by tapping. Hover can add a shortcut on desktop, but never the only way. Earlier phases avoid hover-only designs where it costs nothing, so phone support needs less rework. | 5 |

### 5.5 Maintainability

| ID | Requirement | Phase |
|----|-------------|-------|
| NFR-40 | Frontend and backend each have automated tests that run in CI on every pull request. | 0 |
| NFR-41 | The backend can run against recorded sample Canvas data, so tests don't need a real account. | 1 |
| NFR-42 | A new developer can run the app locally by following the README in under 15 minutes. | 0 |

## 6. Open questions

- ~~**Q-1** Does the Team Lead's school allow personal access tokens?~~ Answered: yes; the Team Lead has a student token and a parent token (A-1).
- **Q-2** When *Due soon* is added (FR-27, Phase 5), should it be 48 hours, or configurable?
- ~~**Q-3** Should discussion posts and quizzes appear alongside assignments?~~ Answered: they are a future feature (FR-29). The portal fetches only courses and assignments with submissions (FR-11).
- ~~**Q-4** Is multi-device sync wanted, or is one browser enough?~~ Answered: yes, the user signs in from anywhere and sees their saved state (D-2).
- **Q-5** Should the portal support parent (observer) tokens? Canvas returns observed students' data through different options, so the views would need a student picker. Proposed for Phase 5.
- ~~**Q-6** Should personal cards (FR-71) come in Phase 3, or wait until later?~~ Answered: later. Students don't need to create their own cards or lists yet, so FR-64 and FR-71 are Phase 5 future features.
- **Q-7** *(Needed before Phase 3.)* When a course ends or the student drops it, should its cards be archived at once, kept until the student hides the course, or kept until the next term starts? (Recommendation: archive when the course leaves Canvas's active list, and bring them back if it returns.)
- **Q-8** *(Needed before Phase 1 is done.)* If a student disconnects and then connects a different Canvas account or school, what happens to the old board? (Recommendation: keep the old account's cards but show only the new account's, starting them in Backlog, and bring the old cards back if the student reconnects the old account. Each card already records its connection. Showing two schools on one board is FR-55, Phase 5.)
- **Q-9** Some assignments can't be submitted in Canvas, such as on-paper or in-class work. Canvas reports them as not submitted until they are graded, so their cards say *Not submitted* (FR-23). Is that acceptable for Phase 1, or should the card show Canvas's submission type instead, such as *On paper*? (Recommendation: show *On paper* or *No submission* from Canvas's `submission_types` field, which is still a Canvas value, not one the portal works out.)
- **Q-10** *(Needed before Phase 3.)* NFR-13 and C-3 allow only Canvas `GET` calls, but the design's first Phase 3 speed-up is Canvas GraphQL, which reads data through `POST /api/graphql`. Should NFR-13 allow read-only GraphQL queries (never mutations), or should Phase 3 tuning skip GraphQL? (Recommendation: allow read-only queries; the goal, G-2, is that nothing in Canvas changes, and a query changes nothing.)
- **Q-11** Should the roadmap add a goal for reach, such as "works for every student, whatever their browser or ability", so NFR-30 and NFR-32 trace to a goal?

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
| 2026-10-25 | Phase 2 is now accounts, dragging, and sync only: FR-28, FR-66 to FR-68, FR-72 to FR-74, FR-78 saving, NFR-34, and NFR-35 move to Phase 3. Added NFR-22 (sync between devices). From the Team Lead's review. |
| 2026-10-25 | Phase 3 is now performance and Canvas sync, from the Team Lead: FR-24, FR-28, FR-40 to FR-44, FR-46, FR-66 to FR-68, FR-72 to FR-74, FR-78 saving, NFR-21, NFR-34, and NFR-35 move to Phase 5; NFR-2 moves to Phase 3 and NFR-12 to Phase 2; FR-45 reworded; added NFR-4 (Canvas changes appear within 15 minutes). Fixed broken table cells in FR-66, FR-67, FR-72 to FR-74, NFR-34, and NFR-35. |
| 2026-10-25 | Added FR-39 (fields added, changed, or cleared in Canvas, including states going backward); FR-45 now Must, archives only after a complete refresh, and restores republished assignments; added Q-7 (cards of ended or dropped courses). From the Team Lead's review. |
| 2026-10-25 | Export (FR-53) moved to Phase 5, from the Team Lead's review. |
| 2026-10-25 | Whole-plan review: rows in each table put in ID order, FR-45 moved to the board section (it is Canvas sync, not notes), scope mentions Canvas sync and notes as a future feature, "dashboard" now "board", FR-66 automatic colors in Phase 1 with custom colors in Phase 5, Q-1 answered. |
| 2026-10-25 | Sign-in (FR-50) moved to Phase 1; FR-5 now always stores the connection with the account (and is Must); NFR-11 simplified. From the Team Lead. |
| 2026-10-25 | Added FR-80 (minimize and expand lists; expanded lists share the width; empty lists start minimized), Phase 1; FR-61 now fits lists to the width instead of a fixed width, and moves to Phase 1. From the Team Lead's review. |
| 2026-10-25 | Canvas fetches are manual, from the Team Lead's review: added FR-15 (fetch only on Refresh or the first load; highlight Refresh when data is over an hour old), FR-14 now keeps the last complete copy, and background sync (NFR-4) moves to Phase 5. |
| 2026-10-25 | FR-13 shows the last sync date and time in the header; added NFR-36 (nothing depends on hover, since phones are a target platform); FR-69 works without hover. From the Team Lead's review. |
| 2026-10-25 | FR-80: minimized or expanded state is not saved and is set fresh on each load or refresh; dropping a card on an empty minimized list expands it. From the Team Lead's review. |
| 2026-10-25 | NFR-33 (phone layout) and NFR-36 (nothing depends on hover) moved to Phase 5, from the Team Lead's review. |
| 2026-10-25 | Added the Requirements by phase index, so it's clear which requirements are in scope for the current phase, from the Team Lead's review. |
| 2026-10-25 | NFR-34 (Trello visual style) moved to Phase 1, from the Team Lead. |
| 2026-10-25 | Whole-set review: NFR-12 (each user sees only their own data) moves to Phase 1, since Phase 1 stores tokens and Canvas data; FR-34's first-board rule is Phase 1; FR-6, FR-45, and FR-65 no longer mention Phase 5 notes or checklists in Phase 1–3 text. |
| 2026-10-25 | NFR-31 (keyboard-only use) and FR-73 (keyboard shortcuts) removed; C-4 no longer mentions keyboard habits. From the Team Lead's review: keyboard actions are not a requirement. |
| 2026-10-25 | Added FR-16 (Refresh progress, Phase 1) and FR-29 (quizzes and discussions, Phase 5); Q-3 answered; FR-11 fetches only courses and assignments; NFR-2's target is set from the TP-14 baseline; Phase 5 rows have no priority. From the Team Lead's review. |
| 2026-10-25 | In-depth review after PR #3: FR-22's points and status now appear on the card front (FR-65), since there is no card back until Phase 5; FR-34 is all Phase 1, since Phase 1 Refreshes already add new assignments to Backlog; the index lists FR-80's Phase 2 drop rule; FR-13 shows the last complete Refresh; FR-21 points to FR-38's order instead of repeating it; FR-39 leaves out the description until the card back shows it; FR-78 says the Phase 1 choice is kept in the browser; FR-42 drops Ctrl+Enter (keyboard actions are not a requirement); NFR-2 shows progress as courses arrive, since only a complete Refresh replaces the data (FR-14); NFR-22 says which move wins; FR-11 says what "nothing else" means; Q-7 is needed before Phase 3; Phase columns use one format; removed the stale "column" note; NFR priority explained. |
| 2026-10-25 | Requirements review, continued: FR-35 (match by Canvas ID, one card per assignment) moves to Phase 1, since Phase 1 Refreshes already add cards and two devices can load the board at once; until Phase 3 a card whose assignment is gone from Canvas is hidden but kept (FR-45); FR-22 uses the student's own due date (overrides); FR-38 states the name tiebreak once and marks dropping as Phase 2; FR-65's badge shows red over green when both apply; FR-4 keeps the board on disconnect; FR-50 and FR-51 mention notes only as Phase 5; FR-80 says what dropping on a minimized list with cards does; NFR-11 allows plain HTTP on `localhost`; the index labels every split requirement; added Q-8 (connecting a different Canvas account) and Q-9 (assignments that can't be submitted in Canvas). |
| 2026-10-25 | Business analyst review: added *Requirements by goal*, tracing every requirement to a roadmap goal; requirements say "the portal", not "the backend", and FR-10 and FR-11 no longer name Canvas endpoints (the design does); FR-1 covers an unreachable address; FR-20 covers no courses or no assignments; FR-22 uses the device's time zone; FR-50 covers staying signed in and signing out; NFR-1, NFR-14, NFR-20, NFR-30, and NFR-34 have measurable or checkable wording; NFR-2's target is written in before Phase 3; NFR-20 covers a failed first load; added Q-10 (Canvas GraphQL versus GET-only, from the design review) and Q-11 (no goal covers browsers and accessibility). |
