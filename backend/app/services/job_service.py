from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.job import Job
from app.schemas.job import JobResponse


def get_job(job_id: str, db: Session) -> JobResponse:
    job_uuid = UUID(job_id)

    statement = (
        select(Job)
        .where(Job.id == job_uuid)
    )

    job = db.scalar(statement)

    if job is None:
        raise HTTPException(
            status_code=404,
            detail="Job not found",
        )

    return JobResponse(
        job_id=str(job.id),
        status=job.status,
        image_url=job.image_url,
    )