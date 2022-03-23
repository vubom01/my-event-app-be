from fastapi import APIRouter, Depends

from app.schemas.sche_base import ResponseSchemaBase, DataResponse

router = APIRouter()


@router.get("", response_model=ResponseSchemaBase)
def health_check():
    return {
        "code": "000",
        "message": "Health check success"
    }
