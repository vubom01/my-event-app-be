import json

from sqlalchemy import Column, String, Integer

from app.models.base_model import BareBaseModel


class Friend(BareBaseModel):
    __tablename__ = "friends"

    user_id = Column(String, nullable=False)
    friend_id = Column(String, nullable=False)
    status = Column(Integer, nullable=False)

    def public_info_to_client(self) -> dict:
        return {
            'title': self.title,
            'type': self.type,
            'choices': json.loads(self.content).get('choices'),
            'duration': self.duration
        }
