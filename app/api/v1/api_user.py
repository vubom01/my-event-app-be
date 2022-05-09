from typing import Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.api import deps
from app.helpers.login_manager import login_required
from app.helpers.paging import PaginationParamsRequest
from app.schemas.sche_base import DataResponse, ItemBaseModel
from app.schemas.sche_user import UserDetail, UserUpdateRequest, ListUser
from app.services.srv_user import UserService

router = APIRouter()


class UpdatePassword(ItemBaseModel):
    current_password: str
    update_password: str


@router.get('/me', dependencies=[Depends(login_required)], response_model=DataResponse[UserDetail])
def detail(current_user: UserDetail = Depends(login_required)):
    return DataResponse().success_response(data=current_user)


@router.put('/me', dependencies=[Depends(login_required)])
def update(current_user: UserDetail = Depends(login_required), db: Session = Depends(deps.get_db),
           request: UserUpdateRequest = None):
    user = UserService.update_user(db=db, user=request, user_detail=current_user)
    return DataResponse().success_response(data=user)


@router.put('/me/password', dependencies=[Depends(login_required)])
def update_password(current_user: UserDetail = Depends(login_required),
                    db: Session = Depends(deps.get_db), password: UpdatePassword = None):
    user = UserService.update_password(db=db, current_password=password.current_password,
                                       update_password=password.update_password, user_detail=current_user)
    return DataResponse().success_response(data=user)


@router.get('', dependencies=[Depends(login_required)], response_model=DataResponse[ListUser])
def get_list_users(db: Session = Depends(deps.get_db), query_params: Optional[str] = None,
                   pagination: PaginationParamsRequest = Depends(), current_user: UserDetail = Depends(login_required)):
    users = UserService.get_list_users(db=db, query_params=query_params, user_id=current_user.id,
                                       page=pagination.page, page_size=pagination.page_size)
    return DataResponse().success_response(data=users)


@router.get('/{id}', dependencies=[Depends(login_required)])
def get_user_by_id(id: str, current_user: UserDetail = Depends(login_required),
                   db: Session = Depends(deps.get_db)):
    user = UserService.get_user_by_id(db=db, id=id, user_id=current_user.id)
    return DataResponse().success_response(data=user)
