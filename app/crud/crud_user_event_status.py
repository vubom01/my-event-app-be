from app.crud.crud_base import CRUDBase
from app.models.user_event_status_model import UserEventStatus
from app.schemas.sche_user_event_status import UserEventStatusDetail
from sqlalchemy.orm import Session


class CRUDUserEventStatus(CRUDBase[UserEventStatusDetail, UserEventStatusDetail, UserEventStatusDetail]):

    def get_user_event_status(self, db: Session, event_id: int, user_id: str):
        return db.query(self.model).filter(self.model.event_id == event_id, self.model.user_id == user_id).first()

    def get_event_requests(self, db: Session, user_id: str):
        return db.query(self.model).filter(self.model.user_id == user_id, self.model.status == 0).all()

    def get_event_requests_by_event_id(self, db: Session, event_id: int, status: int):
        return db.query(self.model).filter(self.model.event_id == event_id, self.model.status == status).all()

    def get_event_join(self, db: Session, user_id: str):
        return db.query(self.model).filter(self.model.user_id == user_id, self.model.status == 1).all()


crud_user_event_status = CRUDUserEventStatus(UserEventStatus)

