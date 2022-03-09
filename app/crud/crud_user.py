from app.crud.crud_base import CRUDBase
from app.schemas.sche_user import UserDetail
from sqlalchemy.orm import Session
from app.models.user_model import User


class CRUDUser(CRUDBase[UserDetail, UserDetail, UserDetail]):

    def get_user_by_filter(self, db: Session, username: str = None, email: str = None):
        if username:
            return db.query(self.model).filter(self.model.username == username).first()
        if email:
            return db.query(self.model).filter(self.model.email == email).first()


crud_user = CRUDUser(User)
