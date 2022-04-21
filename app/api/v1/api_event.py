from typing import Optional, List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.api import deps
from app.helpers.login_manager import login_required
from app.schemas.sche_base import DataResponse, ItemBaseModel
from app.schemas.sche_event import EventCreateRequest, EventDetailResponse
from app.schemas.sche_user import UserDetail
from app.services.srv_event import event_srv

router = APIRouter()


@router.post('', dependencies=[Depends(login_required)])
def create(current_user: UserDetail = Depends(login_required), request: EventCreateRequest = None,
           db: Session = Depends(deps.get_db)):
    event = event_srv.create_event(db=db, event=request, user_id=current_user.id)
    return DataResponse().success_response(data=event)


@router.get('/{event_id}', dependencies=[Depends(login_required)], response_model=DataResponse[EventDetailResponse])
def get_detail(current_user: UserDetail = Depends(login_required), event_id: int = None,
               db: Session = Depends(deps.get_db)):
    event = event_srv.get_detail(db=db, event_id=event_id, user_id=current_user.id)
    return DataResponse().success_response(data=event)


@router.post('/{event_id}/invite', dependencies=[Depends(login_required)])
def send_event_request(event_id: int, user_id: str, current_user: UserDetail = Depends(login_required),
                       db: Session = Depends(deps.get_db)):
    event_request = event_srv.send_event_request(db=db, event_id=event_id, user_id=user_id, host_id=current_user.id)
    return DataResponse().success_response(data=event_request)


@router.delete('/{event_id}/invite', dependencies=[Depends(login_required)])
def delete_user_event(event_id: int, user_id: str, current_user: UserDetail = Depends(login_required),
                      db: Session = Depends(deps.get_db)):
    event_request = event_srv.delete_user_event(db=db, event_id=event_id, user_id=user_id, host_id=current_user.id)
    return DataResponse().success_response(data=event_request)
