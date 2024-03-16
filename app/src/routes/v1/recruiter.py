from app.src.schemas.email import EmailSchema
from fastapi import APIRouter

router = APIRouter()


@router.post("/register/email")
async def register_email_recruiter(email: EmailSchema) -> dict:
    return {"data": email.email}
