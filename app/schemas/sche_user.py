from datetime import date
from typing import Optional, List

from app.schemas.sche_base import ItemBaseModel


class UserDetail(ItemBaseModel):
    id: Optional[int]
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    phone_number: Optional[str]
    gender: Optional[str]
    dob: Optional[date]


class UserDetailRequest(UserDetail):
    password: Optional[str]




