from fastapi import FastAPI

from app.api.generate import router as generate_router
from app.api.health import router as health_router
from app.api.jobs import router as jobs_router

app = FastAPI(
    title="Content Engine Prototype API",
    description="Backend API for content generation prototype.",
    version="1.0.0",
)

app.include_router(health_router)
app.include_router(generate_router)
app.include_router(jobs_router)