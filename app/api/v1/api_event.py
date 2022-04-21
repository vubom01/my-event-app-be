from typing import Optional, List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.api import deps
from app.helpers.enums import ApproveEventStatus, StatusEventRequest
from app.helpers.login_manager import login_required
from app.helpers.paging import PaginationParamsRequest
from app.models.user_event_status_model import UserEventStatus
from app.schemas.sche_base import DataResponse, ItemBaseModel
from app.schemas.sche_event import EventCreateRequest, EventDetailResponse, EventsRequest, EventsResponse, EventRequest, \
    ApproveEventRequest
from app.schemas.sche_user import UserDetail
from app.schemas.sche_user_event_status import ListUserEventStatus
from app.services.srv_event import event_srv

router = APIRouter()


@router.post('', dependencies=[Depends(login_required)])
def create(current_user: UserDetail = Depends(login_required), request: EventCreateRequest = None,
           db: Session = Depends(deps.get_db)):
    event = event_srv.create_event(db=db, event=request, user_id=current_user.id)
    return DataResponse().success_response(data=event)


@router.get('', dependencies=[Depends(login_required)], response_model=DataResponse[EventsResponse])
def get_events(req_data: EventsRequest = Depends(), pagination: PaginationParamsRequest = Depends(),
               current_user: UserDetail = Depends(login_required), db: Session = Depends(deps.get_db)):
    events = event_srv.search_event(db=db, req_data=req_data, pagination=pagination, user_id=current_user.id)
    return DataResponse().success_response(data=events)


@router.get('/request',  dependencies=[Depends(login_required)], response_model=DataResponse[ListUserEventStatus])
def get_event_requests(db: Session = Depends(deps.get_db), current_user: UserDetail = Depends(login_required)):
    event_requests = event_srv.get_event_requests(db=db, user_id=current_user.id)
    return DataResponse().success_response(data=event_requests)


@router.get('/{event_id}', dependencies=[Depends(login_required)], response_model=DataResponse[EventDetailResponse])
def get_detail(current_user: UserDetail = Depends(login_required), event_id: int = None,
               db: Session = Depends(deps.get_db)):
    event = event_srv.get_detail(db=db, event_id=event_id, user_id=current_user.id)
    return DataResponse().success_response(data=event)


@router.post('/{event_id}/like', dependencies=[Depends(login_required)])
def like_event(event_id: int, current_user: UserDetail = Depends(login_required), db: Session = Depends(deps.get_db)):
    response = event_srv.like_event(db=db, event_id=event_id, user_id=current_user.id)
    return DataResponse().success_response(data=response)


@router.delete('/{event_id}/like', dependencies=[Depends(login_required)])
def unlike_event(event_id: int, current_user: UserDetail = Depends(login_required), db: Session = Depends(deps.get_db)):
    response = event_srv.unlike_event(db=db, event_id=event_id, user_id=current_user.id)
    return DataResponse().success_response(data=response)


@router.post('/{event_id}/invite', dependencies=[Depends(login_required)])
def send_event_request(event_id: int, req_data: EventRequest, current_user: UserDetail = Depends(login_required),
                       db: Session = Depends(deps.get_db)):
    response = event_srv.send_event_request(db=db, event_id=event_id, user_id=req_data.user_id,
                                            host_id=current_user.id)
    return DataResponse().success_response(data=response)


@router.put('/{event_id}/invite', dependencies=[Depends(login_required)])
def approve_event_request(event_id: int, req_data: ApproveEventRequest,
                          current_user: UserDetail = Depends(login_required), db: Session = Depends(deps.get_db)):
    response = event_srv.approve_event_request(db=db, event_id=event_id, user_id=current_user.id,
                                               approve=req_data.approve.value)
    return DataResponse().success_response(data=response)


@router.get('/{event_id}/event_request', dependencies=[Depends(login_required)])
def get_event_requests_of_event(event_id: int, status: StatusEventRequest, query_params: Optional[str] = None,
                                pagination: PaginationParamsRequest = Depends(), db: Session = Depends(deps.get_db),
                                current_user: UserDetail = Depends(login_required)):
    event_requests = event_srv.get_event_requests_of_event(db=db, event_id=event_id, host_id=current_user.id,
                                                           query_params=query_params, page=pagination.page,
                                                           page_size=pagination.page_size, status=status.value)
    return DataResponse().success_response(data=event_requests)
