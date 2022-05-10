from datetime import datetime
from typing import List

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
