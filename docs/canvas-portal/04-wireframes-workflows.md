# Wireframes and workflows

**Status:** Draft · **Owner:** Team Lead · **Last updated:** 2026-10-25

Wireframes are rough sketches of each screen: what is on it and where, not
colors or fonts. They are drawn here as text so they can be reviewed and
changed in pull requests. Workflows show how a user moves between screens to
get something done.

Screen IDs (`S-1`, `S-2`, ...) are used by the test procedures.

## 1. Screen map

The layout follows Trello (goal G-3): the board is home, a card opens as a
dialog over the board, and menus open in place instead of on new pages.

```mermaid
flowchart TD
    S1[S-1 Sign in] --> Q{Canvas connected?}
    Q -- no --> S2[S-2 Connect Canvas]
    Q -- yes --> S4[S-4 Board, home screen]
    S2 --> S4
    S4 <--> S3[S-3 Table view]
    S4 --> S5[S-5 Card back dialog]
    S3 --> S5
    S4 --> S7[S-7 Quick edit menu]
    S4 --> S8[S-8 Filter menu]
    S4 --> S9[S-9 Board menu and archived items]
    S4 --> S6[S-6 Settings]
    S6 -- disconnect --> S2
    S6 -- sign out --> S1
```

Every signed-in screen shares a header bar, like Trello's board header. It
sits on the board's background color:

```text
+--------------------------------------------------------------------------+
| Canvas Portal  My assignments  [*Board*| Table ]   [Filter] [⟳] [⋯] (A)  |
+--------------------------------------------------------------------------+
  [Filter] opens S-8. [⟳] refreshes from Canvas; hovering shows "Updated 3 min
  ago". [⋯] opens S-9. (A) is the account menu: Settings, Sign out.
```

## 2. Screens

### S-1 Sign in

Requirements: FR-50, D-7. Shown when no one is signed in.

```text
+--------------------------------------------------+
|                                                  |
|                 Canvas Portal                    |
|                                                  |
|   All your Canvas assignments in one place,      |
|   on a board you can arrange, with your own      |
|   private notes.                                 |
|                                                  |
|          [  G  Sign in with Google  ]            |
|                                                  |
|   We only read from Canvas. We never change      |
|   anything there.                                |
+--------------------------------------------------+
```

### S-2 Connect Canvas

Requirements: FR-1 to FR-3, FR-6. Shown after first sign-in, after
disconnecting, or when Canvas rejects the saved token.

```text
+--------------------------------------------------------------+
|  Connect your Canvas account                                 |
|                                                              |
|  [!] Canvas no longer accepts your saved token.   <- FR-6,   |
|      Please create a new one. Your board and         shown   |
|      notes are safe.                                 only on |
|                                                      error   |
|  School Canvas address                                       |
|  [ https://myschool.instructure.com            ]             |
|                                                              |
|  Access token                                                |
|  [ ••••••••••••••••••••••••••••••••••          ] [show]      |
|                                                              |
|  > How do I get a token?                       <- expands    |
|    1. In Canvas, open Account, then Settings.                |
|    2. Under Approved Integrations, choose                    |
|       New Access Token.                                      |
|    3. Enter a purpose such as "Canvas Portal"                |
|       and generate it.                                       |
|    4. Copy the token and paste it here. Canvas               |
|       only shows it once.                                    |
|                                                              |
|                                  [ Connect ]                 |
+--------------------------------------------------------------+
```

On success the portal shows "Connected as *Name*" (FR-2) and opens S-3.

### S-3 Table view

Requirements: FR-13, FR-20 to FR-26, FR-30, FR-65, FR-78, NFR-20. In Phase 1 this
is the only view. From Phase 2 it is the secondary view behind the board.
Each row uses the same label colors and due badges as the cards.

```text
+--------------------------------------------------------------------------+
| Canvas Portal  My assignments  [ Board |*Table*]   [Filter] [⟳] [⋯] (A)  |
+--------------------------------------------------------------------------+
| [● BIO 101] [● HIST 210] [● MATH 152] [○ ART 120]  [Show all] [Hide all] |
+--------------------------------------------------------------------------+
| [!] Canvas isn't responding. Showing data from 10:42 AM.  <- NFR-20 only |
+--------------------------------------------------------------------------+
| Card               | List         | Label      | Due          | Points   |
|--------------------+--------------+------------+--------------+----------|
| Lab report 3     ≡ | In progress  | ■ BIO 101  | (◷ Tue 11:59)| 20       |
|                    |              |            |   yellow     |          |
| Problem set 7      | To do        | ■ MATH 152 | (◷ Wed 9:00) | 10       |
|                    |              |            |   yellow     |          |
| Essay draft      ≡ | To do        | ■ HIST 210 | (◷ Nov 3)    | 50       |
| Reading reflection | To do        | ■ HIST 210 | none         | 5        |
+--------------------------------------------------------------------------+
  ≡ = has a description (note), FR-43. ■ = course label color, FR-66.
  Clicking a row opens S-5. The List column appears from Phase 2.
  The course buttons are the same as on the board, and hiding a course on one
  view hides it on the other (FR-78).
```

### S-4 Board (home screen)

Requirements: FR-31 to FR-36, FR-60 to FR-66, FR-72 to FR-74, FR-77, FR-78,
NFR-3, NFR-31, NFR-34.

```text
+--------------------------------------------------------------------------+
| Canvas Portal  My assignments  [*Board*| Table ]   [Filter] [⟳] [⋯] (A)  |
+--------------------------------------------------------------------------+
| [● BIO 101] [● HIST 210] [● MATH 152] [○ ART 120]  [Show all] [Hide all] |
+--------------------------------------------------------------------------+
|  board background color                                                  |
|  +--------------------+ +--------------------+ +--------------------+    |
|  | To do          […] | | In progress    […] | | Done           […] |    |
|  | +----------------+ | | +----------------+ | | +----------------+ |    |
|  | | ▬▬ MATH 152    | | | | ▬▬ BIO 101     | | | | ▬▬ BIO 101     | |    |
|  | | Problem set 7  | | | | Lab report 3   | | | | Quiz 4         | |    |
|  | | (◷ Wed 9:00) ✎ | | | | (◷ Tue 11:59)  | | | | (◷ Oct 20 ✓)   | |    |
|  | +----------------+ | | | ≡  ☑ 2/5       | | | +----------------+ |    |
|  | +----------------+ | | +----------------+ | | + Add a card       |    |
|  | | ▬▬ HIST 210    | | | ┌ ─ ─ ─ ─ ─ ─ ─ ┐  | +--------------------+    |
|  | | Essay draft:   | | | │   drop gap    │  |                           |
|  | | causes of WWI  | | | │   (FR-77)     │  | +--------------------+    |
|  | | (◷ Nov 3) ≡    | | | └ ─ ─ ─ ─ ─ ─ ─ ┘  | | + Add another list |    |
|  | | ☑ 1/3          | | | + Add a card       | +--------------------+    |
|  | |                | | +--------------------+                           |
|  | +----------------+ |                                                  |
|  | +----------------+ |                                                  |
|  | | ▬▬ HIST 210    | | <- FR-34: new Canvas assignments land at         |
|  | | NEW            | |    the bottom of To do                           |
|  | | Chapter 5 qs   | |                                                  |
|  | +----------------+ |                           ──scrolls──>           |
|  | + Add a card       | <- FR-71: personal card (Phase 3)                |
|  +--------------------+                                                  |
+--------------------------------------------------------------------------+
  Course buttons (FR-78): one per active course, in its label color. ● shown,
  ○ hidden; tapping one hides or shows that course's cards. [Show all] and
  [Hide all] show or hide every course at once. With every course hidden, the
  board says "All courses are hidden" with a Show all link. Hidden cards keep
  their list and position.
  ▬▬ label strip in the course color (FR-66). (◷ ...) due badge: yellow due
  soon, red overdue, green with ✓ when complete (FR-65). ≡ has a description.
  ✎ is shown here on the card the mouse is over.
  ☑ 2/5 checklist progress (FR-70). ✎ appears on hover and opens S-7.
  List title: click to rename (FR-63). Drag a list by its header (FR-62).
  […] list menu: Add card, Move list, Archive list (FR-36).
  Cards move between lists only when the student drags them; the portal never
  moves a card on its own, even when Canvas marks it submitted.
```

### S-5 Card back

Requirements: FR-22, FR-26, FR-40 to FR-44, FR-46, FR-67, FR-68, FR-70.
Opens as a dialog over the dimmed board at `/c/{cardId}`. On phones it fills
the screen.

```text
+--------------------------------------------------------------------------+
| (dimmed board behind)                                                    |
|   +------------------------------------------------------------------+   |
|   | ▭ Lab report 3                                              [x]  |   |
|   |   in list In progress  <- click to move                          |   |
|   |                                                                  |   |
|   | Labels          Due date                       | Add to card     |   |
|   | [■ BIO 101]     [ ] Tue Oct 28, 11:59 PM       | [☑ Checklist]   |   |
|   |                 (Due soon)                     |                 |   |
|   | 20 points · Not submitted                      | Actions         |   |
|   |                                                | [→ Move      ]  |   |
|   | ≡ Description            private, never sent   | [↗ Open in   ]  |   |
|   |                          to Canvas             | [   Canvas   ]  |   |
|   | +------------------------------------------+   | [▤ Archive   ]  |   |
|   | | Ask Dr. Lee about graph axes.            |   |                 |   |
|   | | Data is in the shared folder.            |   |                 |   |
|   | +------------------------------------------+   |                 |   |
|   | Saved 10:51 AM                     [Edit]      |                 |   |
|   |                                                |                 |   |
|   | ☑ Checklist                 2/5   [Delete]     |                 |   |
|   | [=====-------]  40%                            |                 |   |
|   | [x] Collect data                               |                 |   |
|   | [x] Draw graphs                                |                 |   |
|   | [ ] Write discussion                           |                 |   |
|   | [ ] Proofread                                  |                 |   |
|   | [ ] Submit in Canvas                           |                 |   |
|   | [Add an item]                                  |                 |   |
|   +------------------------------------------------------------------+   |
+--------------------------------------------------------------------------+
  The due-date checkbox is display only for Canvas cards: completion comes
  from Canvas. Personal cards can be checked off. Escape, [x], clicking
  outside, or the browser's Back button closes the dialog.
```

### S-6 Settings

Requirements: FR-4, FR-53, FR-54.

```text
+--------------------------------------------------------------+
| Settings                                                     |
|                                                              |
| Canvas                                                       |
|   Connected as Alex S. at myschool.instructure.com           |
|   [ Disconnect Canvas ]                                      |
|                                                              |
| Your data                                                    |
|   [ Export board and notes (.json) ]                         |
|   [ Delete my account and all data ]   <- asks to confirm    |
|                                                              |
| Account                                                      |
|   Signed in as alex@example.com        [ Sign out ]          |
+--------------------------------------------------------------+
```

### S-7 Quick edit menu

Requirements: FR-69. Opens from the ✎ button on hover, by right-clicking a
card, or by pressing `e`. The card is shown raised, with a menu beside it,
as in Trello.

```text
+--------------------------------------------------------------+
| (dimmed board)                                               |
|   +------------------+  +------------------------+           |
|   | ▬▬ BIO 101       |  | [▭ Open card        ]  |           |
|   | Lab report 3     |  | [→ Move             ]  |           |
|   | (◷ Tue 11:59) ≡  |  | [■ Change label color] |           |
|   | ☑ 2/5            |  | [↗ Open in Canvas   ]  |           |
|   +------------------+  | [▤ Archive          ]  |           |
|                         +------------------------+           |
+--------------------------------------------------------------+
```

### S-8 Filter menu

Requirements: FR-72. A dropdown under the Filter button, opened with `f`.

```text
+------------------------------------------+
| Filter                               [x] |
| Keyword                                  |
| [ Enter a keyword...                 ]   |
|                                          |
| Due date                                 |
| [ ] No dates                             |
| [ ] Overdue                    (red)     |
| [ ] Due in the next day        (yellow)  |
| [ ] Due in the next week                 |
| [ ] Due in the next month                |
| [ ] Marked as complete         (green)   |
|                                          |
| Labels                                   |
| [ ] ■ BIO 101                            |
| [ ] ■ HIST 210                           |
| [ ] ■ MATH 152                           |
+------------------------------------------+
  With a filter on, the header shows
  [Filter · 3 cards match  (x) Clear], and x clears it.
```

### S-9 Board menu and archived items

Requirements: FR-74, FR-75. A panel that slides in from the right edge of the
board.

```text
                          +------------------------------------+
                          | Menu                           [x] |
                          |------------------------------------|
                          | [▤ Archived items]                 |
                          | [■ Labels]            (Phase 5)    |
                          | [▧ Change background] (Phase 5)    |
                          |------------------------------------|
                          | Archived items                     |
                          | [Search archive...]  [Cards|Lists] |
                          | +--------------------------------+ |
                          | | ▬▬ BIO 101                     | |
                          | | Old lab (removed from Canvas)  | |
                          | +--------------------------------+ |
                          | [Restore]  ≡ note kept             |
                          +------------------------------------+
  Cards for assignments removed from Canvas land here (FR-45).
  Restore puts a card back at the bottom of its old list.
```

### Phone layout

Requirement: NFR-33. As in Trello's phone layout, one list fills the screen.
The user swipes sideways between lists, and dots show which list is shown.

```text
+----------------------------+
| ‹  My assignments  [⚲] [⋯] |
+----------------------------+
| [● BIO] [● HIST] [○ MATH] ›|
+----------------------------+
| In progress            […] |
| +------------------------+ |
| | ▬▬ BIO 101             | |
| | Lab report 3           | |
| | (◷ Tue 11:59) ≡ ☑ 2/5  | |
| +------------------------+ |
| +------------------------+ |
| | ▬▬ MATH 152            | |
| | Problem set 7          | |
| | (◷ Wed 9:00)           | |
| +------------------------+ |
| + Add a card               |
|                            |
|          ○ ● ○ ○           |
+----------------------------+
  The course buttons scroll sideways when they don't fit; Show all and Hide
  all are at the end of the row (FR-78).
  To move a card, press and hold it, then drag it to a screen edge to go
  to the next list, or use Move on the card back.
```

## 3. Workflows

### W-1 First-time setup

```mermaid
flowchart TD
    A([Open portal]) --> B[S-1 Sign in with Google]
    B --> C[S-2 Connect Canvas]
    C --> D[Enter school address and token]
    D --> E{Backend checks token<br/>with Canvas}
    E -- rejected --> F[Show 'Canvas did not accept<br/>this token' and keep the form]
    F --> D
    E -- address unreachable --> G[Show 'Couldn't reach that<br/>Canvas address']
    G --> D
    E -- accepted --> H[Show 'Connected as Name']
    H --> I[Fetch courses and assignments]
    I --> J[Board created: To do, In progress, Done;<br/>every assignment in To do]
    J --> K[S-4 Board]
```

### W-2 Daily check

```mermaid
flowchart TD
    A([Open portal on any device]) --> B{Signed in?}
    B -- no --> C[S-1 Sign in] --> D
    B -- yes --> D[Load cached data, page usable<br/>within 2 s, NFR-1]
    D --> E{Cache older<br/>than 5 min?}
    E -- yes --> F[Refresh from Canvas in background]
    E -- no --> G[Show data]
    F --> H{Canvas OK?}
    H -- yes --> G
    H -- token rejected --> I[S-2 with expired-token message]
    H -- down or rate limited --> J[Show cached data<br/>with warning banner]
```

### W-3 Move a card

```mermaid
sequenceDiagram
    actor U as User
    participant F as Frontend
    participant A as Backend

    U->>F: Drag "Lab report 3" to In progress
    F->>F: Card lifts and tilts, a gray gap shows the drop spot
    U->>F: Drop
    F->>F: Card settles into place immediately
    F->>A: PATCH /api/board/cards/{id}
    alt saved
        A-->>F: 200 OK
    else failed
        A-->>F: error
        F->>F: Move card back, show "Couldn't save, try again"
    end
```

Moving the card on screen before the server answers is called an
*optimistic update*. It keeps dragging fast (NFR-3), and the card snaps back
if the save fails, so the screen never shows a state the server doesn't have.

### W-4 Write a note (card description)

```mermaid
flowchart TD
    A([Open card back S-5]) --> B[Select Description and type]
    B --> C[Wait until 1 s after<br/>the last keystroke]
    C --> D[PUT /api/notes/id]
    D --> E{Saved?}
    E -- yes --> F[Show 'Saved 10:51 AM']
    E -- no --> G[Show 'Not saved, retrying'<br/>and keep the text on screen]
    G --> D
    F --> H{Close panel}
    G --> H
    H -- unsaved text --> I[Warn before closing]
```

### W-5 Assignment changes in Canvas

```mermaid
flowchart TD
    A([Refresh from Canvas]) --> B{For each Canvas assignment}
    B -- has a card --> C[Keep column and position;<br/>update name and due date shown]
    B -- no card yet --> D[Add card at bottom of To do<br/>with NEW badge]
    A --> E{For each card}
    E -- assignment gone from Canvas --> F[Mark card archived;<br/>keep its note]
    E -- submitted in Canvas --> G[Due badge turns green;<br/>card stays where the student put it]
```

### W-6 Disconnect and delete data

```mermaid
flowchart TD
    A([S-6 Settings]) --> B{Which action?}
    B -- Disconnect Canvas --> C[Delete stored token] --> D[S-2 Connect Canvas<br/>board and notes kept]
    B -- Export --> E[Download JSON file]
    B -- Delete account --> F[Confirm: type DELETE]
    F --> G[Remove user, token, board,<br/>notes, cache] --> H[S-1 Sign in]
```

### W-7 Shape the board (lists)

```mermaid
flowchart TD
    A([Board]) --> B{What does the user do?}
    B -- "+ Add another list" --> C[Type the name, press Enter]
    C --> D[List added at the end;<br/>composer stays open for another]
    B -- click list title --> E[Title becomes a text box]
    E -- Enter or click away --> F[Saved]
    E -- Escape --> G[Unchanged]
    B -- drag list header --> H[Other lists slide aside;<br/>drop saves the new order]
    B -- list menu: Archive list --> I[List and its cards move<br/>to Archived items]
    I --> J[S-9: Restore brings both back]
```

### W-8 Add a personal card (Phase 3, Q-6)

```mermaid
flowchart TD
    A([+ Add a card at the bottom of a list]) --> B[Text box opens in place]
    B --> C{Key pressed}
    C -- Enter --> D[Card added; box stays open<br/>for the next card]
    D --> B
    C -- Escape --> E[Box closes; nothing added]
    D --> F[Open the card to add a due date,<br/>description, or checklist]
```

## Change log

| Date | Change |
|------|--------|
| 2026-10-25 | First draft. |
| 2026-10-25 | Trello goal (G-3): board is home; S-3 becomes Table view; S-4 and S-5 redrawn as Trello board and card back; added S-7 quick edit, S-8 filter, S-9 board menu; Trello-style phone layout; W-7 and W-8 added. |
| 2026-10-25 | Added the course show/hide button row under the header on S-3, S-4, and the phone layout (FR-78), from the Team Lead's review. |
| 2026-10-25 | Added Hide all next to Show all on the course button row (FR-78). |
| 2026-10-25 | Removed the "Move to Done?" hint (FR-37) from S-4 and W-5; students drag cards to Done themselves. |
