from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import deps
from app.core.config import settings
from app.schemas.sche_base import DataResponse
from app.schemas.sche_user import UserDetail
from app.services.user_service import UserService

router = APIRouter()


@router.get("", response_model=DataResponse[UserDetail])
def login(db: Session = Depends(deps.get_db)):
    user_detail = UserService.detail_user(db=db, user_id=1)
    return DataResponse().success_response(data=user_detail)


