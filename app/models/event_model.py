import json

from sqlalchemy.types import String, DateTime, Integer, Float
from sqlalchemy.schema import Column

from app.models.base_model import BareBaseModel


class Event(BareBaseModel):
    __tablename__ = "events"

    host_id = Column(String, nullable=False)
    topic = Column(String, nullable=False)
    event_name = Column(String, nullable=False)
    start_at = Column(DateTime(timezone=True), nullable=False)
    end_at = Column(DateTime(timezone=True), nullable=True)
    description = Column(String, nullable=False)
    status = Column(Integer, nullable=False)
    lat = Column(Float, nullable=True)
    long = Column(Float, nullable=True)

    def public_info_to_client(self) -> dict:
        return {
            'title': self.title,
            'type': self.type,
            'choices': json.loads(self.content).get('choices'),
            'duration': self.duration
        }
