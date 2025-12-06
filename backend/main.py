from fastapi import FastAPI

from .config import get_settings

settings = get_settings()

app = FastAPI(title=settings.app_name)


@app.get("/health")
def read_health() -> dict[str, str]:
    """Simple health check endpoint."""
    return {"status": "ok"}
