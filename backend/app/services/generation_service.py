from uuid import uuid4
from sqlalchemy.orm import Session
from app.models.job import Job
from app.schemas.generate import GenerateRequest, GenerateResponse


def create_generation_job(
    request: GenerateRequest,
    db: Session,
) -> GenerateResponse:

    job = Job(
        product_name=request.product_name,
        product_description=request.product_description,
        status="pending",
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    return GenerateResponse(
        job_id=str(job.id),
        status=job.status,
    )