from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, inspect
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import Session


@as_declarative()
class Base:
    __abstract__ = True
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def as_dict(self) -> dict:
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}


class BareBaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    updated_at = Column(DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)

    @classmethod
    def create(cls, db: Session, data, commit=False):
        """
        Create new model object with given dict `data`
        :param db:
        :param dict data:
        :param commit:
        :return:
        """
        new_obj = cls(**data)
        db.add(new_obj)
        if commit:
            db.commit()
        else:
            db.flush()
        return new_obj
