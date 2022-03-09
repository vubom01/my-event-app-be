from typing import Optional, List

from app.schemas.sche_base import ItemBaseModel


class UserDetail(ItemBaseModel):
    id: int
    username: Optional[str]
    password: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    phone_number: Optional[str]


