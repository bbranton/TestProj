# User Interface Specification: Phase 0

**Status:** Draft · **Owner:** Team Lead · **Last updated:** 2026-11-02

This file specifies the user interface of Phase 0's local proof of
concept: one page, S-0, that runs only on the student's own computer.
The UI specification is split into one file per phase.
Phase 1 and the sketches of later phases are in
[UI specification: Phase 1](/docs/canvas-portal/04-ui-specification_phase1.md),
which replaces S-0 with sign-in and the board.

Wireframes are rough sketches drawn as text, so they can be reviewed and
changed in pull requests. Screen and button IDs are used by the design
and the test procedures. Terms are defined in the
[glossary](/docs/canvas-portal/glossary.md).

## 1. Conventions

S-0 follows the Phase 1 file's
[Conventions on every screen](/docs/canvas-portal/04-ui-specification_phase1.md#conventions-on-every-screen)
where they apply to one page with no buttons:

- **Color is never the only signal:** every message starts with [!] and
  says what happened in words.
- **Messages are announced:** screen readers read each message out when
  it appears.
- **Dates and times** are written "Oct 28, 11:59 PM", in the computer's
  time zone (FR-22).
- **Messages say what happened and what to do next,** in plain words, and
  never show error codes or the token.
- **Mouse and touch, not keyboard shortcuts:** the only action is
  selecting a card, which is a real browser link, so Tab and screen
  readers reach it.

Button IDs on S-0:

| ID | Label | Screen | Shown as |
|----|-------|--------|----------|
| `OPEN_IN_CANVAS` | *Assignment name*, opens in Canvas | S-0 | The whole card |

## 2. Screens

### S-0 Assignment list (Phase 0)

Requirements: as the requirements index marks them for Phase 0, from the
[roadmap's Phase 0](/docs/canvas-portal/01-roadmap.md#phase-0-setup-and-local-proof-of-concept):
the student's name (FR-2), every assignment from the active courses
(FR-10 to FR-12, FR-21) with its name, course, and due date (FR-22),
sorted by due date (FR-38), each linking to Canvas (FR-26), a message
when there is nothing to show (FR-20) or Canvas can't be used (FR-17),
and no token anywhere on the page (NFR-10). Constraint C-5; decision
D-14.

The local proof of concept's only page. The student starts the portal on
their own computer as the README says, then opens it in their browser at
`localhost`. There is no sign-in, no connect screen, and no header bar:
the Canvas address and token come from the `.env` file, set up by hand.
The page is plain HTML and CSS: one column of simple cards, like Phase
1's Backlog list, with only the fields below.

```text
+--------------------------------------------------------------------+
|  Canvas Portal                                                     |
|  Assignments for Sam Student                                       |
|  Each assignment opens in Canvas in a new tab.                     |
|                                                                    |
|  [!] Couldn't load the assignments for ART 105. The other courses  |
|      are shown. Reload the page to try again.                      |
|                                                                    |
|  +--------------------------------------------------------------+  |
|  | ▬▬ HIST 210                                                  |  |
|  | Chapter 4 questions                                          |  |
|  | (◷ Oct 20, 11:59 PM)                                         |  |
|  +--------------------------------------------------------------+  |
|  +--------------------------------------------------------------+  |
|  | ▬▬ BIO 101                                                   |  |
|  | Lab report 2                                                 |  |
|  | (◷ Oct 22, 11:59 PM)                                         |  |
|  +--------------------------------------------------------------+  |
|  +--------------------------------------------------------------+  |
|  | ▬▬ BIO 101                                                   |  |
|  | Lab report 3                                                 |  |
|  | (◷ Oct 28, 11:59 PM)                                         |  |
|  +--------------------------------------------------------------+  |
|  +--------------------------------------------------------------+  |
|  | ▬▬ HIST 210                                                  |  |
|  | Reading reflection                                           |  |
|  | (no due date)                                                |  |
|  +--------------------------------------------------------------+  |
+--------------------------------------------------------------------+
  "Canvas Portal" is the page's heading. "Assignments for *Name*" uses
  the student's Canvas name (FR-2), so a token for the wrong account is
  easy to spot. The line under it says what selecting a card does.
  The page fetches everything from Canvas each time it loads. There is
  no Refresh button: to fetch again, the student reloads the page with
  the browser's own reload button. Refresh, the "Synced" time, Refresh
  progress (S-10), and a saved copy to fall back on arrive in Phase 1.
  One card per assignment, from every active course, in one column.
  Cards are sorted by due date, earliest at the top; assignments with no
  due date come last and say "(no due date)". Cards with the same due
  date, or no due date, are in name order (FR-38). Past due dates stay
  in their place.
  Card fronts, top to bottom, as on Phase 1's S-4 cards: the ▬▬ label
  strip with the course code, such as "BIO 101", in white on the neutral
  Slate strip color (`#455A64`, 7.2:1 contrast with white, from Phase
  1's course label colors); the assignment name; and the due badge,
  plain, with the date and time written as on every screen, "Oct 28,
  11:59 PM", in the computer's time zone (FR-22).
  Points, submission types, statuses, the Missing highlight, green or red
  badges, and the Opens and Closed lines aren't shown: they arrive with
  the board in Phase 1.
  The whole card (`OPEN_IN_CANVAS`) is one link that opens the
  assignment in Canvas in a new tab (FR-26). Its name for screen readers
  is the assignment name, then the course code and due date, ending with
  "opens in a new tab", so each card is read as one item and a student
  who moves straight to a card still hears where it goes. The cards are a
  real HTML list, so screen readers say how many there are. A card keeps
  a visible focus outline when it's reached with Tab; the browser's own
  outline is fine, as long as the card styling doesn't remove it.
  The card styling is kept to what makes them read as cards: a white
  card with a thin gray border and a little rounding, space inside and
  between cards, and the Slate strip. The page uses the browser's own
  font on a white background, with no board background color. The page
  runs on the student's computer, so it's laid out for a computer's
  window, with the column at most about 640 px wide so names stay easy
  to read; long names wrap inside the card, and it still reads at 200%
  zoom.
```

Messages on the page. Each shows above the cards, starts with [!] so the
words are never only shown by color, is read out by screen readers when
it appears, and says what to do next. None shows the token, the Canvas
address, Canvas's own error text, or an error code.
"Assignments for *Name*" shows above the message only when Canvas has
accepted the token: with a course that failed, no active courses, or no
assignments, which is when a token for the wrong account is easiest to
spot (FR-2). The other messages show without it.

| When | The page shows |
|------|----------------|
| The page is fetching from Canvas | "Loading your assignments from Canvas..." in place of the cards. |
| `.env` has no Canvas address or no token | "The portal isn't set up yet. Add your Canvas address and token to your .env file, as the README says, then restart the portal." No cards. |
| Canvas rejects the token (FR-17) | "Canvas didn't accept the token in your .env file. Create a new token in Canvas, put it in your .env file, then restart the portal, as the README says." No cards. |
| The Canvas address in `.env` doesn't start with `https://`, so the portal refuses it before calling Canvas (NFR-15) | "The Canvas address in your .env file must start with https://. Fix it in your .env file, then restart the portal." No cards. |
| The Canvas address can't be reached | "Couldn't reach Canvas at the address in your .env file. Check that you're online, then reload the page. If the address is wrong, fix it in your .env file and restart the portal." No cards. |
| Canvas redirects the portal, or gives it a paging link, to another address, which the portal refuses so the token stays safe (NFR-15) | "Canvas sent the portal to a different address, so it stopped to keep your token safe. Check the Canvas address in your .env file, then restart the portal." No cards. When this happens while fetching one course's assignments, that course counts as failed and the row for courses that couldn't be fetched applies instead. |
| Canvas doesn't answer in time | "Canvas didn't answer in time. Reload the page to try again." No cards. |
| One or more courses' assignments couldn't be fetched, but others could | "Couldn't load the assignments for ART 105. The other courses are shown. Reload the page to try again." With more than one, it names each: "Couldn't load the assignments for 2 courses: ART 105, SPAN 201. ..." The cards show every other course's assignments. |
| Canvas has no active courses for this account | "Canvas shows no active courses for this account. If that's not right, check that the token in your .env file is from your own Canvas account." No cards. |
| Active courses, but none has assignments | "No assignments in your courses yet." No cards. |
| The portal itself fails, not Canvas | "Something went wrong in the portal, so your assignments didn't load. Reload the page to try again." No cards. |

How long "in time" is, and which checks the portal makes before calling
Canvas, are set in the [design](/docs/canvas-portal/03-design.md#design-by-phase).
The setup and token messages say to restart the portal because `.env` is
read when it starts; if the design reads it on every load instead, they
say "then reload the page".

## Change log

| Date | Change |
|------|--------|
| 2026-11-02 | Created when the UI specification was split by phase, from the Team Lead. Added S-0, the Phase 0 local proof of concept's one page: one column of simple cards (course code strip, name, due date) for every assignment, sorted by due date, with the student's name, links that open in Canvas, and a message for each error, including one course failing, Canvas not answering in time, an `http` address, and a redirect to another address. It fetches from Canvas on each page load, with no Refresh button (Phase 1). From the Team Lead's Phase 0 rescope (roadmap PR #158, D-14) and the Team Lead's choice of simple cards like Phase 1's Backlog. |
