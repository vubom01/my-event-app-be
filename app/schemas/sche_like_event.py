from app.schemas.sche_base import ItemBaseModel


class LikeEvent(ItemBaseModel):
    event_id: int
    user_id: str
