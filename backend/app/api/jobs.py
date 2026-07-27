
from fastapi import APIRouter

from app.schemas.job import JobResponse

router = APIRouter()


@router.get(
    "/jobs/{job_id}",
    response_model=JobResponse,
    tags=["Jobs"],
)
def get_job(job_id: str):
    return JobResponse(
        job_id=job_id,
        status="pending",
        image_url=None,
    )