from app.crud.crud_base import CRUDBase
from app.models.user_event_status_model import UserEventStatus
from app.schemas.sche_user_event_status import UserEventStatusDetail
from sqlalchemy.orm import Session


class CRUDUserEventStatus(CRUDBase[UserEventStatusDetail, UserEventStatusDetail, UserEventStatusDetail]):

    def get_user_event_status(self, db: Session, event_id: int, user_id: str):
        return db.query(self.model).filter(self.model.event_id == event_id, self.model.user_id == user_id).first()


crud_user_event_status = CRUDUserEventStatus(UserEventStatus)

