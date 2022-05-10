import json

from sqlalchemy import Column, String, Integer

from app.models.base_model import BareBaseModel


class Message(BareBaseModel):
    __tablename__ = "message"

    event_id = Column(Integer, nullable=False)
    user_id = Column(String, nullable=False)
    message = Column(String, nullable=False)

    def public_info_to_client(self) -> dict:
        return {
            'title': self.title,
            'type': self.type,
            'choices': json.loads(self.content).get('choices'),
            'duration': self.duration
        }