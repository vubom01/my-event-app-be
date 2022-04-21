import json

from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer

from app.models.base_model import BareBaseModel


class LikeEvent(BareBaseModel):
    __tablename__ = "like_events"

    event_id = Column(Integer, nullable=False)
    user_id = Column(String, nullable=False)

    def public_info_to_client(self) -> dict:
        return {
            'title': self.title,
            'type': self.type,
            'choices': json.loads(self.content).get('choices'),
            'duration': self.duration
        }