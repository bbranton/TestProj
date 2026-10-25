# Roadmap

**Status:** Draft · **Owner:** Team Lead · **Last updated:** 2026-10-25

## 1. Project goals

| ID | Goal |
|----|------|
| G-1 | **One place for everything due.** A student sees what they have due across all their Canvas courses, and what they're doing about it. |
| G-2 | **Read only toward Canvas.** The portal never changes anything in Canvas. Board layout and notes belong to the student and live in the portal. |
| G-3 | **Feels like Trello.** The board looks and behaves as much like [Trello](https://trello.com) as we can: lists side by side, cards you drag, a card that opens into a detailed view, colored labels, due date badges, and Trello's keyboard habits. Someone who uses Trello should feel at home without instructions. |
| G-4 | **Follows the student everywhere.** Signing in on any device or browser shows the same board and notes. |
| G-5 | **Private and safe.** Canvas tokens and notes are protected and never shared. |

G-3 shapes most of the screen and interaction design. It means copying
Trello's *patterns* (layout, behaviors, shortcuts), not its name, logo, icons,
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
    Phase 2 Accounts and kanban board :p2, after p1, 28d
    Phase 3 Private notes            :p3, after p2, 14d
    section Harden
    Phase 4 Polish and deploy        :p4, after p3, 21d
    section Later
    Phase 5 OAuth and extras         :p5, after p4, 28d
```

The bars show order and rough size. There are no fixed dates; a phase is done
when its exit criteria are met.

## 3. Phases in detail

### Phase 0: Decisions and setup

Settle the open decisions in section 5 and set up the empty project so later
phases only add features.

- Write the design document and Phase 1 wireframes, then choose the frontend
  framework (D-1). D-1 is deliberately decided after the design, because the
  features we focus on may change which framework fits best.
- Create a `canvas-portal/` folder in this repo with a `frontend/` and a
  `backend/` part, each with a "hello" page or endpoint.
- Create a Google Cloud project and OAuth client for Sign in with Google
  (D-7), with the Team Lead's Google account as a test user.
- Add GitHub Actions CI that builds both parts and runs their (empty) test
  suites on every pull request.
- Confirm the Team Lead's school allows personal access tokens (risk R-1). Done:
  the Team Lead has a student token and a parent (observer) token for testing.

**Exit criteria:** design and Phase 1 wireframes reviewed; decisions D-1, D-4,
D-5, and D-6 recorded; CI is green on an empty app;
a test Canvas account works with a token.

### Phase 1: Read-only viewer (minimum viable product)

The smallest thing that is useful: connect, then see everything that's due.

- Connect screen: paste a Canvas URL and personal access token (FR-1 to FR-5).
- Backend calls Canvas for active courses and their assignments (FR-10 to
  FR-14), handling Canvas's paging and rate limits.
- Dashboard shows courses and an upcoming-assignments list sorted by due date,
  with filters by course and status, each assignment drawn as a Trello-style
  card (FR-20 to FR-25, FR-65).
- Each assignment links back to its Canvas page (FR-26).
- Clear error messages for a bad token, an expired token, or Canvas being
  unreachable (FR-6, NFR-20).

**Exit criteria:** the Team Lead can connect a real account and see the same
assignments Canvas shows, verified by the Phase 1 test procedures.

### Phase 2: Accounts and kanban board

Board layout and notes are stored on the server from the start (D-2), so
they follow the user to any device or browser. That needs portal accounts
first.

- Portal sign-in so the server knows whose data is whose (FR-50).
- The user's Canvas connection is saved on the server with their account, so
  signing in on a new device doesn't require pasting the token again (FR-5,
  NFR-11).
- Trello-style board: lists side by side that scroll sideways, default lists
  *To do*, *In progress*, *Done*; the board becomes the home screen (FR-30,
  FR-31, FR-60, FR-61).
- Trello-style cards: course label colors, colored due date badges, note icon
  (FR-65, FR-66).
- Clicking a card opens its "card back" in a dialog over the board, with its
  own link (FR-67, FR-68).
- Drag cards between and within lists with Trello's drag feel, and drag lists
  to reorder them; keyboard alternative for dragging (FR-32, FR-62, FR-77,
  NFR-31).
- The board has three fixed lists (To do, In progress, Done) that can be
  renamed by clicking their title (FR-31, FR-63).
- A row of show/hide buttons under the header, one per course (FR-78).
- Trello-style filter menu and keyboard shortcuts (FR-72, FR-73).
- New assignments from Canvas land in *To do*; cards are matched by Canvas ID
  and only move when the student drags them (FR-34, FR-35).
- Board layout is saved on the server and restored on any device (FR-33,
  FR-51).
- Archive and restore cards, as in Trello (FR-74).

**Exit criteria:** layout survives a page reload and a Canvas refresh without
losing or duplicating cards, the same layout appears after signing in on a
second device, and the Trello comparison review (TP-13) passes for the board.

### Phase 3: Private notes

- Add, edit, and delete a note on any assignment (FR-40 to FR-42).
- Notes are the card's *Description*, as on a Trello card back; a card with a
  note shows the description icon (FR-43).
- Quick edit menu on each card (FR-69).
- Notes are never sent to Canvas (FR-44, NFR-12).

**Exit criteria:** notes survive reloads and Canvas refreshes, appear on a
second device, and a network
capture shows no note text going to Canvas.

### Phase 4: Polish and deploy

- Export notes and board as a file (FR-53); delete my data (FR-54).
- Accessibility and mobile layout pass (NFR-30 to NFR-33).
- Deploy to the chosen host (D-3) and link it from the repo's landing page.

**Exit criteria:** the deployed app works from a laptop and a phone;
accessibility checks pass.

### Phase 5: Later ideas (not committed)

- "Log in with Canvas" (OAuth 2) instead of pasting a token (D-4).
- Calendar view of due dates; reminders.
- Grades and submission feedback view.
- Personal cards and lists: "+ Add a card" creates a card that isn't a
  Canvas assignment, and "+ Add another list" adds lists; lists can also be
  archived (FR-71, FR-64, FR-36).
- Checklists inside a card, with progress such as 2/5 on the card front
  (FR-70).
- More than one board, such as one per course or term, as in Trello (FR-76).
- Board background choices and the board menu sidebar (FR-75).
- Parent view: a parent (Canvas *observer*) token shows the courses and
  assignments of the students they observe (Q-5).

## 4. Milestones

| ID | Milestone | Phase | Shows that |
|----|-----------|-------|------------|
| M0 | Empty app builds in CI | 0 | Tooling works end to end |
| M1 | First real assignment list | 1 | Canvas connection works |
| M2 | Viewer complete | 1 | MVP usable day to day |
| M3 | Board saves layout | 2 | Core organizing feature works |
| M4 | Notes complete | 3 | All user-requested features exist |
| M5 | Deployed with sync | 4 | Usable from any device |

## 5. Open decisions

These need the Team Lead's call. Each has a recommendation, but nothing is settled.

| ID | Decision | Options | Recommendation | Needed by |
|----|----------|---------|----------------|-----------|
| D-1 | Frontend framework | **React** (largest ecosystem, most tutorials, mature drag-and-drop libraries such as dnd-kit) or **Svelte** (less code, closer to QML's declarative feel, smaller community) | **Postponed** by the Team Lead (2026-10-25) until requirements and design are further along, since the features may change which fits best. Leaning React for learning resources and drag-and-drop support. | End of Phase 0 design |
| D-2 | Where notes and board layout are stored | **Browser local storage** (no accounts, works offline, but tied to one browser and lost if site data is cleared) or **server database** (follows the user between devices, but needs portal sign-in and more security work) | **Decided** (Team Lead, 2026-10-25): server database. The user should be able to sign in from anywhere and see their saved state. | Done |
| D-3 | Hosting | Frontend on **GitHub Pages**. Backend on **Render**, **Fly.io**, or **Vercel** serverless functions. All have free or cheap tiers with limits. | Decide in Phase 4; run locally until then. | Phase 4 |
| D-4 | How users connect to Canvas | **Personal access token** (works today, no school involvement, user must create and paste it) or **OAuth** (smooth sign-in, needs a developer key from the school's Canvas admin) | Token first; OAuth in Phase 5 if a school will issue a key. | Phase 0 |
| D-5 | Who the app is for | Just the Team Lead, a few friends, or any student at any school | Design for any school (the Canvas URL is a setting), test with one. | Phase 0 |
| D-6 | Backend language | **Python + FastAPI** (readable, quick to write, good for learning) or **Node.js** (same language as the frontend) | Python + FastAPI. | Phase 0 |
| D-7 | How users sign in to the portal | **Sign in with Google**, **email magic link**, **username and password**, or a **hosted auth service** (see [design](03-design.md#5-signing-in-to-the-portal-d-7)) | **Decided** (Team Lead, 2026-10-25): Sign in with Google for the MVP. | Done |

## 6. Risks

| ID | Risk | Effect | Mitigation |
|----|------|--------|------------|
| R-1 | The school has turned off personal access tokens | Phase 1 can't connect | Check early (Phase 0). Fallback: a free Canvas account from Instructure for testing; OAuth with the school later. |
| R-2 | Canvas tokens are powerful; a leak exposes a student's whole account | Privacy harm | Backend never logs tokens, stores them encrypted or not at all, and only uses read endpoints (NFR-10, NFR-11). |
| R-3 | Canvas rate limits slow down large accounts | Slow loading | Cache results, fetch courses in parallel within limits, show partial results (NFR-2). |
| R-4 | Assignments change in Canvas (renamed, deleted, new due date) | Board shows stale or orphaned cards | Match cards by Canvas assignment ID, not name; keep notes on deleted assignments in an "Archived" area (FR-35, FR-45). |
| R-5 | Learning web development alongside building | Slower progress | Small phases, one new technology at a time, docs explain terms. |
| R-6 | A school-managed Google account blocks sign-in to outside apps | Student can't sign in | Allow any Google account, so a personal one works; explain this on the sign-in screen. |
| R-7 | Matching Trello too closely in look (logo, artwork, exact styling) | Trademark or copyright complaint | Copy behavior and layout patterns only; our own name, colors, and icons (C-4). |

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
