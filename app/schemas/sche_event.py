from datetime import datetime
from typing import Optional, List

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
