# Test procedures

**Status:** Draft · **Owner:** Team Lead · **Last updated:** 2026-10-25

This document says how we check that the portal meets its
[requirements](/docs/canvas-portal/02-requirements.md). Automated tests run on every pull
request. Manual procedures are run before a phase is called done, and their
results are recorded in section 7.

Like the requirements, tests are built with their phase. Write the automated
tests listed for the current phase (the repo's [CLAUDE.md](/CLAUDE.md)
names it), and run the manual procedures listed for it in
[Procedures by phase](#procedures-by-phase). Tests marked for a later phase
are planned here so nothing is forgotten, but are not written early.

## 1. Test levels

| Level | What it checks | Tool | Runs |
|-------|----------------|------|------|
| **Unit** | One function on its own, such as mapping Canvas status fields or card ordering | pytest (backend); Vitest (frontend) | Every PR, in CI |
| **API** | A backend endpoint end to end, with a test database and recorded Canvas responses | pytest + FastAPI test client | Every PR, in CI |
| **End-to-end (E2E)** | A real browser clicking through screens against a running backend with recorded Canvas data | Playwright | Every PR, in CI |
| **Accessibility** | Contrast and labels (NFR-32) | axe-core inside Playwright, plus a manual check | From Phase 4: every PR (automated) and each phase sign-off (manual) |
| **Manual, live Canvas** | Real accounts: the Team Lead's student token, the Canvas teacher sandbox (a roadmap Phase 1 prerequisite), and from Phase 5 the parent token | A person following section 5 | Before each phase is done |

The Qt parallel: unit tests are like Qt Test cases on a single class, and E2E
tests are like Squish driving the whole app.

### Recorded Canvas data

CI never uses a real token (A-3, NFR-41). Instead,
`canvas-portal/backend/tests/fixtures/` holds saved Canvas JSON responses
for made-up students, covering:

- 3 active courses, each with a name and course code, and 1 concluded
  course (must not appear)
- Every input to the FR-23 status rules:
  - *Submitted*: `submitted_at` set, and `submitted_at` empty; and one
    where the assignment's `has_submitted_submissions` is true but this
    student has no `submitted_at`, which must show *Not submitted*
  - *Graded*: all four checks true, then each of them false in turn
    (no submission, `graded_submissions_exist` false,
    `grade_matches_current_submission` false after a resubmission, and
    `graded_at` empty)
  - No submission object at all (*Not submitted* and *Not graded*)
  - A submission Canvas reports as `pending_review` (*Submitted* and *Not
    graded*)
  - The `late`, `missing`, and `excused` flags, including Late together
    with Graded, Missing together with Graded, and Excused together with
    Missing
  - Submission types: one type, several types, and `on_paper`
  - Work handed in on paper or needing no submission, before and after it
    is graded (*Not submitted* and *Not graded*, then *Not submitted* and
    *Graded*, by design)
- Availability dates (FR-22, FR-65): `unlock_at` and `lock_at` both empty,
  opening in the future, closed in the past, open now, and one student's
  override of these dates
- Assignments with no due date, and two with the same due date, to check
  the sort order (FR-38)
- A graded quiz and a graded discussion in the assignment list, which show
  as ordinary assignments (FR-11)
- Due dates on both sides of a daylight saving time change, and two in
  the repeated hour when clocks fall back, whose local times sort the
  wrong way but whose UTC times don't (FR-22, FR-38)
- An assignment where the student's due date differs from the class's (a
  Canvas *override*, FR-22)
- A course with more than 100 assignments, split over two pages (FR-12)
- A `403 Rate Limit Exceeded` response followed by success (C-2, FR-16)
- A `401 Unauthorized` response (FR-6)
- A course that answers slowly and one that times out (FR-16, NFR-20)
- A larger account of 8 courses and 200 assignments, for timing tests
  (NFR-1, NFR-2)
- A second student with different courses, for privacy tests (NFR-12)
- **Change sequences** for Phase 3 (FR-39, FR-45): a series of snapshots of
  the same account over time, replayed one per Refresh, covering every row of
  the design's *What can change in Canvas* table, such as a due date that is
  empty, then set, then changed, then cleared; an assignment deleted and
  then republished; a *Graded* card going back to *Not graded* after a
  resubmission; and a fetch cut off
  after the first page
- *(Phase 5)* An assignment description with formatting, a link, a
  `<script>` tag, and an `onclick` attribute (FR-28)

Fixtures contain no real names or data. When a fixture is recorded from a
live account, names and IDs are replaced before it is committed. The Canvas
teacher sandbox is the safest place to record from.

## 2. Pull request checklist

Every pull request must meet these before merge:

- [ ] The PR description lists the requirement IDs it implements, and each
      one is in the current phase in
      [Requirements by phase](/docs/canvas-portal/02-requirements.md#requirements-by-phase).
      The repo's [CLAUDE.md](/CLAUDE.md) names the current phase.
- [ ] CI is green: unit, API, and E2E tests pass, and from Phase 4 the
      accessibility tests too.
- [ ] New or changed behavior has tests that name the requirement IDs they
      check, such as `test_fr23_missing_flag`.
- [ ] **If the PR changes anything a user sees, the PR description lists
      screenshots of each changed screen, with before and after shots when an
      existing screen changes.** Wide and phone widths for layout changes.
      Store and list them as
      [Screenshots in UI PRs](/team/Development/personas/ui-ux-designer.md#screenshots-in-ui-prs) describes.
- [ ] If the PR changes the board or its menus, it says how the change
      compares with Trello's behavior (goal G-3), and any deliberate
      difference is noted.
- [ ] Screenshots contain no real tokens, names, or course data. Use the
      recorded test data.
- [ ] Docs in `docs/canvas-portal/` are updated if requirements, design, or
      screens changed.

E2E tests save screenshots of each screen as they run (Playwright's
`page.screenshot`), so the PR screenshots can be copied from a CI run into
the Library.

The NFR-34 reference images are test files, not PR screenshots. They are
committed with the E2E tests, because CI compares against them, and they
show only recorded test data, like every fixture. The Library rule for PR
screenshots doesn't apply to them.

## 3. Test environments

| Environment | Backend | Database | Canvas | Used for |
|-------------|---------|----------|--------|----------|
| Local | `uvicorn` on the developer's machine | SQLite | Recorded data, the Canvas teacher sandbox, or the Team Lead's real token from `.env` | Development, manual tests |
| CI | Started by GitHub Actions | SQLite, plus Postgres for the concurrency tests | Recorded data only | Automated tests |
| Deployed | Chosen host (D-3) | Postgres | Real Canvas | Phase 4 manual tests (TP-17) |

The NFR-22 concurrency tests also run against a Postgres service in CI.
SQLite locks the whole file on every write, so on SQLite alone those tests
could pass without proving anything about the database used in production.

Browsers for manual passes (NFR-30): the current Chrome on a laptop or
desktop from Phase 1; from Phase 5 also the current Firefox, Safari, and
Edge, and Chrome or Safari on a phone once phones are supported.

## 4. Automated test coverage

Rows are grouped by the phase that builds the requirement. A row that
checks more than one phase's behavior says which part comes later.

| Phase | Requirement | Automated test (planned) | Level |
|-------|-------------|--------------------------|-------|
| 1 | FR-2 | A valid token returns the user's name; an invalid token returns "Canvas did not accept this token"; an address that isn't Canvas returns "Couldn't reach that Canvas address" | API |
| 1 | FR-1, NFR-10 | A Canvas address that isn't `https`, or that resolves to a private or local address, is refused; the token is never sent to another host, including through a redirect or a paging `Link` URL that points elsewhere | API |
| 1 | FR-4 | Disconnect deletes the stored token row, and `GET /api/me` then says not connected; the board is kept, and reconnecting as the same Canvas user brings it back; connecting a different Canvas account hides the old account's cards and starts the new one's in Backlog, and reconnecting the old account brings its cards back (Q-8) | API |
| 1 | FR-5 | After connecting, a second session for the same user is connected without entering the token | API |
| 1 | FR-6 | `401` from Canvas during a Refresh stops it, returns "reconnect", and leaves the board and saved data untouched | API, E2E |
| 1 | FR-10, FR-11, FR-20 | Only active courses, with their names and codes, and their assignments are returned; the graded quiz and graded discussion come back as ordinary assignments; no other Canvas endpoint is called | API |
| 1 | FR-12 | All 120+ assignments returned from a two-page fixture | API |
| 1 | FR-13 | The header shows "Synced" with the date and time of the last complete Refresh; an incomplete Refresh leaves it unchanged | E2E |
| 1 | FR-14, FR-15 | Loading the board with saved data makes no Canvas call, however old the data; the first ever load fetches; Refresh fetches; data over an hour old comes back flagged so the frontend highlights Refresh | API, E2E |
| 1 | FR-16 | Fixture with one slow course and one that times out: progress reports each course's state in order; the rate-limit fixture shows a course waiting on the rate limit, then done; the run ends incomplete, the saved data is unchanged, and no error text holds the token; the log is still returned after the run ends; a second `POST /api/refresh` while one is running joins it instead of starting another; rate-limit retries stop after 5 tries and the course is marked failed; after a server restart, a run left *running* is marked incomplete | API, E2E |
| 1 | FR-16, FR-45 | A complete Refresh that finds assignments gone from Canvas says how many in its summary and offers to show them; choosing that shows the orphaned cards | E2E |
| 1 | FR-20, NFR-20 | Board messages: the first load still running, a failed first load with Retry refresh, no active courses, courses with no assignments, and every course hidden by the course buttons (with Show all, FR-78) each show their message instead of an empty board | E2E |
| 1 | FR-1, FR-2, FR-6 | S-2 shows each of its messages: none on first connect, saved token rejected, entered token rejected, and address unreachable or not `https` | E2E |
| 1 | FR-21, FR-38 | Sort order: soonest first, no-due-date last, ties by name; applies to every list | Unit |
| 1 | FR-22 | Due dates show in the browser's time zone, including across a daylight saving change (Playwright `timezoneId`); every comparison (sort order, the due badge, *Opens* and *Closed*) is made in UTC, so the fall-back fixture sorts by UTC and the results don't change when the browser's time zone does; the override fixture shows the student's date; each card shows the name, course, due date, points, submission types, and status | Unit, E2E |
| 1 | FR-22, FR-65 | With the browser clock set by Playwright: before `unlock_at` the card is grayed out and says *Opens* with the date and time; after `lock_at` it says *Closed* with the date and time; between them, or with both empty, it shows neither; the override fixture uses the student's dates; the card keeps its due date place in every case | Unit, E2E |
| 1 | FR-23 | Each fixture case above gets the *Submitted*, *Graded*, and *Missing* result the FR-23 rules give, including *Not submitted* when only `has_submitted_submissions` is true, *Submitted* and *Not graded* for `pending_review`, *Not graded* when any one of the four checks fails, and both negatives with no submission; on-paper or no-submission work shows *Not submitted* and *Not graded*, then *Not submitted* and *Graded* once graded; a Late tag shows together with Submitted and Graded; every submission type is listed in Canvas's order | Unit |
| 1 | FR-24, FR-72 | The Filter button at the start of the course row opens a menu with no course option (the course buttons are the only course control); each due date option (due date passed, next day, next week, next month, no due date) with the browser clock set by Playwright, each FR-23 status, and the keyword (matching assignment names across every list) each filter the cards, alone, combined, and together with hidden courses; the button says a filter is on and Clear ends it; a reload ends the filter (from Phase 5, it is saved) | E2E |
| 1 | FR-26 | Clicking a card opens the assignment's Canvas page in a new tab | E2E |
| 1 | FR-31, FR-34 | In Phase 1 the board shows only Backlog (To do, In progress, and Done from Phase 2); the first complete Refresh puts every assignment in Backlog; after a later complete Refresh, a new fixture assignment appears in Backlog in its due date place | API, E2E |
| 1 | FR-35 | A renamed or rescheduled assignment keeps the same card, matched by Canvas ID, and is never added twice, even when two board loads or Refreshes run at once; from Phase 2 it also keeps its list (from Phase 5, its notes) | API |
| 1 | FR-38 | Changing a fixture assignment's due date moves its card to the new place in the same list | API |
| 1 | FR-45 | After a complete Refresh in which an assignment is missing, its card isn't shown but its row is kept with its last Canvas details; when the assignment returns, the card is back in its list | API |
| 1 | FR-45 | The orphaned-card option in the filter menu shows how many orphaned cards there are, starts hidden, shows them grayed out and marked as removed from Canvas in their own lists, hides them again, and goes back to hidden on a reload | E2E |
| 1 | FR-50 | Without a session, every `/api/` endpoint except the sign-in ones returns `401`; the Google callback rejects a wrong `state` value; the session cookie is `HttpOnly`, `Secure`, and `SameSite=Lax`; a session survives closing the browser; signing out ends the session | API |
| 1 | FR-60 | Not signed in shows S-1; signed in but not connected shows S-2; signed in and connected lands on the board; in Phase 1 cards can't be dragged | E2E |
| 1 | FR-65 | Card fronts show the course code on a neutral strip, the same for every course until Phase 5 (FR-66), the points, submission types, *Submitted* or *Not submitted*, *Graded* or *Not graded*, and any Late tag; a Missing card is highlighted beyond the badge color; a not-yet-open card looks different from orphaned and (from Phase 5) archived cards; due badge is red for Missing, otherwise green for Submitted or Graded, plain otherwise, so red wins when an assignment is both Missing and Graded | Unit, E2E |
| 1 | FR-78 | Tapping a course button hides and shows its cards; Show all and Hide all; hidden cards keep their list; the choice survives a reload in the same browser | E2E |
| 1 | NFR-10 | Logs, error messages, API responses, and page addresses captured during a full test run contain no token string | API, E2E |
| 1 | NFR-11 | The stored connection row doesn't hold the token in plain text, and it decrypts only with the key from the environment; outside `localhost`, the backend answers plain HTTP only with a redirect to HTTPS | API |
| 1 | NFR-12 | Two users with different fixtures: every endpoint returns only the signed-in user's connection, courses, assignments, board, and Refresh log; from Phase 2, requests naming the other user's card IDs return `404` | API |
| 1 | NFR-13 | Canvas client has no non-GET method; a test fails if one is added | Unit |
| 1 | NFR-14 | During the E2E run, every request the page makes goes to the portal's own address; no third-party scripts load | E2E |
| 1 | NFR-20 | Canvas down, timing out, or still rate limiting after the retries: saved data plus the warning banner; with no saved data yet, S-10 shows the failures and Retry instead of an empty page | API, E2E |
| 1 | NFR-34 | Visual comparison: screenshots of S-4 (and S-5 from Phase 5) match approved reference images (Playwright `toHaveScreenshot`) | E2E |
| 1 | NFR-41 | CI runs every backend test with recorded data and no Canvas token in its environment | API |
| 2 | FR-32, FR-33, FR-38 | Drag a card to another list; it lands in its due date place; reload, it is still there | E2E |
| 2 | FR-35, FR-65 | A card in To do marked submitted in Canvas gets a green badge and stays in To do | API, E2E |
| 2 | FR-51 | Same user, two browser sessions, see the same board | E2E |
| 2 | FR-61 | The lists share the board's width; the board scrolls sideways only below 240 px per list, and dragging empty background scrolls it | E2E |
| 2 | FR-80 | Minimizing a list widens the others to fill the board, expanding narrows them; on each load or Refresh, empty lists are minimized and the rest expanded, even if the student changed them before reloading; a minimized list shows its card count, which leaves out cards of hidden courses and cards the filter hides; dropping a card on an empty minimized list expands it; dropping on a minimized list that has cards keeps it minimized and raises its count | E2E |
| 2 | NFR-1 | With the 8-course, 200-assignment fixture saved and the fixture server adding 1 second to every Canvas response, the board is usable in under 2 seconds and makes no Canvas call | E2E |
| 2 | NFR-3 | With the server's answer delayed by 1 second, a dropped card shows in its new list within 100 ms | E2E |
| 2 | NFR-22 | Concurrency: 20 parallel moves of one card leave it in exactly one list; `changes?since=` returns every change once; two parallel Refreshes with a new assignment create one card; two browser sessions converge within one poll | API, E2E |
| 3 | FR-39, FR-45 | Replays every change sequence fixture and checks each card's list, fields, sort place, and archived flag after every step; a cut-off fetch changes nothing; no card is ever deleted | API |
| 3 | FR-45 | A removed assignment's card is archived and hidden; when the assignment comes back, the card returns to its old list (from Phase 5, with its notes) | API |
| 3 | NFR-2 | Fixture server adds 1 second to every Canvas response: a full Refresh of 8 courses and 200 assignments finishes within the NFR-2 target, and progress reports each course as it finishes | API, E2E |
| 4 | FR-54 | Delete removes every row for the user | API |
| 4 | NFR-32 | axe-core finds no serious issues on S-1, S-2, S-4, S-6, and S-10 (and S-5, S-7 to S-9 once they exist, from Phase 5), covering the NFR-32 criteria: contrast (1.4.3, 1.4.11), names (1.1.1, 2.5.3, 3.3.2, 4.1.2), and status messages announced (4.1.3) for Refresh progress, the Canvas warning, and the filter's match count | Accessibility |
| 5 | FR-23, FR-65 | *Excused* shows as its own label beside the Submitted and Graded labels, turns the badge green, and turns off the Missing highlight, including when Canvas also marks the assignment missing | Unit, E2E |
| 5 | FR-78 | The course button choice is saved with the account and follows to a second session | API, E2E |
| 5 | FR-28 | Card back shows the fixture description; a description with a `<script>` tag and an `onclick` attribute comes back with both removed | Unit, API |
| 5 | FR-40 to FR-42, FR-44 | Add several notes and get them back newest first with dates; edit one and see it marked edited; delete one after confirming; none of it calls Canvas | API, E2E |
| 5 | FR-53 | Export contains the board and notes | API |
| 5 | FR-62 | Dragging a list header reorders lists and the order survives reload | E2E |
| 5 | FR-63 | Click a list title, type, Enter saves; Escape cancels | E2E |
| 5 | FR-64, FR-71 | Composer adds a list or a personal card and stays open for the next | E2E |
| 5 | FR-66 | Each course gets a palette color the first time it appears, the same on its button and all its cards, and keeps it after a reload and in a second session; changing a course's color updates every card of that course | API, E2E |
| 5 | FR-67 | Opening a card changes the address to `/c/{id}`; reloading that address reopens it; Back closes it | E2E |
| 5 | FR-68 | Card back shows every listed field for a Canvas card | E2E |
| 5 | FR-69 | Pencil and right-click open the quick edit menu | E2E |
| 5 | FR-75 | The board menu holds only the board background and course colors, and each change is saved | E2E |
| 5 | FR-70 | Add, check, reorder, and delete checklist items; card front shows progress | API, E2E |
| 5 | FR-74, NFR-21 | Archive a card or a list; the filter menu's Archived option shows them on the board, grayed out with Restore, and Restore puts them back; orphaned cards (assignment gone from Canvas) never appear under Archived; an orphan shown with the FR-45 control can be deleted from the card itself: cancelling keeps it, confirming removes the card and its notes; a card whose assignment still exists can't be deleted | API, E2E |
| 5 | FR-81 | Typing in the search box filters the whole board in place, matching name, course, description, and notes; matching archived and orphaned cards show grayed out; clearing the box shows the board again | E2E |
| 5 | NFR-37 | A full WCAG 2.2 AA audit of every screen, including the keyboard and focus criteria left out of NFR-32, with each finding either fixed or listed under *Variances from WCAG 2.2 AA* | Accessibility |
| 5 | NFR-4 | With background sync on and a fixture changed (new assignment, new due date, newly graded), the board shows each change within one job cycle without Refresh; the job backs off when the fixture reports a low rate-limit budget | API |
| 5 | NFR-36 | At phone width with touch emulation (no hover), every control and the sync time are visible and work by tap | E2E |

## 5. Manual procedures

Each procedure lists the requirements it checks, what's needed first, the
steps, and the expected result. Screen IDs refer to the
wireframes in the
[User Interface Specification](/docs/canvas-portal/04-ui-specification.md). Steps marked with a
later phase are skipped until that phase.

### Procedures by phase

**Entry criteria.** A phase's manual sign-off starts when its features are
merged, CI is green with every automated test listed for the phase in
section 4, and the procedures' **Needs** are in place (for Phase 1, the
roadmap's prerequisites: the Google OAuth client and the Canvas teacher
sandbox).

**Exit criteria (test part).** The tests are done for a phase when every
procedure listed for it passes, the results are recorded in section 7, and
no open issue fails a *Must* requirement of the phase. The test engineer
reports this; the Team Lead calls the phase done, after the project manager's review
of the roadmap's exit criteria. Later work can break earlier screens, so
each phase also reruns the earlier procedures for any screen it changed.

| Phase | Procedures |
|-------|------------|
| 1 | TP-01, TP-02, TP-03, TP-04, TP-05, TP-08 (steps 5 and 6), TP-10 (steps 1 to 3), TP-12 (step 1), TP-13 (steps 1, 10, 13), TP-14 (baseline), TP-16, TP-17 (step 1, if there is a test deploy) |
| 2 | TP-06, TP-08 (steps 1 to 4), TP-10 (step 4), TP-13 (steps 2, 3, 14), TP-14 (step 3 must meet NFR-1) |
| 3 | TP-08 (steps 7 and 8), TP-14 (must meet NFR-2), TP-15, and the week of daily Refreshes in section 7 |
| 4 | TP-10 (step 6), TP-12 (steps 3 to 5), TP-17 |
| 5 | TP-09, TP-11, and the steps marked Phase 5 in the others |

### TP-01 Sign in and connect with a student token

**Checks:** FR-1 to FR-5, FR-16, FR-50, Q-8 · **Phase:** 1
**Needs:** a Google account listed as a test user that hasn't used the
portal; the student token and the teacher sandbox's test student token; a
second device.

| Step | Action | Expected |
|------|--------|----------|
| 1 | Open the portal | S-1 Sign in is shown |
| 2 | Select Sign in with Google and choose the account | S-2 Connect Canvas is shown |
| 3 | Expand "How do I get a token?" | Four steps are shown and match Canvas's current menus |
| 4 | Enter the school address and student token; select Connect | "Connected as *student name*"; S-10 opens on its own and shows each course's progress; when it finishes, the board (S-4) shows every assignment in Backlog |
| 5 | Close the browser, reopen the portal | The board opens without asking for the token, and the "Synced" time hasn't changed (nothing was fetched) |
| 6 | Sign in with the same Google account on the second device | The board opens without asking for the token |
| 7 | On the second device, open Settings (S-6) and select Disconnect Canvas | S-2 is shown |
| 8 | Reload the portal on the first device | S-2 is shown: the connection was removed from the account, not just the device |
| 9 | Connect again with the same token | The board comes back as it was, without being rebuilt |
| 10 | Disconnect, then connect with the teacher sandbox's test student token (a different Canvas account) | Only the sandbox student's cards are shown, all in Backlog; none of the first account's cards appear |
| 11 | Disconnect, then connect with the original student token again | The original board comes back; the sandbox student's cards are hidden |
| 12 | Select Sign out from the account menu | S-1 is shown, and reopening the portal shows S-1 |

### TP-02 Bad and expired tokens

**Checks:** FR-6, NFR-10, NFR-11 · **Phase:** 1
**Needs:** a token you can delete in Canvas (the teacher sandbox's test
student works).

| Step | Action | Expected |
|------|--------|----------|
| 1 | On S-2, enter a made-up token | "Canvas did not accept this token"; form keeps the address |
| 2 | Enter an address that isn't a Canvas site, then one that starts with `http://` | Each is refused with its S-2 message; form keeps what was typed |
| 3 | Connect with a real token; from Phase 2, move one card (from Phase 5, also write a note) | Connected (from Phase 2, the move is saved) |
| 4 | In Canvas, delete that token; in the portal select Refresh | S-2 with the expired-token message |
| 5 | Reconnect with a new token | The board is back as it was; from Phase 2 the moved card is still in its list (from Phase 5, with its note) |
| 6 | Check the backend logs, the S-10 log, and the browser's address bar and history | The token text does not appear anywhere |
| 7 | Open the local database and look at the stored Canvas connection | The token is stored encrypted: its text can't be read there (NFR-11) |

### TP-03 Assignments match Canvas

**Checks:** FR-10 to FR-12, FR-20 to FR-23, FR-26, FR-35, FR-65, NFR-14 · **Phase:** 1
**Needs:** connected student account; for steps 8 and 9, the Canvas teacher
sandbox with its test student.

| Step | Action | Expected |
|------|--------|----------|
| 1 | In Canvas, open each current course's Assignments page | Note the assignments, due dates, points, and status |
| 2 | In the portal, open the board | Same courses, by name and course code (no ended ones), and same assignments; graded quizzes and graded discussions are there as ordinary assignments |
| 3 | Compare due dates | Match, shown in your local time zone |
| 4 | Compare points, and the availability dates of any assignment that hasn't opened yet or has closed | Points match; a not-yet-open card is grayed out and says *Opens* with Canvas's date and time; a closed one says *Closed* with its date and time |
| 5 | Check assignments that are not submitted, submitted, graded, resubmitted after grading, on paper, any marked Late or Missing, and an excused one | Each card's *Submitted* or *Not submitted*, *Graded* or *Not graded*, tags, and submission types match the student's own submission on Canvas's assignment page; a resubmitted one shows *Not graded*; an excused one shows *Excused* beside its Submitted and Graded labels, with a green badge and no Missing highlight, even if Canvas also marks it missing; on-paper work shows *Not submitted* and *Not graded*, then *Not submitted* and *Graded* once graded; Missing cards stand out on the board; the due badge is red for Missing, otherwise green for Submitted or Graded, plain otherwise |
| 6 | Click any card | Its Canvas page opens in a new tab |
| 7 | Open the browser's developer tools, Network tab, and reload the board | Every request goes to the portal's own address; none go to analytics, trackers, or other third-party sites (NFR-14) |
| 8 | In the sandbox, give the test student their own due date for one assignment (an override); connect the portal as that student and select Refresh | The card shows the student's date, not the class's. This answers the design's open check on overrides |
| 9 | In the sandbox, rename an assignment and change its due date; select Refresh | The same card shows the new name and moves to its new due date place; no second card appears |

### TP-04 Course buttons, filters, and search

**Checks:** FR-24, FR-72, FR-78 · **Phase:** 1
**Needs:** connected account with at least three courses; a second device.

| Step | Action | Expected |
|------|--------|----------|
| 1 | Tap one course's button in the row under the header, then tap it again | Its cards hide, then come back; the button shows hidden (○) and shown (●). From Phase 2, the cards come back in the lists they were in |
| 2 | Hide two courses, then select Show all | Every course is shown |
| 3 | Select Hide all | No cards shown; the board says all courses are hidden and offers Show all |
| 4 | Hide one course, then reload; open the portal on the second device | After the reload the course is still hidden; the second device shows every course, since the choice is kept per browser until Phase 5 (from Phase 5, it is hidden there too) |
| 5 | Open Filter at the start of the course row | The menu has due date, status, and keyword options, but no course option |
| 6 | Filter by Not submitted, then hide one course with its button | Only *Not submitted* cards by the FR-23 rules, then only those of the shown courses; the Filter button says a filter is on and offers Clear |
| 7 | Type part of an assignment name | Cards narrow as you type |
| 8 | Filter by "Due in the next week", then by "No due date" | Only cards due within the next week, then only cards with no due date |
| 9 | Clear the filters | Every card of the shown courses is shown again |
| 10 | Set a filter, then reload | The filter is gone (from Phase 5, the filter is kept); hidden courses stay hidden |

### TP-05 Canvas unavailable

**Checks:** FR-13, FR-16, NFR-20, NFR-41 · **Phase:** 1
**Needs:** local environment with recorded data and no Canvas token in `.env`, which also checks that the backend runs on recorded data alone (NFR-41).

| Step | Action | Expected |
|------|--------|----------|
| 1 | Select Refresh so data is saved | Header shows "Synced" with the current date and time |
| 2 | Cut the backend off from Canvas, for example by stopping the recorded-data server or blocking the Canvas address on the backend's machine; select Refresh | Warning banner; the board still shows the last data; the "Synced" time doesn't change |
| 3 | Open the progress panel (S-10) from the banner's Details link | Each course shows as failed with the reason; the summary says the previous data was kept and offers Retry refresh |
| 4 | Close S-10, then open it again from the "Synced" time | The same log is shown |
| 5 | Restore the connection; select Retry refresh | The summary says what was synced; the banner goes away; the "Synced" time updates |
| 6 | Make the recorded data answer one course with `403 Rate Limit Exceeded` a few times; select Refresh and open S-10 | That course shows as waiting on a Canvas rate limit, then done; the Refresh completes |

### TP-06 Board layout persists and syncs

**Checks:** FR-31 to FR-34, FR-38, FR-51, FR-60, FR-61, FR-80, NFR-22 · **Phase:** 2
**Needs:** two devices or two different browsers, same portal account;
local environment with recorded data for step 11.

| Step | Action | Expected |
|------|--------|----------|
| 1 | On device A, open the portal | The board is the home screen, with lists Backlog, To do, In progress, Done; empty lists start minimized, each a strip with its title and a count of 0 |
| 2 | Drag two cards to In progress | Cards move immediately and sit in due date order, earliest at the top |
| 3 | Reload the page | Same layout |
| 4 | Sign in on device B | Same layout |
| 5 | Move a card on device B; reload device A | Device A shows the move |
| 6 | With both devices open, move a card on A and wait without touching B | B shows the move within 30 seconds |
| 7 | Put B to sleep or switch to another app; move three cards on A; wake B | B catches up as soon as it is focused |
| 8 | Move the same card to different lists on A and B within a few seconds | Within 30 seconds both show the card in the list of the later move |
| 9 | On A, start dragging a card while B moves a different card | A's drag isn't interrupted; B's move appears after the drop |
| 10 | Turn off Wi-Fi on A; drag a card | Card goes back with "Couldn't save, try again"; B never shows the move |
| 11 | Add an assignment to the fixture; select Refresh on A and B at the same moment | One Refresh runs (B joins A's); the new card appears once, in Backlog, on both |
| 12 | Open the board in two tabs of the same browser and repeat step 6 | Same as with two devices |
| 13 | Minimize In progress, then drag a card onto its strip | The card goes into In progress; the strip's count goes up and it stays minimized |
| 14 | Reload so an empty Done list starts minimized, then drag a card onto its strip | The card goes into Done and the Done list expands; the other lists narrow to make room |
| 15 | Minimize Backlog, expand an empty list, then reload; then minimize a list and select Refresh | Minimizing widens the other expanded lists and expanding narrows them; after the reload, and again after the Refresh finishes, empty lists are minimized and the rest expanded |
| 16 | Filter out every card of one list | Its count goes to 0, and after a reload it starts minimized (counts include only shown cards) |
| 17 | Expand every list and narrow the window until each would be under 240 px | The board scrolls sideways; dragging empty background also scrolls it |

### TP-07 Board with keyboard only (removed)

Removed from the Team Lead's review: keyboard-only use is not a
requirement. The ID is kept so the other procedure numbers don't change.

### TP-08 Canvas changes reach the board

**Checks:** FR-16, FR-34, FR-35, FR-38, FR-45, FR-65 · **Phase:** 1 (steps 5
and 6), 2 (steps 1 to 4), 3 (steps 7 and 8). TP-15 covers Phase 3 in depth.
**Needs:** recorded data in local environment, edited between steps.

| Step | Action | Expected |
|------|--------|----------|
| 1 | Load the board; move assignment X to In progress (from Phase 5, also put a note on it) | Saved |
| 2 | Edit the fixture: rename X, add a new assignment Y; select Refresh | X keeps its list (from Phase 5, its notes), with the new name; Y appears in Backlog in its due date place |
| 3 | Edit the fixture: change X's due date; select Refresh | X moves to its new due date place, still in In progress |
| 4 | Edit the fixture: mark X submitted; select Refresh | X's due badge turns green and X stays in In progress |
| 5 | Edit the fixture: remove an assignment Y; select Refresh | The summary says 1 assignment was removed from Canvas and offers to show it; Y isn't on the board; the orphaned-card control shows 1 |
| 6 | Show orphaned cards in the filter menu; hide them; show them again and reload; put Y back in the fixture and select Refresh | Y shows in Backlog, grayed out and marked as removed from Canvas; hiding removes it again; after the reload orphans are hidden again; once Y is back, it shows normally and the count is 0 |
| 7 | *(Phase 3)* Edit the fixture: remove X; select Refresh | X leaves the board; its card is marked archived in the database, not deleted (it never appears under the filter's Archived option; from Phase 5 its notes are kept) |
| 8 | *(Phase 3)* Edit the fixture: put X back; select Refresh | X returns to In progress |

### TP-09 Notes

**Checks:** FR-28, FR-40 to FR-44, NFR-21 · **Phase:** 5

| Step | Action | Expected |
|------|--------|----------|
| 1 | Open an assignment and compare the Description with the assignment's page in Canvas | Same text and formatting; there is no way to edit it |
| 2 | Click "Write a note...", type a note, press Save | The note appears under Notes with today's date and time; the card shows ✎ 1 |
| 3 | Add a second note | Both notes show, newest first; the card shows ✎ 2 |
| 4 | Close and reopen the card, then open it on a second device | Same notes, same order and dates |
| 5 | Open the browser's developer tools, Network tab; add a note | Requests go only to the portal's `/api/` address, none to Canvas |
| 6 | Edit the older note | New text, original date, marked "(edited)" |
| 7 | Type a note without saving; try to close the card | Closing warns; the text is still there after cancelling |
| 8 | Turn off Wi-Fi; save a note | "Not saved, try again"; the text stays in the box |
| 9 | Delete a note, cancel, then delete it and confirm | Cancel keeps it; confirm removes it; the card shows ✎ 1 |

### TP-10 Privacy between users

**Checks:** NFR-12, FR-54 · **Phase:** 1 (steps 1 to 3), 2 (step 4),
4 (step 6), 5 (step 5)
**Needs:** two Google test users, A and B; A connected with the Team Lead's
student token, and the teacher sandbox's test student token for B.

| Step | Action | Expected |
|------|--------|----------|
| 1 | As A, select Refresh and note the courses | |
| 2 | As B, in another browser, sign in without connecting Canvas | S-2 is shown; nothing of A's appears |
| 3 | As B, connect with the sandbox student's token | Only the sandbox student's courses appear, never A's |
| 4 | *(Phase 2)* As A, move a card and copy its ID from developer tools; as B, use developer tools to send the same move request for A's card ID | Not found; A's card hasn't moved |
| 5 | *(Phase 5)* As A, export data | JSON file holds A's board and notes only |
| 6 | *(Phase 4)* As A, delete account | Signed out; signing in again starts fresh at S-2; B's board is unchanged |

### TP-11 Parent (observer) token

**Checks:** Q-5 (exploratory until parent view is planned) · **Phase:** 5

| Step | Action | Expected |
|------|--------|----------|
| 1 | Connect with the parent token | Either the observed student's courses, or a clear "parent accounts aren't supported yet" message. Never an error page |

### TP-12 Browsers, phone, and accessibility

**Checks:** NFR-30, NFR-32, NFR-33 (Phase 5) · **Phase:** 1 (step 1 in
Chrome), 4 (steps 3 to 5), 5 (step 1 in the other browsers, step 2)

| Step | Action | Expected |
|------|--------|----------|
| 1 | Run TP-01, TP-03, TP-04, and TP-16 (from Phase 2, also TP-06) in the current Chrome on a laptop or desktop; from Phase 5, also in Firefox, Safari, and Edge | Same results in each |
| 2 | *(Phase 5)* On a phone, open S-4 and S-5 | Phone layout from the wireframes: one list fills the screen and swiping moves between lists |
| 3 | *(Phase 4)* Zoom the browser to 200% | All text readable; nothing cut off |
| 4 | *(Phase 4)* Turn on a screen reader (VoiceOver or NVDA) and go through S-1, S-2, S-4, S-6, and S-10; run a Refresh, cut Canvas off, and set a filter | Every control is announced with a name; Refresh progress, the Canvas warning, and the filter's match count are announced as they change (4.1.3) |
| 5 | *(Phase 4)* View S-4 with the browser's grayscale emulation | Every meaning is still clear without color: each card's course code, Missing cards, badges, and not-yet-open cards (1.4.1) |

### TP-13 Trello comparison review

**Checks:** goal G-3, FR-60 to FR-80, NFR-34, NFR-35, C-4 · **Phase:** 1
(steps 1, 10, 13), 2 (steps 2, 3, 14), 5 (the rest)
**Needs:** the portal and a free Trello account side by side, each with a
board of about four lists and ten cards.

Do each action in Trello first, then in the portal. Record any difference in
how it looks, what it takes (clicks), or how it responds.

| Step | Action in both | Expected in the portal |
|------|----------------|------------------------|
| 1 | Look at the board as a whole | Same arrangement: header on top, a gray list on a colored background (from Phase 2, lists side by side), white cards with label strips (one neutral color until Phase 5) and badges |
| 2 | *(Phase 2)* Drag a card to another list, slowly | Card lifts and tilts, the target list is highlighted, a gap opens at the card's due date spot, neighbors slide smoothly. (Deliberate difference: Trello lets you drop anywhere; the portal keeps due date order, FR-38.) |
| 3 | *(Phase 2)* Drag a card toward the right edge of a board that scrolls | Board scrolls automatically |
| 4 | *(Phase 5)* Drag a list by its header | Lists reorder the same way |
| 5 | *(Phase 5)* Click a list title and rename it | Edits in place; Enter saves, Escape cancels |
| 6 | *(Phase 5)* Add a list, then add three cards in a row | Composer stays open after each, as in Trello |
| 7 | *(Phase 5)* Open a card | Dialog over the dimmed board, same section order; address changes |
| 8 | *(Phase 5)* Reload, then press Back | Reload reopens the card; Back closes it |
| 9 | *(Phase 5)* Use the pencil and right-click on a card | Quick edit menu next to the raised card |
| 10 | Open Filter, filter by "Due date passed", then Clear; then choose one course (in Trello by Filter, in the portal with the course buttons) | Same filter behavior; the Filter button shows the filter is active (deliberate differences: Trello puts Filter in the board header, and the portal picks courses with the course buttons) |
| 11 | *(Phase 5)* Archive a card, then restore it (in the portal, from the filter menu's Archived option) | The card is shown grayed out with Restore, and Restore puts it back (deliberate difference: Trello keeps archived items in its board menu). Orphaned cards never show under Archived; in the portal, an orphan shown with the orphaned-card control offers Delete on the card: cancelling keeps it, confirming removes it and its notes |
| 12 | *(Phase 5)* Count clicks to open a card and filter by a course | No more than Trello (NFR-35) |
| 13 | Check for Trello's name, logo, icons, or artwork anywhere | None (C-4) |
| 14 | *(Phase 2)* Collapse a list in Trello, and minimize one in the portal; then expand it | A similar narrow strip with the list's title and card count; the other lists take up the space (FR-80) |

Record the result of each step as *Same*, *Close* (small, acceptable
difference, noted), or *Different* (opens an issue unless it is a
deliberate, documented difference such as Canvas-only fields).

### TP-14 Canvas load timing

**Checks:** FR-15, FR-16, NFR-1, NFR-2, R-3 · **Phase:** 1 (baseline),
2 (step 3 must meet NFR-1), 3 (must meet NFR-2); repeat after any change to fetching
**Needs:** a local portal connected with the Team Lead's real student token
(kept in the git-ignored `.env`, never committed), and the backend's Canvas
timing log.

| Step | Action | Expected |
|------|--------|----------|
| 1 | Select Refresh and open the progress panel (S-10) | S-10 lists each course as it finishes; record the total time from its summary |
| 2 | From the timing log, record the number of courses, assignments, requests, and the slowest request | Written in the timing table in section 7 |
| 3 | Reload the board | Record how long it takes to show every card from saved data; the timing log shows no Canvas call. From Phase 2, it must be within 2 seconds (NFR-1) |
| 4 | Wait more than an hour; reload | Old data shows at once, Refresh is highlighted, and nothing is fetched until Refresh is selected; during the Refresh the board stays usable |
| 5 | Repeat step 1 on a weekday evening, when Canvas is busiest | Record the time. In Phase 3, if any run misses the NFR-2 target, apply the next fix in the design's *Phase 3 tuning* list and rerun |

The Phase 1 runs are the baseline the Team Lead uses to set the NFR-2
target, and to decide before Phase 2 whether loading from saved data needs
more tuning to meet NFR-1. Record times only, never the token or assignment names.

### TP-15 Canvas changes over time

**Checks:** FR-15, FR-22, FR-23, FR-34, FR-35, FR-38, FR-39, FR-45, NFR-20,
NFR-22, C-2, Q-7 · **Phase:** 3
**Needs:** the Canvas teacher sandbox, with its test student connected to
the portal; a second device; Q-7 answered.

Run every step as teacher in Canvas, then select Refresh on the student's
board and check it. Before each Refresh, check that the board has not
changed on its own (FR-15).

| Step | Teacher does in Canvas | Expected on the student's board |
|------|------------------------|---------------------------------|
| 1 | Create assignment A with no due date | A appears in Backlog, at the end |
| 2 | (Student drags A to To do.) Add a due date to A | A stays in To do and moves to its due date place |
| 3 | Change A's due date to earlier | A moves up within To do |
| 4 | Clear A's due date | A moves to the end of To do with no due date |
| 5 | Rename A and change its points; set A's available-from date in the future, then clear it | New name and points; same list; A is grayed out with *Opens* and the date, then back to normal |
| 6 | Create B and C at once | Both in Backlog, in date order, once each |
| 7 | Delete B | B leaves the board; its card is marked archived in the database, not deleted. The filter menu's orphaned-card option shows a count of 1; showing orphans brings B back in its list, grayed out and marked as removed from Canvas; hiding them, or reloading, hides it again |
| 8 | Unpublish C; after the Refresh, publish it again and select Refresh | C leaves the board and the orphan count goes up, then C returns to its old list, no longer grayed out, and the count goes back down |
| 9 | (Student submits A.) Grade A; (student resubmits A); then grade it again | A shows Submitted and Not graded, then Graded, then Not graded after the resubmission, then Graded again |
| 10 | Mark A excused, then not excused | The *Excused* label shows beside A's other labels with a green badge, then goes away |
| 11 | Give the student their own due date for A (an override) | The student's board shows the student's date |
| 12 | During a Refresh, cut the backend's network for a few seconds | Nothing is archived or changed; the warning banner shows; the next Refresh catches up |
| 13 | Conclude the course | Result matches the Q-7 decision |
| 14 | (No teacher change.) Select Refresh on the first device, then on the second device while it runs | The second device joins the running Refresh: one run, the same progress on both, and no rate-limit errors (C-2) |

After each step, check the second device too: it shows the same thing within
the NFR-22 time.

### TP-16 Read-only board

**Checks:** FR-21, FR-31, FR-34, FR-38, FR-60, FR-65, FR-78 ·
**Phase:** 1 (TP-06 takes over the board in Phase 2)
**Needs:** connected student account with at least three courses and some
assignments with no due date; a second device.

| Step | Action | Expected |
|------|--------|----------|
| 1 | Open the board | Only Backlog is shown, filling the board; To do, In progress, and Done aren't shown |
| 2 | Read down Backlog | Cards from every course together, in due date order, earliest at the top; cards with no due date at the end, by name |
| 3 | Look at each course's button and cards | Each card's strip shows its course code; every strip and button uses the same neutral color (course colors come in Phase 5, FR-66) |
| 4 | Try to drag a card | The card doesn't move |
| 5 | Reload, then open the board on the second device | Same layout on both devices |
| 6 | Connect the portal as the sandbox's test student after removing them from every course, then after adding them to a course with no assignments | The board says there are no active courses, then that there are no assignments, instead of showing empty lists |

### TP-17 Deployed app

**Checks:** FR-50, NFR-11, D-5 · **Phase:** 1 (step 1, on any test deploy), 4
**Needs:** the app deployed to the chosen host (D-3), with the Google OAuth
client published; a Google account that is not a listed test user. Step 1
also runs on every test deploy before Phase 4 (NFR-11).

| Step | Action | Expected |
|------|--------|----------|
| 1 | Open the deployed address with `http://` | The browser is sent to `https://` and shows a secure connection |
| 2 | Sign in with the Google account that isn't a test user | Signed in; S-2 is shown |
| 3 | Run TP-01 and TP-03 on the deployed app, in Chrome (from Phase 5, every browser in NFR-30) | Same results as locally |

## 6. Reporting a problem

A failed step becomes a GitHub issue that includes the procedure and step
(such as "TP-06 step 4"), what happened, what was expected, the browser and
device, and a screenshot with any real data hidden. Never paste a token into
an issue.

Each issue names the requirement the step checks. A failure against a
*Must* requirement of the current phase means the phase's test exit
criteria are not met. A *Should* or *Could* failure, or a *Close* result in
TP-13, is recorded; the project manager and the Team Lead decide whether it waits
for a later phase. A failing test is fixed, never skipped or weakened
without the Team Lead.

## 7. Results log

Copy this table for each phase sign-off, with one row for each procedure in
[Procedures by phase](#procedures-by-phase).

| Procedure | Steps run | Date | Tester | Environment and browser | Result | Issue |
|-----------|-----------|------|--------|-------------------------|--------|-------|
| TP-01 | All | | | | Pass / Fail | |

For Phase 3, the Team Lead selects Refresh once a day for a week on the
real account and records each day:

| Date | Result (complete or incomplete) | Rate-limit errors | Cards lost, duplicated, or wrongly archived | Notes |
|------|---------------------------------|-------------------|--------------------------------------------|-------|
| | | | | |

TP-14 timings go in their own table, one row per run:

| Date and time of day | Phase | Courses | Assignments | Requests | Slowest request | Total time | Notes |
|----------------------|-------|---------|-------------|----------|-----------------|------------|-------|
| | | | | | | | |

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
| 2026-10-25 | TP-05 checks the sync date and time; added an NFR-36 touch test (no hover). |
| 2026-10-25 | FR-80 test now checks list state is set fresh on reload; TP-06 step 14 checks that dropping on an empty minimized list expands it. |
| 2026-10-25 | Phone tests marked Phase 5: the NFR-36 touch test and TP-12 step 2; phone browsers join the manual passes in Phase 5. |
| 2026-10-25 | Links point to the renamed User Interface Specification. |
| 2026-10-25 | PR checklist: each PR lists the requirement IDs it implements, all from the current phase. |
| 2026-10-25 | TP-13 starts in Phase 1 for the visual style (NFR-34). |
| 2026-10-25 | Whole-set review: TP-04 renamed to match its Phase 1 steps, TP-10 starts in Phase 1 with NFR-12, and the unit test example says status mapping. |
| 2026-10-25 | TP-07 (keyboard only), the NFR-31 and FR-73 automated tests, and the TP-13 shortcut step removed; TP-13 steps renumbered. From the Team Lead's review: keyboard actions are not a requirement. |
| 2026-10-25 | FR-16 progress test; TP-05 step 2a checks the progress panel on failure; TP-14 reads times from the panel and uses the NFR-2 target. |
| 2026-10-25 | In-depth QA review after PR #3: added *Procedures by phase* with entry and test exit criteria, a Phase column in the coverage table, and failure severity; added Phase 1 tests for FR-1 address checks, FR-4, FR-5, FR-13, FR-20, FR-22 (time zone, override, points and status on cards), FR-26, FR-50, FR-60, FR-66, NFR-10, NFR-11, NFR-14, and NFR-41, Phase 2 tests for NFR-3 and FR-80 drops, and an NFR-2 row of its own; FR-16 test covers rate-limit waits, joining a running Refresh, retry limits, and stuck runs; concurrency tests also run on Postgres; new fixtures; TP-01 signs in, disconnects, reconnects, and connects a different Canvas account (Q-8); FR-35 is Phase 1 (TP-03 step 9); NFR-30 is Chrome only until Phase 5; hidden courses and filtered-out cards don't count toward list counts; courses are chosen only with the course buttons; Course colors (FR-66) moved to Phase 5, with neutral strips until then; orphaned-card option and the Refresh summary's removed count are Phase 1 (TP-08 steps 5 and 6); Phase 1 scope cut: only Backlog is shown, the course buttons stay in Phase 1 as the only course control (FR-61, FR-80, and NFR-1 in Phase 2, Excused in Phase 5), and the orphan option resets on reload; Excused is its own label, beside Submitted and Graded; on-paper work stays Not submitted by design; NFR-11 HTTPS is checked on every deploy; date comparisons are checked in UTC (FR-22); `pending_review` fixture; NFR-37 full WCAG audit in Phase 5; NFR-32 checks name each WCAG criterion, with a grayscale step; the FR-65 test checks that red wins over green; TP-03 checks points and the override open check, and clicks the card instead of a missing ↗; TP-04 checks course buttons and the Phase 1 filter menu (FR-24, FR-72), including that a reload ends the filter; TP-05 uses Retry refresh and a rate-limit step; TP-08 no longer needs Phase 5 notes or the Archived view; TP-09 drops Ctrl+Enter; TP-10, TP-12, and TP-13 mark their phases correctly (NFR-30 is Phase 1); TP-14 uses Refresh and a timing table; FR-45 tests cover hidden cards in Phase 1 and the orphaned-card control and the Refresh summary's removed count in Phase 2 (TP-08 steps 5 and 6, also checked in TP-15 steps 7 and 8); TP-15 step 14 checks joining a running Refresh from a second device, and section 7 logs the Phase 3 week of daily Refreshes; added TP-16 (read-only board, Phase 1) and TP-17 (deployed app, Phase 4); accessibility tests start in Phase 4 and check only screens that exist; tests for board messages, S-2 messages, and an empty account (TP-16 step 6); manual checks for NFR-11 (TP-02), NFR-14 (TP-03), and NFR-41 (TP-05); fixture path matches the repo; availability date tests (*Opens* and *Closed*, TP-03 step 4, TP-15 step 5); status tests and fixtures follow the rewritten FR-23 rules (Submitted from `submitted_at`, Graded from four checks, submission types, no Pending review); "column" now "list". |
