from typing import List, Optional

from app.helpers.paging import PaginationParamsResponse
from app.schemas.sche_base import ItemBaseModel


class FriendRequestDetail(ItemBaseModel):
    user_id: str
    friend_id: str
    status: int


class FriendRequest(ItemBaseModel):
    friend_id: str


class FriendDetail(ItemBaseModel):
    id: int
    friend_id: str


class ListFriendRequest(ItemBaseModel):
    items: List[FriendDetail]
    pagination: PaginationParamsResponse


class ApproveFriendRequest(ItemBaseModel):
    status: Optional[int] = 0
