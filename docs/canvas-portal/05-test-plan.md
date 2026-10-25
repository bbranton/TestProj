# Test procedures

**Status:** Draft · **Owner:** Team Lead · **Last updated:** 2026-10-25

This document says how we check that the portal meets its
[requirements](02-requirements.md). Automated tests run on every pull
request. Manual procedures are run before a phase is called done, and their
results are recorded in section 7.

## 1. Test levels

| Level | What it checks | Tool | Runs |
|-------|----------------|------|------|
| **Unit** | One function on its own, such as status calculation or card ordering | pytest (backend); Vitest (frontend) | Every PR, in CI |
| **API** | A backend endpoint end to end, with a test database and recorded Canvas responses | pytest + FastAPI test client | Every PR, in CI |
| **End-to-end (E2E)** | A real browser clicking through screens against a running backend with recorded Canvas data | Playwright | Every PR, in CI |
| **Accessibility** | Contrast, labels, focus, keyboard use | axe-core inside Playwright, plus manual keyboard pass | Every PR (automated); each phase (manual) |
| **Manual, live Canvas** | Real accounts with the Team Lead's student and parent tokens | A person following section 5 | Before each phase is done |

The Qt parallel: unit tests are like Qt Test cases on a single class, and E2E
tests are like Squish driving the whole app.

### Recorded Canvas data

CI never uses a real token (A-3). Instead, `backend/tests/fixtures/` holds
saved Canvas JSON responses for a made-up student, covering:

- 3 active courses, 1 concluded course (must not appear)
- Assignments in every Canvas submission state (unsubmitted, submitted,
  graded, pending review), with the late, missing, and excused flags, including
  one that is both graded and late,
  no due date
- An assignment description with formatting, a link, a `<script>` tag, and
  an `onclick` attribute (FR-28)
- A course with more than 100 assignments, split over two pages (FR-12)
- A `403 Rate Limit Exceeded` response followed by success (C-2)
- A `401 Unauthorized` response (FR-6)
- **Change sequences** for Phase 3 (FR-39, FR-45): a series of snapshots of
  the same account over time, replayed one per refresh, covering every row of
  the design's *What can change in Canvas* table, such as a due date that is
  empty, then set, then changed, then cleared; an assignment deleted and
  then republished; a state going graded to submitted; and a fetch cut off
  after the first page

Fixtures contain no real names or data. When a fixture is recorded from a
live account, names and IDs are replaced before it is committed.

## 2. Pull request checklist

Every pull request must meet these before merge:

- [ ] CI is green: unit, API, E2E, and accessibility tests pass.
- [ ] New or changed behavior has tests that name the requirement IDs they
      check, such as `test_fr23_missing_flag`.
- [ ] **If the PR changes anything a user sees, the PR description includes
      screenshots of each changed screen, with before and after shots when an
      existing screen changes.** Wide and phone widths for layout changes.
      Store and embed them as the repo's [CLAUDE.md](../../CLAUDE.md) describes.
- [ ] If the PR changes the board, card back, or menus, it says how the
      change compares with Trello's behavior (goal G-3), and any deliberate
      difference is noted.
- [ ] Screenshots contain no real tokens, names, or course data. Use the
      recorded test data.
- [ ] Docs in `docs/canvas-portal/` are updated if requirements, design, or
      screens changed.

E2E tests save screenshots of each screen as they run (Playwright's
`page.screenshot`), so the PR screenshots can come straight from a CI run.

## 3. Test environments

| Environment | Backend | Database | Canvas | Used for |
|-------------|---------|----------|--------|----------|
| Local | `uvicorn` on the developer's machine | SQLite | Recorded data, or real token from `.env` | Development, manual tests |
| CI | Started by GitHub Actions | SQLite | Recorded data only | Automated tests |
| Deployed | Chosen host (D-3) | Postgres | Real Canvas | Phase 4 manual tests |

Browsers for manual passes (NFR-30): current Chrome, Firefox, Safari, and
Edge on a laptop, plus Chrome or Safari on a phone.

## 4. Automated test coverage

| Requirement | Automated test (planned) | Level |
|-------------|--------------------------|-------|
| FR-2 | Valid token returns user name; invalid token returns a clear error | API |
| FR-4 | Disconnect deletes the stored token row | API |
| FR-6 | `401` from Canvas returns "reconnect" and leaves board and notes untouched | API, E2E |
| FR-10, FR-11 | Only active courses and their assignments are returned | API |
| FR-12 | All 120+ assignments returned from a two-page fixture | API |
| FR-14, FR-15 | Loading the board with saved data makes no Canvas call, however old the data; the first ever load fetches; Refresh fetches; data over an hour old comes back flagged so the frontend highlights Refresh | API, E2E |
| FR-21, FR-38 | Sort order: soonest first, no-due-date last, ties by name; applies to every list | Unit |
| FR-23 | Each Canvas `workflow_state` maps to its label, and the late, missing, and excused flags show as tags, including together with a state | Unit |
| FR-24 (Phase 5) | Course, Canvas state and flag, and search filters | E2E |
| FR-32, FR-33, FR-38 | Drag a card to another list; it lands in its due date place; reload, it is still there | E2E |
| FR-31, FR-34 | First board load puts every assignment in Backlog; a new fixture assignment appears in Backlog in its due date place | API |
| FR-38 | Changing a fixture assignment's due date moves its card to the new place in the same list | API |
| FR-28 (Phase 5) | Card back shows the fixture description; a description with a `<script>` tag and an `onclick` attribute comes back with both removed | Unit, API |
| FR-35 | Renamed assignment keeps its column and notes | API |
| FR-34, FR-65 | Card marked submitted in Canvas gets a green badge and is not moved | API, E2E |
| FR-40 to FR-42 (Phase 5) | Add several notes and get them back newest first with dates; edit one and see it marked edited; delete one after confirming | API, E2E |
| FR-44, NFR-13 | Canvas client has no non-GET method; a test fails if one is added | Unit |
| FR-45 | Removed assignment's card is archived and its notes kept | API |
| FR-51 | Same user, two browser sessions, see the same board | E2E |
| FR-53 (Phase 5) | Export contains the board and notes | API |
| FR-54 | Delete removes every row for the user | API |
| NFR-10 | Logs captured during a full test run contain no token string | API |
| NFR-12 | User B gets `404` for every one of user A's cards and notes | API |
| NFR-1, NFR-2 | Fixture server adds 1 second to every Canvas response: with saved data the board answers in under 2 seconds and makes no Canvas call; a cold load of 8 courses and 200 assignments finishes in 15 seconds, with courses appearing one at a time | API, E2E |
| FR-39, FR-45 | Replays every change sequence fixture and checks each card's list, fields, sort place, and archived flag after every step; a cut-off fetch changes nothing; no card is ever deleted | API |
| NFR-4 (Phase 5) | With background sync on and a fixture changed (new assignment, new due date, newly graded), the board shows each change within one job cycle without Refresh; the job backs off when the fixture reports a low rate-limit budget | API |
| NFR-20 | Canvas down: cached data plus warning banner | API, E2E |
| NFR-22 | Concurrency: 20 parallel moves of one card leave it in exactly one list; `changes?since=` returns every change once; two parallel board loads with a new assignment create one card; two browser sessions converge within one poll | API, E2E |
| NFR-31 | Move a card using only the keyboard | E2E |
| FR-60 | Signed-in, connected user lands on the board | E2E |
| FR-61 | The four lists are always Backlog, To do, In progress, Done; expanded lists fill the width; the board scrolls sideways only below 240 px per list | E2E |
| FR-80 | Minimizing a list widens the others to fill the board, expanding narrows them; on load, empty lists are minimized and other lists keep their last state; a minimized list shows its card count | E2E |
| FR-62 (Phase 5) | Dragging a list header reorders lists and the order survives reload | E2E |
| FR-63 (Phase 5) | Click a list title, type, Enter saves; Escape cancels | E2E |
| FR-64, FR-71 (Phase 5) | Composer adds a list or a personal card and stays open for the next | E2E |
| FR-65 | Due badge is green for Submitted or Graded, red for Missing, plain otherwise | Unit, E2E |
| FR-66 (Phase 5) | Each course gets a palette color; changing it updates every card of that course | API, E2E |
| FR-67 (Phase 5) | Opening a card changes the address to `/c/{id}`; reloading that address reopens it; Back closes it | E2E |
| FR-68 (Phase 5) | Card back shows every listed field for a Canvas card | E2E |
| FR-69 (Phase 5) | Pencil and right-click open the quick edit menu | E2E |
| FR-70 (Phase 5) | Add, check, reorder, and delete checklist items; card front shows progress | API, E2E |
| FR-72 (Phase 5) | Each filter option, combined filters, and Clear | E2E |
| FR-78 | Tapping a course button hides and shows its cards on the board; Show all and Hide all; hidden cards keep their place; choice survives a reload (and, from Phase 5, a second session) | API, E2E |
| FR-73 (Phase 5) | Every shortcut in the keyboard map does its action, and `?` lists them all | E2E |
| FR-74 (Phase 5) | Archive and restore a card or a list | API, E2E |
| NFR-34 | Visual comparison: screenshots of S-4 (and S-5 from Phase 5) match approved reference images (Playwright `toHaveScreenshot`) | E2E |
| NFR-32 | axe-core finds no serious issues on S-1 to S-9 | Accessibility |

## 5. Manual procedures

Each procedure lists the requirements it checks, what's needed first, the
steps, and the expected result. Screen IDs refer to the
[wireframes](04-wireframes-workflows.md).

### TP-01 Connect with a student token

**Checks:** FR-1, FR-2, FR-3, FR-5, FR-50 · **Phase:** 1
**Needs:** signed-in portal account with no Canvas connection; student token.

| Step | Action | Expected |
|------|--------|----------|
| 1 | Open the portal | S-2 Connect Canvas is shown |
| 2 | Expand "How do I get a token?" | Four steps are shown and match Canvas's current menus |
| 3 | Enter the school address and student token; select Connect | "Connected as *student name*", then the board (S-4) |
| 4 | Close the browser, reopen the portal | The board opens without asking for the token |
| 5 | Sign in with the same Google account on a second device | The board opens without asking for the token |
| 6 | Sign out, then open the portal | S-1 Sign in is shown |

### TP-02 Bad and expired tokens

**Checks:** FR-6, NFR-10 · **Phase:** 1
**Needs:** a token you can delete in Canvas.

| Step | Action | Expected |
|------|--------|----------|
| 1 | On S-2, enter a made-up token | "Canvas did not accept this token"; form keeps the address |
| 2 | Connect with a real token; from Phase 2, move one card (from Phase 5, also write a note) | Saved |
| 3 | In Canvas, delete that token; in the portal select Refresh | S-2 with the expired-token message |
| 4 | Reconnect with a new token | The moved card (and note) are still there |
| 5 | Check backend logs | The token text does not appear anywhere |

### TP-03 Assignments match Canvas

**Checks:** FR-10 to FR-12, FR-20 to FR-23, FR-26 · **Phase:** 1
**Needs:** connected student account.

| Step | Action | Expected |
|------|--------|----------|
| 1 | In Canvas, open each current course's Assignments page | Note the assignments, due dates, and points |
| 2 | In the portal, open the board | Same courses (no ended ones) and same assignments |
| 3 | Compare due dates | Match, shown in your local time zone |
| 4 | Check one assignment of each state, and any marked Late, Missing, or Excused | Labels and tags match what Canvas shows on its own assignment page |
| 5 | Select ↗ on any assignment | Its Canvas page opens in a new tab |

### TP-04 Filters and search

**Checks:** FR-24, FR-78 · **Phase:** 1 (steps 1 to 4 from Phase 5)

| Step | Action | Expected |
|------|--------|----------|
| 1 | Select one course | Only that course's assignments are listed |
| 2 | Set Status to Not submitted | Only that course's assignments Canvas reports as not submitted |
| 3 | Type part of an assignment name | List narrows as you type |
| 4 | Clear the filters | Every assignment is listed again |
| 5 | Tap one course's button in the row under the header, then tap it again | Its assignments hide, then come back; the button shows hidden (○) and shown (●) |
| 6 | Hide two courses, then select Show all | Every course is shown |
| 7 | Select Hide all | No assignments shown; the page says all courses are hidden and offers Show all |

### TP-05 Canvas unavailable

**Checks:** NFR-20, FR-13 · **Phase:** 1
**Needs:** local environment.

| Step | Action | Expected |
|------|--------|----------|
| 1 | Load the board so data is cached | "Updated just now" |
| 2 | Point the backend's Canvas address at an unreachable host; select Refresh | Warning banner; last data still listed with its time |
| 3 | Restore the address; select Refresh | Banner goes away; time updates |

### TP-06 Board layout persists and syncs

**Checks:** FR-31 to FR-33, FR-38, FR-51, FR-60, NFR-22 · **Phase:** 2
**Needs:** two devices or two different browsers, same portal account.

| Step | Action | Expected |
|------|--------|----------|
| 1 | On device A, open the portal | The board is the home screen, with lists Backlog, To do, In progress, Done, and every assignment starts in Backlog |
| 2 | Drag two cards to In progress | Cards move immediately and sit in due date order, earliest at the top |
| 3 | Reload the page | Same layout |
| 4 | Sign in on device B | Same layout |
| 5 | Move a card on device B; reload device A | Device A shows the move |
| 6 | With both devices open, move a card on A and wait without touching B | B shows the move within 30 seconds |
| 7 | Put B to sleep or switch to another app; move three cards on A; wake B | B catches up as soon as it is focused |
| 8 | Move the same card to different lists on A and B within a few seconds | Within 30 seconds both show the card in the list of the later move |
| 9 | On A, start dragging a card while B moves a different card | A's drag isn't interrupted; B's move appears after the drop |
| 10 | Turn off Wi-Fi on A; drag a card | Card goes back with "Couldn't save, try again"; B never shows the move |
| 11 | Add an assignment to the fixture; open the board on A and B at the same moment | The new card appears once, in Backlog, on both |
| 12 | Open the board in two tabs of the same browser and repeat step 6 | Same as with two devices |
| 13 | Minimize In progress, then drag a card onto its strip | The card goes into In progress; the strip's count goes up and it stays minimized |

### TP-07 Board with keyboard only

**Checks:** NFR-31 · **Phase:** 2

| Step | Action | Expected |
|------|--------|----------|
| 1 | Using only Tab, reach a card | The card has a visible focus outline |
| 2 | Press Space, then the right arrow, then Space | Card moves one list right; a screen reader announcement is made |
| 3 | Pick up a card and press Escape | Card returns to where it was |

### TP-08 Canvas changes reach the board

**Checks:** FR-34, FR-35, FR-38, FR-45, FR-65 · **Phase:** 2–3 (TP-15 covers Phase 3 in depth)
**Needs:** recorded data in local environment, edited between steps.

| Step | Action | Expected |
|------|--------|----------|
| 1 | Load the board; put a note on assignment X; move it to In progress | Saved |
| 2 | Edit the fixture: rename X, add a new assignment Y; refresh | X keeps its list and notes, with the new name; Y appears in Backlog in its due date place |
| 3 | Edit the fixture: mark X submitted; refresh | X's due badge turns green and X stays in In progress |
| 4 | Edit the fixture: remove X; refresh | X is under Archived with its notes |

### TP-09 Notes

**Checks:** FR-28, FR-40 to FR-44, NFR-21 · **Phase:** 5

| Step | Action | Expected |
|------|--------|----------|
| 1 | Open an assignment and compare the Description with the assignment's page in Canvas | Same text and formatting; there is no way to edit it |
| 2 | Click "Write a note...", type a note, press Save | The note appears under Notes with today's date and time; the card shows ✎ 1 |
| 3 | Add a second note with Ctrl+Enter | Both notes show, newest first; the card shows ✎ 2 |
| 4 | Close and reopen the card, then open it on a second device | Same notes, same order and dates |
| 5 | Open the browser's developer tools, Network tab; add a note | Requests go only to the portal's `/api/` address, none to Canvas |
| 6 | Edit the older note | New text, original date, marked "(edited)" |
| 7 | Type a note without saving; try to close the card | Closing warns; the text is still there after cancelling |
| 8 | Turn off Wi-Fi; save a note | "Not saved, try again"; the text stays in the box |
| 9 | Delete a note, cancel, then delete it and confirm | Cancel keeps it; confirm removes it; the card shows ✎ 1 |

### TP-10 Privacy between users

**Checks:** NFR-12, FR-54 · **Phase:** 2–4
**Needs:** two portal accounts A and B.

| Step | Action | Expected |
|------|--------|----------|
| 1 | As A, move a card (from Phase 5, also write a note); copy the card's ID from developer tools | |
| 2 | As B, request A's card and note IDs directly | Not found |
| 3 | *(Phase 5)* As A, export data | JSON file holds A's board and notes only |
| 4 | As A, delete account | Signed out; signing in again starts fresh |

### TP-11 Parent (observer) token

**Checks:** Q-5 (exploratory until parent view is planned) · **Phase:** 5

| Step | Action | Expected |
|------|--------|----------|
| 1 | Connect with the parent token | Either the observed student's courses, or a clear "parent accounts aren't supported yet" message. Never an error page |

### TP-12 Browsers, phone, and accessibility

**Checks:** NFR-30, NFR-32, NFR-33 · **Phase:** 4

| Step | Action | Expected |
|------|--------|----------|
| 1 | Run TP-01, TP-03, and TP-06 in Chrome, Firefox, Safari, and Edge | Same results in each |
| 2 | On a phone, open S-4 (and S-5 from Phase 5) | Phone layout from the wireframes: one list fills the screen and swiping moves between lists |
| 3 | Zoom the browser to 200% | All text readable; nothing cut off |
| 4 | Turn on a screen reader (VoiceOver or NVDA) and go through S-4 | Every control is announced with a name |

### TP-13 Trello comparison review

**Checks:** goal G-3, FR-60 to FR-77, NFR-34, NFR-35, C-4 · **Phase:** 2, then
each later phase
**Needs:** the portal and a free Trello account side by side, each with a
board of about three lists and ten cards.

Do each action in Trello first, then in the portal. Record any difference in
how it looks, what it takes (clicks or keys), or how it responds.

| Step | Action in both | Expected in the portal |
|------|----------------|------------------------|
| 1 | Look at the board as a whole | Same arrangement: header on top, lists side by side on a colored background, gray lists, white cards with label strips and badges |
| 2 | Drag a card to another list, slowly | Card lifts and tilts, the target list is highlighted, a gap opens at the card's due date spot, neighbors slide smoothly. (Deliberate difference: Trello lets you drop anywhere; the portal keeps due date order, FR-38.) |
| 3 | Drag a card toward the right edge | Board scrolls automatically |
| 4 | *(Phase 5)* Drag a list by its header | Lists reorder the same way |
| 5 | *(Phase 5)* Click a list title and rename it | Edits in place; Enter saves, Escape cancels |
| 6 | *(Phase 5)* Add a list, then add three cards in a row | Composer stays open after each, as in Trello |
| 7 | *(Phase 5)* Open a card | Dialog over the dimmed board, same section order; address changes |
| 8 | *(Phase 5)* Reload, then press Back | Reload reopens the card; Back closes it |
| 9 | *(Phase 5)* Use the pencil and right-click on a card | Quick edit menu next to the raised card |
| 10 | *(Phase 5)* Press `f`, filter by a course and by "Due date passed", then `x` | Same behavior; the course row shows the filter is active (deliberate difference: Trello puts Filter in the board header) |
| 11 | *(Phase 5)* Try each shortcut in Trello's shortcut list that the portal supports | Same key does the same thing |
| 12 | *(Phase 5)* Archive a card and restore it from the board menu | Same steps |
| 13 | *(Phase 5)* Count clicks to open a card and filter by a course | No more than Trello (NFR-35) |
| 14 | Check for Trello's name, logo, icons, or artwork anywhere | None (C-4) |

Record the result of each step as *Same*, *Close* (small, acceptable
difference, noted), or *Different* (opens an issue unless it is a
deliberate, documented difference such as Canvas-only fields).

### TP-14 Canvas load timing

**Checks:** NFR-1, NFR-2, R-3 · **Phase:** 1 (baseline), 3 (must pass); repeat
after any change to fetching
**Needs:** the Team Lead's real student token in the git-ignored `.env`, and
the backend's Canvas timing log.

| Step | Action | Expected |
|------|--------|----------|
| 1 | Clear the portal's cache; open the board | Courses appear one at a time; record the total time until the last one |
| 2 | From the timing log, record the number of courses, assignments, requests, and the slowest request | Written in the results log |
| 3 | Reload the board | Shows within 2 seconds from the cache (NFR-1) |
| 4 | Wait more than an hour; reload | Old data shows at once, Refresh is highlighted, and nothing is fetched until Refresh is selected; during the Refresh the board stays usable |
| 5 | Repeat step 1 on a weekday evening, when Canvas is busiest | Record the time. In Phase 3, if any run misses 15 seconds (NFR-2), apply the next fix in the design's *Phase 3 tuning* list and rerun |

Record times only, never the token or assignment names, in the results log.

### TP-15 Canvas changes over time

**Checks:** FR-15, FR-23, FR-34, FR-35, FR-38, FR-39, FR-45, Q-7 · **Phase:** 3
**Needs:** a Canvas course where the Team Lead can act as teacher (a free
Canvas account from Instructure works), a student account enrolled in it,
and the portal.

Run every step as teacher in Canvas, then select Refresh on the student's
board and check it. Before each Refresh, check that the board has not
changed on its own (FR-15).

| Step | Teacher does in Canvas | Expected on the student's board |
|------|------------------------|---------------------------------|
| 1 | Create assignment A with no due date | A appears in Backlog, at the end |
| 2 | (Student drags A to To do.) Add a due date to A | A stays in To do and moves to its due date place |
| 3 | Change A's due date to earlier | A moves up within To do |
| 4 | Clear A's due date | A moves to the end of To do with no due date |
| 5 | Rename A and change its points | New name and points; same list |
| 6 | Create B and C at once | Both in Backlog, in date order, once each |
| 7 | Delete B | B leaves the board; it is archived, not gone |
| 8 | Unpublish C, wait one refresh, publish it again | C leaves the board, then returns to its old list |
| 9 | (Student submits A.) Grade A, then remove the grade | Badge goes Submitted, Graded, then back to Submitted |
| 10 | Mark A excused, then not excused | Excused tag shows, then goes away |
| 11 | Give the student their own due date for A (an override) | The student's board shows the student's date |
| 12 | During a refresh, cut the backend's network for a few seconds | Nothing is archived or changed; the warning banner shows; the next refresh catches up |
| 13 | Conclude the course | Result matches the Q-7 decision |

After each step, check a second device too: it shows the same thing within
the NFR-22 time.

## 6. Reporting a problem

A failed step becomes a GitHub issue that includes the procedure and step
(such as "TP-06 step 4"), what happened, what was expected, the browser and
device, and a screenshot with any real data hidden.

## 7. Results log

Copy this table for each phase sign-off.

| Procedure | Date | Tester | Environment and browser | Result | Issue |
|-----------|------|--------|-------------------------|--------|-------|
| TP-01 | | | | Pass / Fail | |

## Change log

| Date | Change |
|------|--------|
| 2026-10-25 | First draft. Includes the screenshot rule for UI changes. |
| 2026-10-25 | Trello goal (G-3): Trello comparison step in the PR checklist, automated tests for FR-60 to FR-77 and NFR-34, TP-13 Trello comparison review; TP-06, TP-07, TP-12 updated. |
| 2026-10-25 | Course show/hide buttons (FR-78): automated test and TP-04 steps 5 and 6. |
| 2026-10-25 | Hide all added to FR-78 tests and TP-04 step 7. |
| 2026-10-25 | FR-37 removed: tests now check that a submitted card only changes its badge. |
| 2026-10-25 | FR-70 checklist tests marked Phase 5. |
| 2026-10-25 | Adding cards and lists moved to Phase 5 in the automated tests and TP-13. |
| 2026-10-25 | FR-38 (always sorted by due date): sort tests, TP-06 step 2, TP-08 step 2, and TP-13 step 2 updated. |
| 2026-10-25 | Quick edit tests marked Phase 5. |
| 2026-10-25 | Backlog list: FR-31/FR-34 test, TP-06 step 1, and TP-08 step 2 updated. |
| 2026-10-25 | NEW badge removed from the FR-34 test and TP-08 step 2. |
| 2026-10-25 | Due soon removed from fixtures and status tests (Phase 5, FR-27). |
| 2026-10-25 | Status tests now check the direct mapping of Canvas fields (FR-23); fixtures cover every state and flag. |
| 2026-10-25 | "Hide finished" steps removed from TP-03 and TP-04; hiding assignments is Phase 5 (FR-25). |
| 2026-10-25 | TP-13 step 10 notes the Filter button's new place in the course row. |
| 2026-10-25 | TP-09 rewritten for dated, comment-style notes and the read-only Canvas description (FR-28); description cleaning fixture and test added. |
| 2026-10-25 | List rename and reorder tests (FR-62, FR-63, TP-13 steps 4 and 5) marked Phase 5. |
| 2026-10-25 | Table view removed: TP-01, TP-03, TP-04, TP-05, TP-11, and coverage rows now use the board. |
| 2026-10-25 | TP-06 gains sync steps 6 to 12 and an NFR-22 concurrency test row, for the Phase 2 focus on dragging and sync. |
| 2026-10-25 | Added TP-14 (Canvas load timing with the real student account) and a slow-Canvas automated test for NFR-1 and NFR-2. |
| 2026-10-25 | Phase 3 is performance and Canvas sync: TP-09 and the card back, notes, filter, label, shortcut, and archive tests move to Phase 5; TP-14 is a Phase 1 baseline and must pass in Phase 3; added an NFR-4 background refresh test. |
| 2026-10-25 | Added TP-15 (Canvas changes over time, run as teacher), change sequence fixtures, and an automated replay test for FR-39 and FR-45, from the Team Lead's review. |
| 2026-10-25 | Export tests (FR-53, TP-10 step 3) marked Phase 5. |
| 2026-10-25 | Whole-plan review: TP-02, TP-12, TP-13, and the FR-78 and NFR-34 tests now mark Phase 5 steps. |
| 2026-10-25 | TP-01 checks sign-in (FR-50) and the saved connection on a second device, now that both are Phase 1. |
| 2026-10-25 | Added an FR-80 test (minimize, expand, and width fitting) and TP-06 step 13 (dropping on a minimized list). |
| 2026-10-25 | Refresh is manual (FR-15): tests check that loading never fetches and that Refresh is highlighted after an hour; TP-15 uses Refresh instead of waiting for background sync; NFR-4 test is Phase 5. |
