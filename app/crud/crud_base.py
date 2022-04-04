from typing import Generic, TypeVar, Type, Any, Optional, List, Union, Dict, Sequence

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.orm import Session, Query
from sqlalchemy.exc import DataError

from app.helpers.exception_handler import ValidateException
from app.helpers.paging import Pagination, Page, PaginationParams, PageType
from app.models.base_model import Base


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, db: Session, id: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.id == id).first()

    def create(self, db: Session, *, obj_in: CreateSchemaType, **data) -> ModelType:
        if data.get('by_alias') is not None:
            obj_in_data = jsonable_encoder(obj_in, by_alias=data.get('by_alias'))
        else:
            obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def create_multi(self, db: Session, *, list_obj_in: Sequence[CreateSchemaType]) -> Sequence[ModelType]:
        list_db_obj = []
        for obj_in in list_obj_in:
            obj_in_data = jsonable_encoder(obj_in)
            db_obj = self.model(**obj_in_data)
            list_db_obj.append(db_obj)
        db.add_all(list_db_obj)
        db.commit()
        return list_db_obj

    def update(
            self,
            db: Session,
            *,
            db_obj: ModelType,
            obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        obj_data = db_obj.as_dict()
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def paginate(self, query: Query, params: Optional[PaginationParams] = None) -> Page:
        try:
            total = query.count()
            if params.page == 0:
                params.page = 1

            items = query.order_by(text(f"{params.sort_by} {params.direction}")) \
                .offset(params.page_size * (params.page - 1)).limit(params.page_size).all()

            total_page = (total - 1) // params.page_size + 1

            pagination = Pagination(
                current_page=params.page,
                page_size=params.page_size,
                total_items=total,
                total_pages=total_page
            )

        except Exception as e:
            print(e)
            if type(e) == DataError:
                raise ValidateException("008", "Các toán tử tìm kiếm không phù hợp với trường hoặc giá trị tìm kiếm")
            raise Exception("Lỗi Paging")

        return PageType.get().create(total, items, pagination)


