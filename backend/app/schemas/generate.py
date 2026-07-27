from pydantic import BaseModel


class GenerateRequest(BaseModel):
    product_name: str
    product_description: str

class GenerateResponse(BaseModel):
    job_id: str
    status: str