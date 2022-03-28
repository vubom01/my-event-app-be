from app.schemas.sche_base import ItemBaseModel


class FriendRequestDetail(ItemBaseModel):
    user_id: str
    friend_id: str
    status: int


class FriendRequest(ItemBaseModel):
    friend_id: str
