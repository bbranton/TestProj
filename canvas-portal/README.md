# Canvas Assignments Portal

The app described in [docs/canvas-portal](../docs/canvas-portal/README.md).
This is the Phase 0 skeleton: a backend with one health endpoint, and CI
that runs its tests on every pull request. The frontend arrives once the
framework is chosen (decision D-1).

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

## Settings

Copy `.env.example` to `.env` and fill it in. `.env` is git-ignored; never
commit tokens or secrets.
