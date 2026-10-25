"""Canvas Assignments Portal backend.

Phase 0 skeleton: one health endpoint so CI can prove the app starts.
"""

from fastapi import FastAPI

app = FastAPI(title="Canvas Assignments Portal")


@app.get("/api/health")
def health() -> dict[str, str]:
    """Report that the backend is running."""
    return {"status": "ok"}
