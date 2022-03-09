from app.crud.crud_base import CRUDBase
from app.schemas.sche_user import UserDetail
from sqlalchemy.orm import Session
from app.models.user_model import User


class CRUDUser(CRUDBase[UserDetail, UserDetail, UserDetail]):

    def test(self):
        pass


crud_user = CRUDUser(User)
