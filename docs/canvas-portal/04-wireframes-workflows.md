# Wireframes and workflows

**Status:** Draft · **Owner:** Team Lead · **Last updated:** 2026-10-25

Wireframes are rough sketches of each screen: what is on it and where, not
colors or fonts. They are drawn here as text so they can be reviewed and
changed in pull requests. Workflows show how a user moves between screens to
get something done.

Screen IDs (`S-1`, `S-2`, ...) are used by the test procedures.

## 1. Screen map

```mermaid
flowchart TD
    S1[S-1 Sign in] --> Q{Canvas connected?}
    Q -- no --> S2[S-2 Connect Canvas]
    Q -- yes --> S3[S-3 Dashboard: list view]
    S2 --> S3
    S3 <--> S4[S-4 Dashboard: board view]
    S3 --> S5[S-5 Assignment detail and note]
    S4 --> S5
    S3 --> S6[S-6 Settings]
    S4 --> S6
    S6 -- disconnect --> S2
    S6 -- sign out --> S1
```

Every dashboard screen shares a top bar:

```text
+--------------------------------------------------------------------------+
| Canvas Portal      [ List | Board ]      Updated 3 min ago [Refresh]  [⚙] |
+--------------------------------------------------------------------------+
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

### S-3 Dashboard: list view

Requirements: FR-13, FR-20 to FR-26, NFR-20.

```text
+--------------------------------------------------------------------------+
| Canvas Portal      [*List*| Board ]      Updated 3 min ago [Refresh]  [⚙] |
+--------------------------------------------------------------------------+
| [!] Canvas isn't responding. Showing data from 10:42 AM.  <- NFR-20 only |
+-------------------+------------------------------------------------------+
| COURSES           | [ Search assignments...   ]  Status: [All      v]    |
| [x] All courses   | [x] Hide finished                                    |
| [ ] BIO 101       +------------------------------------------------------+
| [ ] HIST 210      | DUE SOON                                             |
| [ ] MATH 152      |  Lab report 3          BIO 101   Tue 11:59 PM  20 pt |
|                   |                                  [Due soon]   ✎   ↗  |
|                   |  Problem set 7         MATH 152  Wed 9:00 AM   10 pt |
|                   |                                  [Due soon]       ↗  |
|                   | UPCOMING                                             |
|                   |  Essay draft           HIST 210  Nov 3          50 pt |
|                   |                                  [Upcoming]   ✎   ↗  |
|                   | NO DUE DATE                                          |
|                   |  Reading reflection    HIST 210  —               5 pt |
|                   |                                  [Upcoming]       ↗  |
+-------------------+------------------------------------------------------+
  ✎ = has a note (FR-43)    ↗ = open in Canvas, new tab (FR-26)
  Clicking a row opens S-5.
```

### S-4 Dashboard: board view

Requirements: FR-30 to FR-37, NFR-3, NFR-31.

```text
+--------------------------------------------------------------------------+
| Canvas Portal      [ List |*Board*]      Updated 3 min ago [Refresh]  [⚙] |
+--------------------------------------------------------------------------+
| Course: [All courses v]                                  [+ Add column]  |
+------------------------+------------------------+------------------------+
| To do (3)          […] | In progress (1)    […] | Done (2)           […] |
+------------------------+------------------------+------------------------+
| +--------------------+ | +--------------------+ | +--------------------+ |
| | Problem set 7      | | | Lab report 3     ✎ | | | Quiz 4             | |
| | MATH 152           | | | BIO 101            | | | BIO 101            | |
| | Wed 9:00 AM  [Due  | | | Tue 11:59 PM       | | | [Graded]           | |
| |  soon]             | | | [Due soon]         | | +--------------------+ |
| +--------------------+ | +--------------------+ |                        |
| +--------------------+ |                        |                        |
| | Essay draft      ✎ | |                        |                        |
| | HIST 210  Nov 3    | |                        |                        |
| | [Submitted]        | |                        |                        |
| | Submitted. Move to | |  <- FR-37 hint,        |                        |
| | Done? [Move]       | |     never automatic    |                        |
| +--------------------+ |                        |                        |
| +--------------------+ |                        |                        |
| | NEW  Chapter 5 qs  | |  <- FR-34 new cards    |                        |
| | HIST 210  Nov 8    | |     land at bottom     |                        |
| +--------------------+ |                        |                        |
+------------------------+------------------------+------------------------+
| > Archived (1)    <- FR-45: assignments removed from Canvas              |
+--------------------------------------------------------------------------+
  […] column menu: Rename, Move left/right, Delete (FR-36)
  Keyboard: focus a card, Space to pick up, arrows to move, Space to drop,
  Escape to cancel (NFR-31).
```

### S-5 Assignment detail and note

Requirements: FR-22, FR-26, FR-40 to FR-44, FR-46. Opens as a side panel
over S-3 or S-4 on wide screens, and as a full screen on phones.

```text
                              +------------------------------------------+
                              | Lab report 3                         [x] |
                              | BIO 101 · Due Tue Oct 28, 11:59 PM       |
                              | 20 points · [Due soon]                   |
                              | [ Open in Canvas ↗ ]                     |
                              +------------------------------------------+
                              | MY NOTES (private, never sent to Canvas) |
                              | [B] [I] [•] [link]          <- FR-46     |
                              | +--------------------------------------+ |
                              | | Ask Dr. Lee about graph axes.        | |
                              | | Data is in the shared folder.        | |
                              | |                                      | |
                              | +--------------------------------------+ |
                              | Saved 10:51 AM            <- FR-42       |
                              |                         [Delete note]    |
                              +------------------------------------------+
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

### Phone layout

Requirement: NFR-33. Courses move into a filter menu, and the list takes the
full width. The board scrolls sideways one column at a time.

```text
+----------------------------+
| Canvas Portal   [⟳]  [⚙]  |
| [*List*| Board ]           |
| [Search...]   [Filters v]  |
+----------------------------+
| DUE SOON                   |
| Lab report 3            ✎  |
| BIO 101 · Tue 11:59 PM     |
| [Due soon]                 |
|----------------------------|
| Problem set 7              |
| MATH 152 · Wed 9:00 AM     |
| [Due soon]                 |
+----------------------------+
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
    I --> J[S-3 List view]
    J --> K[Board created with<br/>every assignment in To do]
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
    F->>F: Move card on screen immediately
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

### W-4 Write a note

```mermaid
flowchart TD
    A([Open assignment S-5]) --> B[Type in note box]
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
    E -- submitted but not in Done --> G[Show 'Move to Done?' hint]
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

## Change log

| Date | Change |
|------|--------|
| 2026-10-25 | First draft. |
