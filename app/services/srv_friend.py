import logging

from app.crud.crud_friend import crud_friend
from app.crud.crud_user import crud_user
from app.helpers.exception_handler import CustomException
from app.schemas.sche_friend import FriendRequest, FriendRequestDetail

logger = logging.getLogger()


class FriendService:
    @staticmethod
    def send_friend_request(db=None, request: FriendRequest = None, user_id: str = None):
        if user_id == request.friend_id:
            raise CustomException(http_code=400, message='friend_id is invalid')

        user = crud_user.get(db=db, id=request.friend_id)
        if user is None:
            raise CustomException(http_code=400, message='User is not found')

        friend_request = crud_friend.get_friend_request(db=db, user_id=user_id, friend_id=request.friend_id)
        if friend_request:
            raise CustomException(http_code=400, message='Request has been sent')

        friend = FriendRequestDetail(
            user_id=user_id,
            friend_id=request.friend_id,
            status=0
        )
        response = crud_friend.create(db=db, obj_in=friend)
        return response.id



