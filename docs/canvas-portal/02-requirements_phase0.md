# Requirements: Phase 0

**Status:** Draft · **Owner:** Team Lead · **Last updated:** 2026-11-02

## 1. Purpose and scope

This file lists what Phase 0 of the Canvas Assignments Portal must do.
Phase 0 is the setup, done on 2026-10-25, and then a local proof of
concept, from the Team Lead's rescoping of Phase 0 in the
[roadmap](/docs/canvas-portal/01-roadmap.md#3-phases-in-detail).

The requirements are split by phase (Team Lead, 2026-11-02). Phase 1 and
later, and the parts every phase shares (goals, users, assumptions,
constraints, and open questions), are in the
[Phase 1 requirements](/docs/canvas-portal/02-requirements_phase1.md).
An ID means the same requirement in every file. Where Phase 0 builds
only a part of a requirement, its row here states that part, and the
Phase 1 file states it in full.

**The proof of concept (C-5).** Phase 0 ends with a first release that
runs only on the student's own computer (`localhost`), for one student
whose Canvas address and token are set by hand in the local file that git
ignores (A-3). It has no sign-in, no connect screen, and no saved data:
each page load fetches from Canvas again, and the data is held in memory
only. It uses no third-party libraries when it runs or in its tests;
tools that run only in CI, such as Ruff, are allowed (decision D-14). Phase 1 replaces
its code, keeping its recorded Canvas responses and test cases, and
builds each requirement below again, in full.

The [Phase 1 requirements](/docs/canvas-portal/02-requirements_phase1.md)'
assumptions A-1 to A-3 and constraints C-1 to C-4 apply here too.

### Requirements by phase

Build only these in Phase 0. Anything else is out of scope, even where
the design or the User Interface Specification already describes it.
When a requirement with a row in both files changes, check the other
file's row in the same PR.

- Connecting to Canvas: FR-2
- Fetching data from Canvas: FR-10, FR-11, FR-12, FR-17
- Viewing courses and assignments: FR-20, FR-21, FR-22, FR-26
- Sorting: FR-38
- Security and privacy: NFR-10, NFR-12, NFR-13, NFR-14, NFR-15
- Maintainability: NFR-40, NFR-41, NFR-42

### Requirements by goal

| Goal | Requirements |
|------|--------------|
| G-1 One place for everything due | FR-2, FR-10 to FR-12, FR-17, FR-20 to FR-22, FR-26, FR-38 |
| G-2 Read only toward Canvas | NFR-13 |
| G-5 Private and safe | NFR-10, NFR-12, NFR-14, NFR-15 |
| Developer | NFR-40 to NFR-42 |

Every functional requirement here is a Must. Each non-functional
requirement is required for Phase 0 to be done.

## 2. Constraint

- **C-5** Phase 0's proof of concept is as section 1 describes: one
  student on their own computer, set up by hand, nothing saved, and no
  third-party libraries outside CI. Phase 1 replaces its code.

## 3. Functional requirements

| ID | Requirement | Priority | Phase |
|----|-------------|----------|-------|
| FR-2 | The portal fetches the student's Canvas profile with the token and shows their name at the top of the page, so a wrong token is easy to spot. | Must | 0 |
| FR-10 | The portal fetches the courses in which the student's Canvas enrollment is active. Ended (concluded) courses are not fetched. | Must | 0 |
| FR-11 | The portal fetches the assignments of each active course from Canvas's assignments list (the design names the endpoint). No other kinds of course item, such as ungraded discussions, pages, or announcements, are fetched. Graded quizzes and graded discussions that Canvas returns in this same list show as ordinary assignments. The student's submissions are not fetched in Phase 0. | Must | 0 |
| FR-12 | The portal follows Canvas paging so no courses or assignments are missed. | Must | 0 |
| FR-17 | When Canvas can't be used, the page says why instead of showing an empty list: Canvas rejects the token (wrong, expired, or revoked), the Canvas address can't be reached, or Canvas doesn't answer within the time limit the design sets, or Canvas answers with an error, or its certificate fails NFR-15's check. If the list of courses can't be fetched in full, the page says so instead of showing part of it. If some courses' assignments can't be fetched, the list still shows the other courses' assignments and names each course that failed. Phase 0 only: Phase 1 replaces it with FR-6, FR-16, and NFR-20, which keep the last complete copy. | Must | 0 |
| FR-20 | If the student has no active courses, or none of their active courses has any assignments, the page says so instead of showing an empty list. | Must | 0 |
| FR-21 | The page shows the assignments of every active course together, in one read-only list, in the order FR-38 sets. | Must | 0 |
| FR-22 | Each assignment shows its name, its course code, and its due date and time, shown in the time zone of the device being used. The due date is the one Canvas gives this student, including a date set just for them (a Canvas *override*). Every comparison of dates and times, such as sorting by due date, is made in UTC; only the display uses the device's time zone. | Must | 0 |
| FR-26 | Each assignment links to its page in Canvas, opening in a new tab. | Must | 0 |
| FR-38 | Assignments are sorted by due date, earliest at the top, and assignments with no due date come last. Assignments with the same due date, and those with no due date, are in name order. | Must | 0 |

## 4. Non-functional requirements

| ID | Requirement | Phase |
|----|-------------|-------|
| NFR-10 | The Canvas token is never written to logs, error messages, the page, or the page's address (URL), and is never sent to the browser. | 0 |
| NFR-12 | The student's Canvas data is visible only to them. With no sign-in in Phase 0, this means no other computer, and no page from another site open in the same browser, can read what the portal shows. | 0 |
| NFR-13 | The portal calls only Canvas read (`GET`) endpoints. | 0 |
| NFR-14 | Out of respect for student privacy rules such as FERPA (US student records law), the portal loads no analytics, advertising, or other third-party scripts. | 0 |
| NFR-15 | The Canvas token is sent only to the student's Canvas host, over HTTPS with the server's certificate checked. The portal refuses a Canvas address that doesn't use HTTPS, and follows no redirect or paging link whose scheme, host, or port differs from the Canvas address's. A refused address or link sends no request with the token, and the page says why, as FR-17 does. | 0 |
| NFR-40 | Frontend and backend each have automated tests that run in CI on every pull request. | 0 |
| NFR-41 | The backend can run against recorded sample Canvas data, so tests don't need a real account. | 0 |
| NFR-42 | A new developer can run the app locally by following the README in under 15 minutes. | 0 |

## Change log

| Date | Change |
|------|--------|
| 2026-11-02 | First draft, from the Team Lead's split of the requirements by phase and rescoping of Phase 0 as a local proof of concept (#158). The setup's NFR-40 and NFR-42 come from the Phase 1 file; the proof of concept adds C-5, FR-17, and NFR-15, and the Phase 0 parts of FR-2, FR-10 to FR-12, FR-20 to FR-22, FR-26, FR-38, NFR-10, NFR-12 to NFR-14, and NFR-41. |
