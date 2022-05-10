from datetime import datetime
from typing import List, Optional

from app.helpers.paging import PaginationParamsResponse
from app.schemas.sche_base import ItemBaseModel


class MessageDetail(ItemBaseModel):
    id: int
    event_id: int
    user_id: str
    message: str
    created_at: datetime


class SendMessageRequest(ItemBaseModel):
    event_id: int
    message: str


class Message(ItemBaseModel):
    event_id: int
    user_id: str
    message: str


class MessageResponse(ItemBaseModel):
    id: int
    user_id: str
    user_name: str
    user_image: str
    message: str
    created_at: datetime


class ListMessageResponse(ItemBaseModel):
    event_id: int
    event_name: str
    items: List[MessageResponse]
    pagination: PaginationParamsResponse


class RoomDetail(ItemBaseModel):
    event_id: int
    event_name: str
    event_images: Optional[List[str]]
    user_id: str
    user_name: str
    message: str


class Rooms(ItemBaseModel):
    items: List[RoomDetail]
    pagination: PaginationParamsResponse
