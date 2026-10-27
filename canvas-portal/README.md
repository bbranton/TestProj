# Canvas Assignments Portal

The app described in [docs/canvas-portal](/docs/canvas-portal/README.md).
This is the Phase 0 skeleton: a FastAPI backend with one health endpoint,
a React + TypeScript frontend (built with Vite) with one page, and CI that
tests both on every pull request.

## Run the backend locally

Needs Python 3.12 or newer.

```sh
cd canvas-portal/backend
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
ruff format --check . && ruff check .
pytest
uvicorn app.main:app --reload
```

Then open <http://localhost:8000/api/health>, which answers
`{"status": "ok"}`, or <http://localhost:8000/docs> for the API docs that
FastAPI generates.

## Run the frontend locally

Needs Node.js 22 or newer. In a second terminal:

```sh
cd canvas-portal/frontend
npm install
npm run format:check && npm run lint
npm test
npm run dev
```

Then open the address Vite prints (usually <http://localhost:5173>). Calls
to `/api/...` are passed to the backend on port 8000.

## Format and lint

CI fails a PR whose code isn't formatted or has a lint problem, so run the
checks above before pushing. To fix formatting:

- Backend: `ruff format .`, and `ruff check --fix .` for the lint problems
  Ruff can fix itself. Ruff's settings are in `backend/pyproject.toml`.
- Frontend: `npm run format` runs Prettier. Fix ESLint problems by hand;
  its rules, including React hooks and no `console.*`, are in
  `frontend/eslint.config.js`.

Ruff and Prettier are pinned to one version, because a new version can
format code differently.

The frontend has two TypeScripts for now. ESLint's TypeScript parser
needs TypeScript 6 (`typescript`, kept below 6.1 as typescript-eslint
requires), and the app type-checks and builds with TypeScript 7
(`typescript7`) through `npm run build`. A bare `tsc` runs TypeScript 6,
so don't use it. Until the split ends, don't turn on typed linting
(`recommendedTypeChecked` or `parserOptions.projectService`), or ESLint
would type-check with a different compiler from the build. Once
typescript-eslint supports TypeScript 7, go back to one `typescript@7`
and a plain `tsc -b`.

## Settings

Copy `.env.example` to `.env` and fill it in. `.env` is git-ignored; never
commit tokens or secrets.
