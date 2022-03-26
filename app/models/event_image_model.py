import json

from sqlalchemy.types import String, Integer
from sqlalchemy.schema import Column

from app.models.base_model import BareBaseModel


class EventImage(BareBaseModel):
    __tablename__ = "event_images"

    event_id = Column(Integer, nullable=False)
    image = Column(String, nullable=False)

    def public_info_to_client(self) -> dict:
        return {
            'title': self.title,
            'type': self.type,
            'choices': json.loads(self.content).get('choices'),
            'duration': self.duration
        }
