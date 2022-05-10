from typing import Optional

from fastapi import APIRouter, Depends
from requests import Session

from app.api import deps
from app.helpers.login_manager import login_required
from app.helpers.paging import PaginationParamsRequest
from app.schemas.sche_base import DataResponse
from app.schemas.sche_message import SendMessageRequest, ListMessageResponse, Rooms
from app.schemas.sche_user import UserDetail
from app.services.srv_chat_room import chat_room_srv

router = APIRouter()


@router.get('', dependencies=[Depends(login_required)], response_model=DataResponse[Rooms])
def get_rooms(event_name: Optional[str] = None, pagination: PaginationParamsRequest = Depends(),
              current_user: UserDetail = Depends(login_required), db: Session = Depends(deps.get_db)):
    rooms = chat_room_srv.get_rooms(user_id=current_user.id, event_name=event_name, page=pagination.page,
                                    page_size=pagination.page_size, db=db)
    return DataResponse().success_response(data=rooms)


@router.get('/message', dependencies=[Depends(login_required)], response_model=DataResponse[ListMessageResponse])
def get_message(event_id: int, pagination: PaginationParamsRequest = Depends(),
                current_user: UserDetail = Depends(login_required), db: Session = Depends(deps.get_db)):
    message = chat_room_srv.get_message(event_id=event_id, user_id=current_user.id, page=pagination.page,
                                        page_size=pagination.page_size, db=db)
    return DataResponse().success_response(data=message)


@router.post('/message', dependencies=[Depends(login_required)])
def send_message(request: SendMessageRequest, current_user: UserDetail = Depends(login_required),
                 db: Session = Depends(deps.get_db)):
    message = chat_room_srv.send_message(event_id=request.event_id, user_id=current_user.id,
                                         message=request.message, db=db)
    return DataResponse().success_response(data=message)
