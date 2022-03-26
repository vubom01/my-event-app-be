from app.schemas.sche_base import ItemBaseModel


class EventImageDetail(ItemBaseModel):
    event_id: int
    image: str
