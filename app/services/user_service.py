import logging

from app.crud.crud_user import crud_user

logger = logging.getLogger()


class UserService:

    @classmethod
    def detail_user(cls, db=None, user_id=None):
        user_detail = crud_user.get(db=db, id=user_id)
        return user_detail
