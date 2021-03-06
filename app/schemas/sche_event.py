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
    host_fullname: Optional[str]
    liked: Optional[bool]
    joined: Optional[bool]


class EventsRequest(ItemBaseModel):
    type: Optional[SearchEventType]
    host_info: Optional[str]
    event_name: Optional[str]
    topic: Optional[str]
    start_at_start: Optional[datetime]
    start_at_end: Optional[datetime]
    end_at_start: Optional[datetime]
    end_at_end: Optional[datetime]
    status: Optional[int]


class EventWithHostInfo(EventDetailResponse):
    host_fullname: str
    host_username: str
    host_email: str


class EventsResponse(ItemBaseModel):
    items: List[EventWithHostInfo]
    pagination: PaginationParamsResponse


class EventRequest(ItemBaseModel):
    user_id: List[str]


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
