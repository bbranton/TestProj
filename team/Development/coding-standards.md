# Coding standards

How code for the Canvas portal is written: the Python backend in
`canvas-portal/backend/` and the TypeScript and React frontend in
`canvas-portal/frontend/`. The
[Developer persona](/team/Development/personas/developer.md) owns this file
and decides what goes in it. Each rule is short and says why.

These rules cover how code is written inside the design. What the code
builds is in the [design](/docs/canvas-portal/03-design.md), what it must
do is in the [requirements](/docs/canvas-portal/02-requirements.md), and
which phase is in scope is in
[Canvas portal phases](/CLAUDE.md#canvas-portal-phases). Where this file and
the design differ, the design wins and the Developer fixes this file.

## Tools CI enforces

CI runs these on every PR that touches `canvas-portal/`, as
[`canvas-portal-ci.yml`](/.github/workflows/canvas-portal-ci.yml) says.
Fix any failure before asking for review. GitHub doesn't block a merge on
a failing check, since no check is required yet. Run the same commands
locally before pushing, so CI only confirms what you already saw.

| Part | Command | What it catches |
|------|---------|-----------------|
| Backend | `pip install -e ".[dev]"`, then `pytest` in `canvas-portal/backend` | Failing backend tests |
| Frontend | `npm ci`, then `npm test` in `canvas-portal/frontend` | Failing Vitest tests |
| Frontend | `npm run build` | Type errors, through `tsc -b` with `strict` on, and a broken Vite build |

CI uses Python 3.12 and Node 22; use the same locally.

The [docs check](/.github/workflows/docs-check.yml) also runs on every PR:
`python3 team/Development/scripts/docs_check.py`. It fails on a broken
repo link or an unknown requirement ID in any Markdown file.

**No formatter or linter runs yet.** Tools such as Ruff for Python, or
Prettier and ESLint for TypeScript, would be new dev dependencies, which
the [architect](/team/Development/personas/architect.md#decisions) takes to
the Team Lead before the DevOps engineer adds them to CI. Until then,
follow the style rules below by hand, and reviewers check them. The rules
match those tools' defaults, so adding a tool later changes little code.

## Style and format

Python:

- **Follow PEP 8, with 4-space indents and lines of at most 88
  characters.** It's what every Python reader expects, and 88 is Ruff's
  and Black's default.
- **Type-hint every function's arguments and return value.** FastAPI
  reads the hints to check requests and build the API docs, and they show
  mistakes before the code runs.
- **Give every module, public function, and class a docstring.** One line
  is enough when the name and hints already say most of it.
- **Test files are exempt from the docstring and return-hint rules,**
  except the requirement-ID docstring in [Tests](#tests). A test's name
  already says what it checks.

TypeScript and React:

- **Keep `strict` on, and don't use `any`.** Use `unknown` and narrow it.
  `any` turns off the type checks that CI relies on.
- **Use 2-space indents, double quotes, and semicolons,** as the existing
  code does, which is also Prettier's default.
- **Write function components with hooks, not classes.** It's how current
  React is written, and how its examples are.
- **Keep one component per file, with its test beside it,** such as
  `App.tsx` and `App.test.tsx`, as the
  [repository layout](/docs/canvas-portal/03-design.md#8-repository-layout)
  says. A reader finds the test without searching.

Both:

- **Comment why, not what.** The code says what it does. A comment says
  why it does it that way, or names the requirement ID it carries out.
- **Delete dead code instead of commenting it out.** Git keeps the
  history.

## Naming

- **Python:** `snake_case` for functions, variables, and modules,
  `PascalCase` for classes, and `UPPER_CASE` for constants.
- **TypeScript:** `camelCase` for functions and variables, `PascalCase` for
  components, types, and interfaces, and `UPPER_CASE` for constants. A
  component's file has the component's name, such as `CardFront.tsx`.
- **Use the [glossary](/docs/canvas-portal/glossary.md) words in names,**
  such as `card`, `board`, and `refresh`, so the code reads like the
  requirements. A new term goes in the glossary in the same PR.
- **Spell names out.** `assignment`, not `asgn`. Common short forms such as
  `id` and `url` are fine.

## Error handling

- **Return every API error in the design's one shape,**
  `{"error": "<code>", "message": "<text>"}`, with a code from the
  [Backend API](/docs/canvas-portal/03-design.md#4-backend-api) table. The
  frontend picks a screen by code, so a new code is a design change that
  goes to the architect first. When a case has no code yet, ask the
  architect for one before building it.
- **Raise the app's own error type with a design code, not
  `HTTPException(detail=...)`.** FastAPI's defaults don't use the shape:
  an unhandled exception returns a plain-text 500, and `HTTPException` and
  a bad request body (422) return `{"detail": ...}`.
- **Send every error through one app-level exception handler** for the
  app's error type, `HTTPException`, `RequestValidationError`, and any
  other `Exception`. It returns the shape, and logs unexpected errors with
  their stack trace, so no error reaches the frontend in another form.
- **Catch the narrowest exception you can handle, and only where you can
  handle it.** A bare `except:` or `catch {}` hides the bug and its stack
  trace.
- **Never swallow an error.** Handle it, or let it rise to the app-level
  handler.
- **Keep one course's failure to that course.** A Canvas error or timeout
  marks that course failed in the Refresh, as
  [Refresh progress](/docs/canvas-portal/03-design.md#refresh-progress-fr-16)
  says, and the rest carry on.
- **In the frontend, handle every request's error state.** A component
  that fetches shows the
  [UI specification](/docs/canvas-portal/04-ui-specification.md)'s words
  for each error code, never a blank screen. For `invalid_request` and
  `internal_error`, that's the
  [General error message](/docs/canvas-portal/04-ui-specification.md#general-error-message).
- **Never show the backend's `message` text or the error code on screen.**
  The frontend picks what to show by code, as the design says, so the
  backend's wording can change without changing a screen.

## Logging

- **Backend: log with Python's `logging` module, one logger per module
  (`logging.getLogger(__name__)`), never `print`.** Log levels and the
  token filter only work on the logging module.
- **Never log a Canvas token, cookie, session ID, or secret, and never
  put one in an error message,** as the
  [design's security table](/docs/canvas-portal/03-design.md#7-security)
  and NFR-10 say. Log IDs, not student data such as names or assignment
  text.
- **Never log a request body, a validation error's input values, the
  Google sign-in `code` and `state` values, or Google's tokens.**
  Exception text and stack traces count as log output. The token filter
  removes headers and fields named `token`, not free text inside an
  exception message, so the app-level handler logs the exception type and
  where it happened, not text that could hold what was sent.
- **Keep the Canvas token out of every URL, query string, and browser
  store.** Send it only in the body of `PUT /api/canvas/connection` and in
  the `Authorization` header to the saved Canvas host. In the frontend,
  clear it from component state once that request returns, and never put
  it in `localStorage`, `sessionStorage`, the URL, or a request library's
  cache. Give the token field `autocomplete="off"`, so form autofill and
  password managers don't keep it. These carry out
  NFR-10 and the design's security table: a URL ends up in history,
  server logs, and the `Referer` header.
- **Log each Canvas call's endpoint, page count, and time taken,** as
  [Making Canvas loads fast](/docs/canvas-portal/03-design.md#making-canvas-loads-fast-nfr-1-nfr-2-r-3)
  says. Those numbers are the TP-14 baseline.
- **Frontend: no `console.*` calls in merged code,** including
  `console.error` and `console.warn`. The browser console is visible to
  anyone at the screen, a logged request could hold the Canvas token the
  student is typing on S-2, and leftover logs bury real errors.

## Tests

The [test plan](/docs/canvas-portal/05-test-plan.md) says what is tested
and how; the test engineer owns it. For the unit tests the Developer
writes:

- **Name the requirement ID a test covers** in its name or docstring,
  such as `def test_missing_badge_stays_red_when_graded():` with
  `"""FR-65: ..."""`. The `trace-requirement` skill finds IDs in code, so
  a reviewer can see each ID the PR claims has a test.
- **Test that each endpoint hides another user's data.** Its tests ask
  for another user's ID and expect `not_found`, as NFR-12 and the
  design's security table say.
- **Write a test for every bug fix that fails before the fix.** It proves
  the fix and keeps the bug from coming back.
- **Never use a real Canvas token in a test.** Use the recorded sample
  data in `canvas-portal/backend/tests/fixtures/`, as NFR-41 and the
  [repository layout](/docs/canvas-portal/03-design.md#8-repository-layout)
  say. The folder arrives in Phase 1.
- **Clean recorded sample data before committing it.** Drop the
  `Authorization` header, and replace real names, courses, emails, and
  Canvas IDs with made-up ones. The repo is public, so a fixture is
  published the moment it's pushed. The reviewer checks the fixture diff
  for both.
- **Test one behavior per test, and keep tests independent.** A failing
  test then names the broken behavior, and tests can run in any order.
- **Find frontend elements by role and name,** such as
  `screen.getByRole("heading", { name: "Canvas Portal" })`, not by class or
  test ID. It's how a user, and a screen reader, finds them.

## Changing these standards

The Developer changes this file in a PR, reviewed as
[Who reviews what](/team/review-protocol.md#who-reviews-what) says. A rule
that adds a tool to CI also has the DevOps engineer, and one that touches
the design has the architect.
