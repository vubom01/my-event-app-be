from typing import List

from sqlalchemy import text

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

    def get_list_user(self, db: Session, user_id: List[str]):
        friends = db.query(self.model).filter(self.model.id.in_(user_id)).\
            order_by(text(f"updated_at desc")).all()
        return friends

    def get_all_users(self, db: Session):
        users = db.query(self.model).order_by(text(f"created_at asc")).all()
        return users


crud_user = CRUDUser(User)
