from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.api import deps
from app.helpers.login_manager import login_required
from app.schemas.sche_base import DataResponse, ItemBaseModel
from app.schemas.sche_user import UserDetail, UserUpdateRequest
from app.services.srv_user import UserService

router = APIRouter()


class UpdatePassword(ItemBaseModel):
    current_password: str
    update_password: str


@router.get('/me', dependencies=[Depends(login_required)], response_model=DataResponse[UserDetail])
def detail(current_user: UserDetail = Depends(UserService.get_current_user)):
    return DataResponse().success_response(data=current_user)


@router.put('/me', dependencies=[Depends(login_required)])
def update(current_user: UserDetail = Depends(UserService.get_current_user), db: Session = Depends(deps.get_db),
           request: UserUpdateRequest = None):
    user = UserService.update_user(db=db, user=request, user_detail=current_user)
    return DataResponse().success_response(data=user)


@router.put('/me/password', dependencies=[Depends(login_required)])
def update_password(current_user: UserDetail = Depends(UserService.get_current_user),
                    db: Session = Depends(deps.get_db), password: UpdatePassword = None):
    user = UserService.update_password(db=db, current_password=password.current_password,
                                       update_password=password.update_password, user_detail=current_user)
    return DataResponse().success_response(data=user)

