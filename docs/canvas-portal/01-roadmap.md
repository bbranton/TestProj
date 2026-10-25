# Roadmap

**Status:** Draft · **Owner:** Team Lead · **Last updated:** 2026-10-25

## 1. Project goals

| ID | Goal |
|----|------|
| G-1 | **One place for everything due.** A student sees what they have due across all their Canvas courses, and what they're doing about it. |
| G-2 | **Read only toward Canvas.** The portal never changes anything in Canvas. Board layout and notes belong to the student and live in the portal. |
| G-3 | **Feels like Trello.** The board looks and behaves as much like [Trello](https://trello.com) as we can: lists side by side, cards you drag, a card that opens into a detailed view, colored labels, and due date badges. Someone who uses Trello should feel at home without instructions. |
| G-4 | **Follows the student everywhere.** Signing in on any device or browser shows the same board and notes. |
| G-5 | **Private and safe.** Canvas tokens and notes are protected and never shared. |

G-3 shapes most of the screen and interaction design. It means copying
Trello's *patterns* (layout and behaviors), not its name, logo, icons,
or artwork; see constraint C-4 in the [requirements](02-requirements.md).

## 2. Phases at a glance

```mermaid
gantt
    title Canvas portal phases (sizes are estimates, not dates)
    dateFormat  YYYY-MM-DD
    axisFormat  %b
    section Foundation
    Phase 0 Decisions and setup      :p0, 2026-11-01, 14d
    section Viewer
    Phase 1 Read-only viewer         :p1, after p0, 28d
    section Organize
    Phase 2 Dragging and sync        :p2, after p1, 28d
    section Keep current
    Phase 3 Performance and Canvas sync :p3, after p2, 28d
    section Harden
    Phase 4 Polish and deploy        :p4, after p3, 21d
    section Later
    Phase 5 Future features          :p5, after p4, 28d
```

The bars show order and rough size. There are no fixed dates; a phase is done
when its exit criteria are met.

## 3. Phases in detail

### Phase 0: Decisions and setup

Settle the open decisions in section 5 and set up the empty project so later
phases only add features.

- Write the design document and the User Interface Specification, then
  choose the frontend framework (D-1). Done: React.
- Create a `canvas-portal/` folder in this repo with a `frontend/` and a
  `backend/` part, each with a "hello" page or endpoint. Done.
- Add GitHub Actions CI that builds both parts and runs their tests on every
  pull request. Done.
- Confirm the Team Lead's school allows personal access tokens (risk R-1). Done:
  the Team Lead has a student token and a parent (observer) token for testing.

**Exit criteria:** design and User Interface Specification reviewed;
decisions D-1, D-4, D-5, and D-6 recorded; CI is green on the skeleton app.

### Phase 1: Read-only viewer (minimum viable product)

The smallest thing that is useful: connect, then see everything that's due.

**Prerequisites**, done by the Team Lead before development starts:

- Create a Google Cloud project and OAuth client for Sign in with Google
  (D-7), with the Team Lead's Google account as a test user. The client ID
  and secret go in the git-ignored `.env`, never in the repo.
- Set up a Canvas course where the Team Lead can act as teacher (a free
  Canvas account from Instructure works), with a test student enrolled, and
  check that a token from it works. It is the safe place to record Canvas
  responses for the test fixtures, and the Phase 3 change tests (TP-15)
  need it.

**Work:**

- Sign in with Google, so the server knows whose data is whose (FR-50,
  D-7).
- Connect screen: paste a Canvas URL and personal access token (FR-1 to
  FR-4). The connection is saved, encrypted, with the student's account, so
  it works on any device they sign in from (FR-5, NFR-11).
- Backend calls Canvas for active courses and their assignments (FR-10 to
  FR-14), handling Canvas's paging and rate limits.
- A read-only board with the four lists Backlog, To do, In progress, and
  Done: every assignment is a Trello-style card in Backlog, sorted by due
  date, with the course show/hide buttons (FR-20 to FR-23, FR-31, FR-60,
  FR-65, FR-66, FR-78). The board has Trello's visual style from the start:
  colored background, light gray rounded lists, and white cards with a soft
  shadow (NFR-34).
- Each list can be minimized or expanded; expanded lists share the full
  width and resize as lists open and close, and empty lists start
  minimized, so in Phase 1 Backlog fills the board (FR-61, FR-80). Moving cards between lists comes in
  Phase 2.
- Clicking a card opens that assignment's own page in Canvas, in a new tab
  (FR-26). The portal's own card detail view (the card back) is a Phase 5
  future feature.
- Clear error messages for a bad token, an expired token, or Canvas being
  unreachable (FR-6, NFR-20).
- Measure how long a full Canvas load takes with the Team Lead's real
  student account and record it as a baseline (TP-14). Tuning is Phase 3; see
  the design's [Making Canvas loads fast](03-design.md#making-canvas-loads-fast-nfr-1-nfr-2-r-3).

**Exit criteria:** the Team Lead can connect a real account and see the same
assignments Canvas shows, verified by the Phase 1 test procedures, and
TP-14 has a recorded baseline.

### Phase 2: Dragging and sync

This phase does one thing: the student can drag cards between lists, and
that is saved and kept in sync on every device they use. Board layout is
stored on the server (D-2), using the accounts from Phase 1. Keeping the
student's own devices in sync is needed here, but it is the simpler kind of
sync; keeping the backend in step with Canvas is the hard part and gets
Phase 3.

- Drag cards between lists with Trello's drag feel; cards keep their due
  date order (FR-32, FR-38, FR-77, NFR-3).
- The layout is saved on the server and restored on any device (FR-33,
  FR-51).
- Sync: a move made on one device appears on the user's other open devices
  within 30 seconds, and no card is ever lost or duplicated (NFR-22, D-8).
- Canvas merge: new assignments land in *Backlog*, cards are matched by
  Canvas ID, and they move only when the student drags them (FR-34, FR-35).

**Exit criteria:** TP-06 passes in full: layout survives reloads and Canvas
refreshes, two devices open at the same time stay in step, moving the same
card on both settles on one list everywhere, and a dropped connection never
leaves a device showing a move the server doesn't have. The concurrency tests
for NFR-22 pass, and the drag steps of the Trello comparison review (TP-13)
pass.

### Phase 3: Performance and Canvas sync

This phase makes Refresh fast and makes sure every Refresh brings the
portal's copy of Canvas data fully in step with Canvas. Refresh stays
manual: the portal never fetches on its own, and highlights Refresh when the
data is more than an hour old (FR-15). It starts from the TP-14 timings
recorded in Phase 1.

Keeping the backend in step with Canvas is the hardest part of the whole
project and gets the most testing. Teachers create, delete, and change
assignments at any time; fields such as due dates can be missing at first,
added later, changed, or cleared again; and a fetch can fail halfway. Every
one of these cases has a planned outcome in the design (*What can change in
Canvas*) and a test (TP-15).

- Tune Refresh, working through the design's list in order: Canvas
  GraphQL, descriptions left out of the main load, nearest due dates first,
  then the Planner API as a fallback (NFR-1, NFR-2, R-3).
- Each Refresh brings in every change: new, changed, and removed
  assignments, new due dates and submission states, and course changes
  such as a new term (FR-13, FR-34, FR-35, FR-45).
- Every kind of Canvas change has a defined result on the board: new,
  deleted, unpublished and republished, renamed, fields added, changed, or
  cleared, submission state going forward or back, and courses ending or
  being dropped (FR-39, FR-45, Q-7).
- A partial or failed fetch never archives or changes cards (FR-45).
- Changes from a Refresh reach the student's other open devices through the
  Phase 2 sync (NFR-22).
- A Refresh stays within Canvas's rate limits, and a second Refresh while
  one is running (for example from another device) joins it instead of
  starting another (C-2).

**Exit criteria:** TP-14 meets NFR-1 and NFR-2 on the Team Lead's real
account, including at a busy time; TP-08 passes; every scenario in TP-15
and its automated suite passes; a week of daily Refreshes against the Team
Lead's real account produces no rate-limit errors and no lost, duplicated,
or wrongly archived cards.

### Phase 4: Polish and deploy

- Delete my data (FR-54).
- Accessibility pass for contrast, labels, and focus (NFR-32), and a final
  check that every browser still works (NFR-30).
- Deploy to the chosen host (D-3) and link it from the repo's landing page.

**Exit criteria:** the deployed app works from a laptop or desktop in
every browser in NFR-30;
accessibility checks pass.

### Phase 5: Later ideas (not committed)

- "Log in with Canvas" (OAuth 2) instead of pasting a token (D-4).
- Calendar view of due dates; reminders.
- Grades and submission feedback view.
- Personal cards and lists: "+ Add a card" creates a card that isn't a
  Canvas assignment, and "+ Add another list" adds lists; lists can also be
  archived (FR-71, FR-64, FR-36).
- Rename a list by clicking its title, and drag lists to reorder them
  (FR-63, FR-62).
- Quick edit menu on each card: pencil button or right-click (FR-69).
- Phone support: a layout for phone-width screens, where one list fills the
  screen and the student swipes between lists, plus nothing that depends on
  hover (NFR-33, NFR-36). The UI details come first, such as how dragging,
  minimized lists, and the course row work on a small touch screen.
- Hide assignments, such as graded or excused ones (FR-25).
- Statuses the portal works out itself, such as *Upcoming*, *Due soon* (with a
  yellow badge), and *Overdue* (FR-27).
- Show which assignments are new or were updated in Canvas since the
  student last looked, such as with a badge (FR-79).
- Checklists inside a card, with progress such as 2/5 on the card front
  (FR-70).
- Card back: clicking a card opens a dialog with its own link, showing the
  assignment's Canvas description read only (FR-28, FR-67, FR-68). Until
  then, clicking a card opens the assignment in Canvas (FR-26).
- Private notes: dated, comment-style notes on any assignment, like the
  comments on a Trello card, never sent to Canvas (FR-40 to FR-44, FR-46,
  NFR-21).
- Course label colors chosen by the student (FR-66), and the course
  show/hide choice saved with the account (FR-78).
- Trello-style filter menu with status filters and search (FR-24, FR-72).
- Archive and restore cards, as in Trello (FR-74).
- Export the board and notes as a file (FR-53).
- Background sync: refresh from Canvas on a schedule, even while the
  student is signed out, so changes appear without pressing Refresh
  (NFR-4).
- More than one board, such as one per course or term, as in Trello (FR-76).
- Board background choices and the board menu sidebar (FR-75).
- More than one school per student, such as a high school and a college
  during dual enrollment, all on one board (FR-55).
- Parent view: a parent (Canvas *observer*) token shows the courses and
  assignments of the students they observe (Q-5).

## 4. Milestones

| ID | Milestone | Phase | Shows that |
|----|-----------|-------|------------|
| M0 | Empty app builds in CI | 0 | Tooling works end to end |
| M1 | First real assignment list | 1 | Canvas connection works |
| M2 | Viewer complete | 1 | MVP usable day to day |
| M3 | Dragging saves and syncs | 2 | Core organizing feature works on every device |
| M4 | Fast loads and Canvas sync | 3 | Board stays current without waiting on Canvas |
| M5 | Deployed with sync | 4 | Usable from any laptop or desktop browser |

## 5. Open decisions

Open decisions need the Team Lead's call; each has a recommendation. Settled
decisions are struck through and kept for the record.

| ID | Decision | Options | Recommendation | Needed by |
|----|----------|---------|----------------|-----------|
| ~~D-1~~ | ~~Frontend framework~~ | **React** (largest ecosystem, most tutorials, mature drag-and-drop libraries such as dnd-kit) or **Svelte** (less code, closer to QML's declarative feel, smaller community) | **Decided** (Team Lead, 2026-10-25): React, with TypeScript and Vite. React has the most Trello-style board examples and the best support from Pragmatic drag and drop. | Done |
| ~~D-2~~ | ~~Where notes and board layout are stored~~ | **Browser local storage** (no accounts, works offline, but tied to one browser and lost if site data is cleared) or **server database** (follows the user between devices, but needs portal sign-in and more security work) | **Decided** (Team Lead, 2026-10-25): server database. The user should be able to sign in from anywhere and see their saved state. | Done |
| D-3 | Hosting | Frontend on **GitHub Pages**. Backend on **Render**, **Fly.io**, or **Vercel** serverless functions. All have free or cheap tiers with limits. | Decide in Phase 4; run locally until then. The sign-in cookie works best when the frontend and backend share one site, so the backend can also serve the built frontend instead of GitHub Pages. If background sync (Phase 5) is added later, the host must also run scheduled jobs. | Phase 4 |
| ~~D-4~~ | ~~How users connect to Canvas~~ | **Personal access token** (works today, no school involvement, user must create and paste it) or **OAuth** (smooth sign-in, needs a developer key from the school's Canvas admin) | **Decided** (Team Lead, 2026-10-25): personal access token. OAuth is a Phase 5 idea if a school will issue a key. | Done |
| ~~D-5~~ | ~~Who the app is for~~ | Just the Team Lead, a few friends, or any student at any school | **Decided** (Team Lead, 2026-10-25): any student at any school (the Canvas address is a setting), tested with the Team Lead's school. | Done |
| ~~D-6~~ | ~~Backend language~~ | **Python + FastAPI** (readable, quick to write, good for learning) or **Node.js** (same language as the frontend) | **Decided** (Team Lead, 2026-10-25): Python + FastAPI. | Done |
| ~~D-7~~ | ~~How users sign in to the portal~~ | **Sign in with Google**, **email magic link**, **username and password**, or a **hosted auth service** (see [design](03-design.md#5-signing-in-to-the-portal-d-7)) | **Decided** (Team Lead, 2026-10-25): Sign in with Google for the MVP. | Done |
| D-8 | How other open devices learn about a move (NFR-22) | **Polling** (each device asks "anything new?" every 30 seconds and when its window comes back into focus; simple, works on any host) or **live push** (the server tells devices instantly over a WebSocket or server-sent events; faster, but more to build and host) | Polling for Phase 2; live push only if 30 seconds feels slow in practice. See [design](03-design.md#keeping-devices-in-sync-nfr-22-d-8). | Start of Phase 2 |

## 6. Risks

| ID | Risk | Effect | Mitigation |
|----|------|--------|------------|
| R-1 | The school has turned off personal access tokens | Phase 1 can't connect | Check early (Phase 0). Fallback: a free Canvas account from Instructure for testing; OAuth with the school later. |
| R-2 | Canvas tokens are powerful; a leak exposes a student's whole account | Privacy harm | Backend never logs tokens, stores them encrypted, and only uses read endpoints (NFR-10, NFR-11). |
| R-3 | Canvas is slow: in the Team Lead's experience a full load of courses, each with 100+ assignments, can take several minutes, and rate limits slow it further | Students wait or give up | Never make the student wait on Canvas: show the last data at once, refresh only when the student asks, and highlight Refresh when the data is old (FR-15). Measure early with a real account (TP-14 baseline in Phase 1), then in Phase 3 fetch less, in fewer requests, and switch to Canvas GraphQL if needed (see design, *Making Canvas loads fast*). |
| R-4 | Assignments change in Canvas (renamed, deleted, new due date) | Board shows stale or orphaned cards | Merged into R-9. |
| R-5 | Learning web development alongside building | Slower progress | Small phases, one new technology at a time, docs explain terms. |
| R-6 | A school-managed Google account blocks sign-in to outside apps | Student can't sign in | Allow any Google account, so a personal one works; explain this on the sign-in screen. |
| R-7 | Matching Trello too closely in look (logo, artwork, exact styling) | Trademark or copyright complaint | Copy behavior and layout patterns only; our own name, colors, and icons (C-4). |
| R-8 | Sync bugs: two devices or two browser tabs disagree, or a card is lost or duplicated | Student stops trusting the board | Phase 2 is only dragging and sync; one row per card enforced by the database; concurrency tests in CI and the TP-06 sync procedure (NFR-22). |
| R-9 | The backend falls out of step with Canvas: a teacher deletes, changes, or clears something and the board shows stale data, loses a card, or archives one that still exists | Students miss or mistrust deadlines | Phase 3 is dedicated to it; every change case has a planned outcome (design, *What can change in Canvas*); only complete fetches can archive; scenario fixtures replayed in CI and TP-15 against a real account. |

## Change log

| Date | Change |
|------|--------|
| 2026-10-25 | First draft. |
| 2026-10-25 | D-1 postponed; D-2 decided (server storage), so accounts move into Phase 2 and Phase 4 becomes polish and deploy. R-1 cleared with student and parent test tokens. Parent view added to Phase 5. |
| 2026-10-25 | D-7 decided: Sign in with Google for the MVP. Added Google setup to Phase 0 and risk R-6. |
| 2026-10-25 | Section 1 becomes Project goals, adding G-3 (feels like Trello). Phases 2 and 3 take on Trello-style board, card back, quick edit, checklists, and personal cards. Added risk R-7. |
| 2026-10-25 | Phase 2 adds course show/hide buttons (FR-78), from the Team Lead's review. |
| 2026-10-25 | Dropped the "Move to Done?" hint (FR-37) from Phase 2. |
| 2026-10-25 | Checklists (FR-70) moved from Phase 3 to Phase 5. |
| 2026-10-25 | Adding cards and lists, and archiving lists, moved to Phase 5 as future features (Q-6 answered). |
| 2026-10-25 | Phase 2 adds FR-38: cards always sorted by due date within each list. |
| 2026-10-25 | Quick edit menu (FR-69) moved from Phase 3 to Phase 5. |
| 2026-10-25 | Phase 2 board gains a Backlog list before To do for new Canvas assignments. |
| 2026-10-25 | Added FR-79 (new and updated assignment indicators) to Phase 5. |
| 2026-10-25 | Added FR-27 (Due soon status) to Phase 5. |
| 2026-10-25 | FR-27 in Phase 5 now covers all computed statuses (Upcoming, Due soon, Overdue). |
| 2026-10-25 | Hiding assignments (FR-25) moved from Phase 1 to Phase 5. |
| 2026-10-25 | Phase 3 notes are dated, comment-style entries, separate from the read-only Canvas description (FR-28). |
| 2026-10-25 | Renaming and reordering lists (FR-62, FR-63) moved from Phase 2 to Phase 5. |
| 2026-10-25 | Added more than one school per student (FR-55) to Phase 5. |
| 2026-10-25 | Table view removed; Phase 1 shows a read-only board with every card in Backlog, from the Team Lead's review. |
| 2026-10-25 | Phase 2 narrowed to accounts, dragging between lists, and sync, from the Team Lead's review; everything else moved to Phase 3. Added D-8 (how devices learn about changes) and R-8 (sync bugs). |
| 2026-10-25 | R-3 widened to slow Canvas loads, from the Team Lead's experience; Phase 1 now measures load times (TP-14) and fixes them before Phase 2. |
| 2026-10-25 | Phase 3 is now performance and Canvas sync, from the Team Lead; the card back, notes, label colors, saved course toggles, filter menu, shortcuts, and archiving move to Phase 5. Phase 1 records a TP-14 baseline instead of meeting NFR-2. |
| 2026-10-25 | Backend-to-Canvas sync named the hardest part of the project, from the Team Lead's review: Phase 3 lists the change cases (FR-39, FR-45, Q-7) and TP-15 in its exit criteria; added R-9. |
| 2026-10-25 | Export (FR-53) moved from Phase 4 to Phase 5. |
| 2026-10-25 | Whole-plan review: Gantt sections renamed, Phase 1 no longer lists Phase 5 filters (FR-24), Phase 0 adds a Canvas teacher sandbox, D-3 notes the background job and same-site cookie needs, R-4 merged into R-9. |
| 2026-10-25 | Phase 1: merged the two "opens in Canvas" lines into one clear bullet, from the Team Lead's review. |
| 2026-10-25 | Google sign-in and the saved Canvas connection (FR-50, FR-5, NFR-11) moved from Phase 2 to Phase 1, from the Team Lead; Phase 2 renamed "Dragging and sync". |
| 2026-10-25 | Minimize and expand lists (FR-80) added to Phase 1, along with the four lists (FR-31) and width-fitting lists (FR-61); Phase 2 no longer lists them. |
| 2026-10-25 | Refresh is manual (FR-15), from the Team Lead's review: Phase 3 tunes and verifies Refresh instead of running a background job; background sync (NFR-4) is a Phase 5 idea; D-3 and R-3 updated. |
| 2026-10-25 | Phone support (NFR-33, NFR-36) moved from Phase 4 to Phase 5, since its UI details need working out first; the Phase 4 exit criteria now cover laptops and desktops only. From the Team Lead's review. |
| 2026-10-25 | Phase 1 includes Trello's visual style (NFR-34), from the Team Lead. |
| 2026-10-25 | Whole-set review: Phase 4's accessibility bullet matches the requirement phases, R-2 says tokens are stored encrypted, M5 no longer promises phones. |
| 2026-10-25 | Keyboard alternative and shortcuts removed from G-3, Phase 2, Phase 4, and Phase 5 (NFR-31, FR-73). From the Team Lead's review: keyboard actions are not a requirement. |
| 2026-10-25 | D-4 (token), D-5 (any school), and D-6 (Python + FastAPI) decided; settled decisions D-2, D-4 to D-7 struck through, from the Team Lead. |
| 2026-10-25 | D-1 decided: React. |
| 2026-10-25 | Phase 0 marked done; the Google OAuth client and the Canvas teacher sandbox move to Phase 1 as prerequisites, from the Team Lead. |
