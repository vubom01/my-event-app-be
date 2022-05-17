from typing import Optional

from app.schemas.sche_base import ItemBaseModel


class BodyEmail(ItemBaseModel):
    subject: Optional[str]
    body: str
