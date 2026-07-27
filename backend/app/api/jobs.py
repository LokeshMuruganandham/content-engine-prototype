
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.job_service import get_job
from app.schemas.job import JobResponse

router = APIRouter()


@router.get(
    "/jobs/{job_id}",
    response_model=JobResponse,
    tags=["Jobs"],
)
def get_job_endpoint(
    job_id: str,
    db: Session = Depends(get_db),
):
    return get_job(job_id, db)