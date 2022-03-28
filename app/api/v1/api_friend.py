from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import deps
from app.helpers.login_manager import login_required
from app.schemas.sche_base import DataResponse
from app.schemas.sche_friend import FriendRequest
from app.schemas.sche_user import UserDetail
from app.services.srv_friend import FriendService

router = APIRouter()


@router.post('', dependencies=[Depends(login_required)])
def send_friend_request(current_user: UserDetail = Depends(login_required), request: FriendRequest = None,
                        db: Session = Depends(deps.get_db)):
    response = FriendService.send_friend_request(db=db, request=request, user_id=current_user.id)
    return DataResponse().success_response(data=response)
