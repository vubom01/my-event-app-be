from datetime import date
from typing import Optional, List

from app.helpers.paging import PaginationParamsResponse
from app.schemas.sche_base import ItemBaseModel


class UserDetail(ItemBaseModel):
    id: Optional[str]
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    phone_number: Optional[str]
    gender: Optional[str]
    dob: Optional[date]
    avatar: Optional[str]


class UserDetailRequest(UserDetail):
    password: Optional[str]


class UserUpdateRequest(ItemBaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    phone_number: Optional[str]
    gender: Optional[str]
    dob: Optional[date]
    avatar: Optional[str]


class ListUser(ItemBaseModel):
    items: List[UserDetail]
    pagination: PaginationParamsResponse

