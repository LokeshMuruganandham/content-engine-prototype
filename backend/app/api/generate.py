from fastapi import APIRouter

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
def generate(request: GenerateRequest):
    return create_generation_job()