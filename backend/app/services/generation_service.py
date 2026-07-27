from uuid import uuid4

from app.schemas.generate import GenerateResponse


def create_generation_job() -> GenerateResponse:
    """
    Create a placeholder generation job.

    Later this function will:
    - Enhance the prompt using Gemini
    - Generate an image using ComfyUI
    - Store metadata in PostgreSQL
    - Upload images to Supabase Storage
    """

    return GenerateResponse(
        job_id=str(uuid4()),
        status="pending",
    )