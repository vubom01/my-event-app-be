from typing import Optional

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import deps
from app.helpers.login_manager import login_required
from app.helpers.paging import PaginationParamsRequest
from app.schemas.sche_base import DataResponse
from app.schemas.sche_friend import FriendRequest, ListFriendRequest, ApproveFriendRequest
from app.schemas.sche_user import UserDetail, ListUser
from app.services.srv_friend import FriendService

router = APIRouter()


@router.post('', dependencies=[Depends(login_required)])
def send_friend_request(current_user: UserDetail = Depends(login_required), request: FriendRequest = None,
                        db: Session = Depends(deps.get_db)):
    response = FriendService.send_friend_request(db=db, request=request, user_id=current_user.id)
    return DataResponse().success_response(data=response)


@router.put('/{friend_request_id}', dependencies=[Depends(login_required)])
def approve_friend_request(req_data: ApproveFriendRequest = None, db: Session = Depends(deps.get_db),
                           friend_request_id: int = None, current_user: UserDetail = Depends(login_required)):
    response = FriendService.approve_fried_request(db=db, friend_request_id=friend_request_id, status=req_data.status,
                                                   user_id = current_user.id)
    return DataResponse().success_response(data=response)


@router.get('/request', dependencies=[Depends(login_required)], response_model=DataResponse[ListFriendRequest])
def get_list_friend_requests(current_user: UserDetail = Depends(login_required),
                             pagination: PaginationParamsRequest = Depends(), db: Session = Depends(deps.get_db)):
    response = FriendService.get_list_friend_request(db=db, page=pagination.page, page_size=pagination.page_size,
                                                     user_id=current_user.id)
    return DataResponse().success_response(data=response)


@router.get('', response_model=DataResponse[ListUser])
def get_list_friends(current_user: UserDetail = Depends(login_required), queryParams: Optional[str] = None,
                     pagination: PaginationParamsRequest = Depends(), db: Session = Depends(deps.get_db)):
    response = FriendService.get_list_friends(db=db, user_id=current_user.id, queryParams=queryParams,
                                              page=pagination.page, page_size=pagination.page_size)
    return DataResponse().success_response(data=response)
