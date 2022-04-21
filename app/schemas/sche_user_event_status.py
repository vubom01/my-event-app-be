from typing import List

from app.schemas.sche_base import ItemBaseModel


class UserEventStatus(ItemBaseModel):
    event_id: int
    user_id: str
    status: int


class UserEventStatusDetail(UserEventStatus):
    id: int


class ListUserEventStatus(ItemBaseModel):
    event_requests: List[UserEventStatus]
