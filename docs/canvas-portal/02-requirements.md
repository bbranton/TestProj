# Requirements

**Status:** Draft · **Owner:** Team Lead · **Last updated:** 2026-10-25

## 1. Purpose and scope

This document lists what the Canvas Assignments Portal must do (*functional
requirements*, `FR`) and how well it must do it (*non-functional
requirements*, `NFR`). Each requirement has an ID that the design and test
documents refer back to.

**In scope:** reading a student's courses and assignments from Canvas,
showing them, arranging them on a kanban board, and keeping private notes.

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
| FR-23 | Status is one of: *Upcoming*, *Due soon* (within 48 hours), *Overdue*, *Submitted*, *Graded*. | Must | 1 |
| FR-24 | The user can filter by course and by status, and search by assignment name. | Should | 1 |
| FR-25 | The user can hide past, completed assignments (on by default). | Should | 1 |
| FR-26 | Each assignment links to its page in Canvas, opening in a new tab. | Must | 1 |

### 4.4 Kanban board

| ID | Requirement | Priority | Phase |
|----|-------------|----------|-------|
| FR-30 | The user can switch between list view and board view. | Must | 2 |
| FR-31 | The board starts with columns *To do*, *In progress*, *Done*. | Must | 2 |
| FR-32 | The user can drag a card to another column or another position in the same column. | Must | 2 |
| FR-33 | The board layout (which column each card is in, and its order) is saved and restored on the next visit. | Must | 2 |
| FR-34 | Assignments that are new since the last visit appear at the bottom of *To do*. | Must | 2 |
| FR-35 | Cards are matched to assignments by Canvas assignment ID, so a renamed or rescheduled assignment keeps its place. | Must | 2 |
| FR-36 | The user can add, rename, reorder, and delete columns. Deleting a column moves its cards to *To do*. | Could | 2 |
| FR-37 | When Canvas reports an assignment as submitted and its card is not in *Done*, the card shows a "Submitted, move to Done?" hint. The portal does not move it automatically. | Should | 2 |

### 4.5 Private notes

| ID | Requirement | Priority | Phase |
|----|-------------|----------|-------|
| FR-40 | The user can add a plain-text note to any assignment. | Must | 3 |
| FR-41 | The user can edit and delete a note. | Must | 3 |
| FR-42 | Notes save automatically while typing, and the page shows when the note was saved. | Should | 3 |
| FR-43 | A card with a note shows a note icon; opening the assignment shows the full note. | Must | 3 |
| FR-44 | Notes are never sent to Canvas. | Must | 3 |
| FR-45 | If an assignment disappears from Canvas, its note and card move to an *Archived* area rather than being deleted. | Should | 3 |
| FR-46 | Notes support simple formatting (bold, lists, links). | Could | 3 |

### 4.6 Accounts, sync, and data control

| ID | Requirement | Priority | Phase |
|----|-------------|----------|-------|
| FR-50 | The user can sign in to the portal so their board and notes are tied to them on the server. | Must | 2 |
| FR-51 | Board and notes stored on the server appear on any device where the user signs in. | Must | 2 |
| FR-52 | *(Removed: board and notes are on the server from the start, so there is no browser data to import.)* | n/a | n/a |
| FR-53 | The user can export their board and notes as a JSON file. | Should | 4 |
| FR-54 | The user can delete all their data from the portal. | Must | 4 |

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
| NFR-33 | Usable on a phone-width screen (list view at minimum). | 4 |

### 5.5 Maintainability

| ID | Requirement | Phase |
|----|-------------|-------|
| NFR-40 | Frontend and backend each have automated tests that run in CI on every pull request. | 0 |
| NFR-41 | The backend can run against recorded sample Canvas data, so tests don't need a real account. | 1 |
| NFR-42 | A new developer can run the app locally by following the README in under 15 minutes. | 0 |

## 6. Open questions

- **Q-1** Does the Team Lead's school allow personal access tokens? (Blocks Phase 1; see R-1.)
- **Q-2** Should "Due soon" be 48 hours, or configurable?
- **Q-3** Should discussion posts and quizzes appear alongside assignments? Canvas exposes them as assignments in most cases, so the default is yes.
- ~~**Q-4** Is multi-device sync wanted, or is one browser enough?~~ Answered: yes, the user signs in from anywhere and sees their saved state (D-2).
- **Q-5** Should the portal support parent (observer) tokens? Canvas returns observed students' data through different options, so the views would need a student picker. Proposed for Phase 5.

## Change log

| Date | Change |
|------|--------|
| 2026-10-25 | First draft. |
| 2026-10-25 | Server storage decided: FR-50 and FR-51 move to Phase 2, FR-52 removed. Added parent (observer) user, test tokens under A-1, A-3 token handling, Q-5. |
