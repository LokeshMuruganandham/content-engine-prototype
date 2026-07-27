
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db

from app.schemas.generate import (
    GenerateRequest,
    GenerateResponse,
)
from app.services.generation_service import create_generation_job

router = APIRouter()


@router.post(
    "/generate",
    response_model=GenerateResponse,
    status_code=201,
    tags=["Generation"],
)
def generate(
    request: GenerateRequest,
    db: Session = Depends(get_db),
):
    return create_generation_job(request, db)