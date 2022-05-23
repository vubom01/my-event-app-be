from sqlalchemy.orm import Session

from app.crud.crud_base import CRUDBase
from app.helpers.paging import PaginationParams
from app.models.friend_model import Friend
from app.schemas.sche_friend import FriendRequestDetail


class CRUDFriend(CRUDBase[FriendRequestDetail, FriendRequestDetail, FriendRequestDetail]):

    def get_friend_request(self, db: Session, user_id: str, friend_id: str):
        return db.query(self.model).filter(self.model.user_id == user_id, self.model.friend_id == friend_id).first()

    def get_list_request(self, db: Session, page: int, page_size: int, user_id: int):
        query = db.query(self.model).filter(self.model.user_id == user_id, self.model.status == 0)
        pagination = PaginationParams(
            page=page,
            page_size=page_size,
            sort_by='created_at',
        )
        resp = self.paginate(query=query, params=pagination)
        return resp

    def get_list_send(self, db: Session, page: int, page_size: int, user_id: int):
        query = db.query(self.model).filter(self.model.friend_id == user_id, self.model.status == 0)
        pagination = PaginationParams(
            page=page,
            page_size=page_size,
            sort_by='created_at',
        )
        resp = self.paginate(query=query, params=pagination)
        return resp

    def accept_friend_request(self, db: Session, friend_request_id: int):
        friend_request = self.get(db=db, id=friend_request_id)
        resp = self.update(db=db, db_obj=friend_request, obj_in={'status': 1})
        return resp

    def get_all_friends(self, db: Session, user_id: int, status: int = 1):
        return db.query(self.model).filter(self.model.user_id == user_id, self.model.status == status)


crud_friend = CRUDFriend(Friend)
