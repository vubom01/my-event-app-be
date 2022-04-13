from app.schemas.sche_base import ItemBaseModel


class UserEventStatus(ItemBaseModel):
    event_id: int
    user_id: str
    status: int
    like: int


class UserEventStatusDetail(UserEventStatus):
    id: int
