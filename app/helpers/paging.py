import logging

from pydantic import BaseModel, root_validator
from typing import Optional, TypeVar, Generic, Sequence, Type
from contextvars import ContextVar
from pydantic.generics import GenericModel

from app.core.error import error_code, message
from app.helpers.exception_handler import ValidateException


T = TypeVar("T")
C = TypeVar("C")

logger = logging.getLogger()


class PaginationParamsRequest(BaseModel):
    page: Optional[int] = 1
    page_size: Optional[int] = 10

    @root_validator()
    def validate_data(cls, data):
        page = data.get("page")
        page_size = data.get("page_size")

        if page <= 0:
            raise ValidateException(
                error_code.ERROR_003_PAGE_LARGE_THAN_0, message.MESSAGE_003_PAGE_LARGE_THAN_0)
        if page_size <= 0 or page_size > 1000:
            raise ValidateException(
                error_code.ERROR_002_PAGE_SIZE_LARGE_THAN_0, message.MESSAGE_002_PAGE_SIZE_LARGE_THAN_0)

        return data


class PaginationParams(BaseModel):
    page_size: Optional[int] = 10
    page: Optional[int] = 0
    sort_by: Optional[str] = 'id'
    direction: Optional[str] = 'desc'


class PaginationParamsResponse(BaseModel):
    current_page: Optional[int]
    page_size: Optional[int]
    total_items: Optional[int]


class Pagination(BaseModel):
    current_page: int
    page_size: int
    total_items: int


class Page(GenericModel, Generic[T]):
    items: Sequence[T]
    pagination: Pagination

    @classmethod
    def create(cls, total: int, items: Sequence[T], pagination: Pagination) -> "Page[T]":
        return cls(
            total=total,
            items=items,
            pagination=pagination
        )


PageType: ContextVar[Type[Page]] = ContextVar("PageType", default=Page)
