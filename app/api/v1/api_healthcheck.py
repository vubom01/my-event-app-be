from fastapi import APIRouter

from app.schemas.sche_base import ResponseSchemaBase

router = APIRouter()


@router.get("", response_model=ResponseSchemaBase)
def health_check():
    return {
        "code": "000",
        "message": "Health check success"
    }
