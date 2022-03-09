import json

from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer

from app.models.base_model import BareBaseModel


class User(BareBaseModel):
    __tablename__ = "users"

    username = Column(String, nullable=False)
    password = Column(Integer, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(Integer, nullable=False)
    email = Column(Integer, nullable=False)
    phone_number = Column(Integer, nullable=False)

    def public_info_to_client(self) -> dict:
        return {
            'title': self.title,
            'type': self.type,
            'choices': json.loads(self.content).get('choices'),
            'duration': self.duration
        }
