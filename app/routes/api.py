from app.routes.v1 import recruiter
from fastapi import APIRouter

router = APIRouter()
router.include_router(recruiter.router, tags=["recruiter"], prefix="/recruiter")
