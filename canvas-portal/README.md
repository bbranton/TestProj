# Canvas Assignments Portal

The app described in [docs/canvas-portal](../docs/canvas-portal/README.md).
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
npm test
npm run dev
```

Then open the address Vite prints (usually <http://localhost:5173>). Calls
to `/api/...` are passed to the backend on port 8000.

## Settings

Copy `.env.example` to `.env` and fill it in. `.env` is git-ignored; never
commit tokens or secrets.
