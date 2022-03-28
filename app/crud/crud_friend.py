from sqlalchemy.orm import Session

from app.crud.crud_base import CRUDBase
from app.models.friend_model import Friend
from app.schemas.sche_friend import FriendRequestDetail


class CRUDFriend(CRUDBase[FriendRequestDetail, FriendRequestDetail, FriendRequestDetail]):

    def get_friend_request(self, db: Session, user_id: str, friend_id: str):
        return db.query(self.model).filter(self.model.user_id == user_id, self.model.friend_id == friend_id).first()


crud_friend = CRUDFriend(Friend)
