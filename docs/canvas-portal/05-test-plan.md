# Test procedures

**Status:** Draft · **Owner:** Bridget · **Last updated:** 2026-10-25

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
| **Manual, live Canvas** | Real accounts with Bridget's student and parent tokens | A person following section 5 | Before each phase is done |

The Qt parallel: unit tests are like Qt Test cases on a single class, and E2E
tests are like Squish driving the whole app.

### Recorded Canvas data

CI never uses a real token (A-3). Instead, `backend/tests/fixtures/` holds
saved Canvas JSON responses for a made-up student, covering:

- 3 active courses, 1 concluded course (must not appear)
- Assignments in every status: upcoming, due soon, overdue, submitted, graded,
  no due date
- A course with more than 100 assignments, split over two pages (FR-12)
- A `403 Rate Limit Exceeded` response followed by success (C-2)
- A `401 Unauthorized` response (FR-6)

Fixtures contain no real names or data. When a fixture is recorded from a
live account, names and IDs are replaced before it is committed.

## 2. Pull request checklist

Every pull request must meet these before merge:

- [ ] CI is green: unit, API, E2E, and accessibility tests pass.
- [ ] New or changed behavior has tests that name the requirement IDs they
      check, such as `test_fr23_overdue_status`.
- [ ] **If the PR changes anything a user sees, the PR description includes
      screenshots of each changed screen, with before and after shots when an
      existing screen changes.** Wide and phone widths for layout changes.
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
| FR-14 | Second request within 5 minutes makes no Canvas call | API |
| FR-21 | Sort order: soonest first, no-due-date last | Unit |
| FR-23 | Each status from the status flowchart, including the 48-hour edge | Unit |
| FR-24 | Course, status, and search filters | E2E |
| FR-32, FR-33 | Drag a card, reload, card is still there | E2E |
| FR-34 | New fixture assignment appears at bottom of To do | API |
| FR-35 | Renamed assignment keeps its column and note | API |
| FR-37 | Submitted card outside Done shows hint and is not moved | API, E2E |
| FR-40 to FR-42 | Create, edit, autosave, delete a note | API, E2E |
| FR-44, NFR-13 | Canvas client has no non-GET method; a test fails if one is added | Unit |
| FR-45 | Removed assignment's card is archived and its note kept | API |
| FR-51 | Same user, two browser sessions, see the same board | E2E |
| FR-53, FR-54 | Export contains board and notes; delete removes every row for the user | API |
| NFR-10 | Logs captured during a full test run contain no token string | API |
| NFR-12 | User B gets `404` for every one of user A's cards and notes | API |
| NFR-20 | Canvas down: cached data plus warning banner | API, E2E |
| NFR-31 | Move a card using only the keyboard | E2E |
| NFR-32 | axe-core finds no serious issues on S-1 to S-6 | Accessibility |

## 5. Manual procedures

Each procedure lists the requirements it checks, what's needed first, the
steps, and the expected result. Screen IDs refer to the
[wireframes](04-wireframes-workflows.md).

### TP-01 Connect with a student token

**Checks:** FR-1, FR-2, FR-3, FR-5 · **Phase:** 1
**Needs:** signed-in portal account with no Canvas connection; student token.

| Step | Action | Expected |
|------|--------|----------|
| 1 | Open the portal | S-2 Connect Canvas is shown |
| 2 | Expand "How do I get a token?" | Four steps are shown and match Canvas's current menus |
| 3 | Enter the school address and student token; select Connect | "Connected as *student name*", then S-3 |
| 4 | Close the browser, reopen the portal | S-3 opens without asking for the token |

### TP-02 Bad and expired tokens

**Checks:** FR-6, NFR-10 · **Phase:** 1
**Needs:** a token you can delete in Canvas.

| Step | Action | Expected |
|------|--------|----------|
| 1 | On S-2, enter a made-up token | "Canvas did not accept this token"; form keeps the address |
| 2 | Connect with a real token; move one card and write one note | Saved |
| 3 | In Canvas, delete that token; in the portal select Refresh | S-2 with the expired-token message |
| 4 | Reconnect with a new token | The moved card and the note are still there |
| 5 | Check backend logs | The token text does not appear anywhere |

### TP-03 Assignments match Canvas

**Checks:** FR-10 to FR-12, FR-20 to FR-23, FR-26 · **Phase:** 1
**Needs:** connected student account.

| Step | Action | Expected |
|------|--------|----------|
| 1 | In Canvas, open each current course's Assignments page | Note the assignments, due dates, and points |
| 2 | In the portal, open S-3 with "Hide finished" off | Same courses (no ended ones) and same assignments |
| 3 | Compare due dates | Match, shown in your local time zone |
| 4 | Check one assignment of each status | Status label matches the status flowchart in the design |
| 5 | Select ↗ on any assignment | Its Canvas page opens in a new tab |

### TP-04 Filters and search

**Checks:** FR-24, FR-25 · **Phase:** 1

| Step | Action | Expected |
|------|--------|----------|
| 1 | Select one course | Only that course's assignments are listed |
| 2 | Set Status to Overdue | Only overdue assignments in that course |
| 3 | Type part of an assignment name | List narrows as you type |
| 4 | Clear filters; toggle "Hide finished" | Past graded or submitted work hides and shows |

### TP-05 Canvas unavailable

**Checks:** NFR-20, FR-13 · **Phase:** 1
**Needs:** local environment.

| Step | Action | Expected |
|------|--------|----------|
| 1 | Load S-3 so data is cached | "Updated just now" |
| 2 | Point the backend's Canvas address at an unreachable host; select Refresh | Warning banner; last data still listed with its time |
| 3 | Restore the address; select Refresh | Banner goes away; time updates |

### TP-06 Board layout persists and syncs

**Checks:** FR-30 to FR-33, FR-51 · **Phase:** 2
**Needs:** two devices or two different browsers, same portal account.

| Step | Action | Expected |
|------|--------|----------|
| 1 | On device A, switch to Board | Columns To do, In progress, Done |
| 2 | Drag two cards to In progress and reorder them | Cards move immediately |
| 3 | Reload the page | Same layout |
| 4 | Sign in on device B | Same layout |
| 5 | Move a card on device B; reload device A | Device A shows the move |

### TP-07 Board with keyboard only

**Checks:** NFR-31 · **Phase:** 2

| Step | Action | Expected |
|------|--------|----------|
| 1 | Using only Tab, reach a card | The card has a visible focus outline |
| 2 | Press Space, then the right arrow, then Space | Card moves one column right; a screen reader announcement is made |
| 3 | Pick up a card and press Escape | Card returns to where it was |

### TP-08 Canvas changes reach the board

**Checks:** FR-34, FR-35, FR-37, FR-45 · **Phase:** 2–3
**Needs:** recorded data in local environment, edited between steps.

| Step | Action | Expected |
|------|--------|----------|
| 1 | Load the board; put a note on assignment X; move it to In progress | Saved |
| 2 | Edit the fixture: rename X, add a new assignment Y; refresh | X keeps column and note with new name; Y at bottom of To do with NEW |
| 3 | Edit the fixture: mark X submitted; refresh | X shows "Move to Done?" and stays in In progress |
| 4 | Edit the fixture: remove X; refresh | X is under Archived with its note |

### TP-09 Notes

**Checks:** FR-40 to FR-44, NFR-21 · **Phase:** 3

| Step | Action | Expected |
|------|--------|----------|
| 1 | Open an assignment; type a note; wait 2 seconds | "Saved *time*" |
| 2 | Close and reopen the assignment | Note is there; card shows ✎ |
| 3 | Open the note on a second device | Same text |
| 4 | Open the browser's developer tools, Network tab; edit the note | Requests go only to the portal's `/api/` address, none to Canvas |
| 5 | Turn off Wi-Fi; type more; try to close | "Not saved" shown; closing warns |
| 6 | Delete the note | ✎ disappears from the card |

### TP-10 Privacy between users

**Checks:** NFR-12, FR-54 · **Phase:** 3–4
**Needs:** two portal accounts A and B.

| Step | Action | Expected |
|------|--------|----------|
| 1 | As A, write a note; copy the card's ID from developer tools | |
| 2 | As B, request A's card and note IDs directly | Not found |
| 3 | As A, export data | JSON file holds A's board and notes only |
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
| 2 | On a phone, open S-3, S-4, and S-5 | Phone layout from the wireframes; no sideways scrolling except the board |
| 3 | Zoom the browser to 200% | All text readable; nothing cut off |
| 4 | Turn on a screen reader (VoiceOver or NVDA) and go through S-3 | Every control is announced with a name |

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
