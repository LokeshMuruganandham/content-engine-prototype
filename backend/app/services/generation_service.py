from uuid import uuid4

from sqlalchemy.orm import Session

from app.models.job import Job
from app.schemas.generate import GenerateRequest, GenerateResponse
from app.services.gemini_service import gemini_service


def create_generation_job(
    request: GenerateRequest,
    db: Session,
) -> GenerateResponse:

    try:
        enhanced_prompt = gemini_service.enhance_prompt(
            product_name=request.product_name,
            description=request.product_description,
        )
    except RuntimeError:
        enhanced_prompt = request.product_description

    job = Job(
        product_name=request.product_name,
        product_description=request.product_description,
        enhanced_prompt=enhanced_prompt,
        status="pending",
    )

    try:
        db.add(job)
        db.commit()
        db.refresh(job)

    except Exception:
        db.rollback()
        raise

    return GenerateResponse(
        job_id=str(job.id),
        status=job.status,
    )