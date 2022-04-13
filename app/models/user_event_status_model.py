import json

from sqlalchemy import Column, String, Integer

from app.models.base_model import BareBaseModel


class UserEventStatus(BareBaseModel):
    __tablename__ = "user_event_status"

    event_id = Column(Integer, nullable=False)
    user_id = Column(String, nullable=False)
    status = Column(Integer, nullable=False, default=0)
    like = Column(Integer, nullable=False, default=0)

    def public_info_to_client(self) -> dict:
        return {
            'title': self.title,
            'type': self.type,
            'choices': json.loads(self.content).get('choices'),
            'duration': self.duration
        }
