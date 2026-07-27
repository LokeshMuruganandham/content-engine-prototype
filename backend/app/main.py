from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.generate import router as generate_router
from app.api.health import router as health_router
from app.api.jobs import router as jobs_router
from app.core.database import Base, engine

# Import models so SQLAlchemy registers them
from app.models.job import Job


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create database tables on startup
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Content Engine Prototype API",
    description="Backend API for content generation prototype.",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(health_router)
app.include_router(generate_router)
app.include_router(jobs_router)