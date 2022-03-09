from fastapi import APIRouter, Depends

from app.auth0.auth_middleware import get_current_user
from app.schemas.sche_base import ResponseSchemaBase, DataResponse

router = APIRouter()


@router.get("", response_model=ResponseSchemaBase)
def health_check():
    return {
        "code": "000",
        "message": "Health check success"
    }


@router.get("/private")
def test(user=Depends(get_current_user)):
    return DataResponse().success_response(data=user)
