from datetime import datetime
from typing import Optional, List

from app.helpers.enums import SearchEventType, ApproveEventStatus
from app.helpers.paging import PaginationParamsResponse
from app.schemas.sche_base import ItemBaseModel


class EventDetail(ItemBaseModel):
    host_id: Optional[str]
    topic: Optional[str]
    event_name: Optional[str]
    start_at: Optional[datetime]
    end_at: Optional[datetime]
    description: Optional[str]
    status: Optional[int]
    lat: Optional[float]
    long: Optional[float]


class EventCreateRequest(EventDetail):
    images: Optional[List[str]]


class EventDetailResponse(EventDetail):
    id: int
    images: Optional[List[str]]


class EventsRequest(ItemBaseModel):
    type: Optional[SearchEventType]
    host_info: Optional[str]
    event_name: Optional[str]
    topic: Optional[str]
    start_at: Optional[datetime]
    end_at: Optional[datetime]
    status: Optional[int]


class EventsResponse(ItemBaseModel):
    events: List[EventDetailResponse]


class EventRequest(ItemBaseModel):
    user_id: str


class ApproveEventRequest(ItemBaseModel):
    approve: ApproveEventStatus


class InfoEventRequestDetail(ItemBaseModel):
    event_id: int
    event_name: str
    event_description: Optional[str]
    host_id: str
    host_username: str
    host_email: str
    host_fullname: str
