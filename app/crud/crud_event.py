from typing import List

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.crud.crud_base import CRUDBase
from app.models.event_model import Event
from app.schemas.sche_event import EventDetail


class CRUDEvent(CRUDBase[EventDetail, EventDetail, EventDetail]):

    def get_all_events(self, db: Session):
        return db.query(self.model).order_by(text(f"start_at asc")).all()

    def get_events(self, db: Session, event_ids: List[int]):
        events = db.query(self.model).filter(self.model.id.in_(event_ids)).\
            order_by(text(f"start_at desc")).all()
        return events

    def get_events_by_host_id(self, db: Session, user_id: str):
        return db.query(self.model).filter(self.model.host_id == user_id).all()


crud_event = CRUDEvent(Event)
