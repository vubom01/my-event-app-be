from sqlalchemy.orm import Session

from app.crud.crud_base import CRUDBase
from app.models.like_event_model import LikeEvent


class CRUDLikeEvent(CRUDBase[LikeEvent, LikeEvent, LikeEvent]):

    def get_like_event(self, db: Session, event_id: int, user_id: str):
        return db.query(self.model).filter(self.model.event_id == event_id, self.model.user_id == user_id).first()


crud_like_event = CRUDLikeEvent(LikeEvent)
