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

        friend_request = crud_friend.get_friend_request(db=db, user_id=request.friend_id, friend_id=user_id)
        if friend_request:
            raise CustomException(http_code=400, message='Request has been sent')

        friend = FriendRequestDetail(
            user_id=request.friend_id,
            friend_id=user_id,
            status=0
        )
        response = crud_friend.create(db=db, obj_in=friend)
        return response.id

    @staticmethod
    def get_list_friend_request(db=None, page: int = None, page_size: int = None, user_id: str = None):
        friend_requests = crud_friend.get_list_request(db=db, page=page, page_size=page_size, user_id=user_id)
        for friend_request in friend_requests.items:
            user = crud_user.get(db=db, id=friend_request.friend_id)
            friend_request.username = user.username
            friend_request.first_name = user.first_name
            friend_request.last_name = user.last_name
            friend_request.email = user.email
            friend_request.phone_number = user.phone_number
        return friend_requests

    @staticmethod
    def approve_friend_request(db=None, friend_request_id: int = None, status: int = None, user_id: int = None):
        print(status)
        friend_request = crud_friend.get(db=db, id=friend_request_id)
        if friend_request is None:
            raise CustomException(http_code=400, message="Not found")
        if friend_request.user_id != user_id:
            raise CustomException(http_code=400, message="Don't have permission")

        resp = None
        if status == 0:
            resp = crud_friend.remove(db=db, id=friend_request_id)
        if status == 1:
            friend = FriendRequestDetail(
                user_id=friend_request.friend_id,
                friend_id=user_id,
                status=1
            )
            crud_friend.create(db=db, obj_in=friend)
            resp = crud_friend.accept_friend_request(db=db, friend_request_id=friend_request_id)
        return resp

    @staticmethod
    def get_list_friends(db=None, user_id: str = None, page: int = None, page_size: int = None,
                         queryParams: str = None, status: int = None):
        friends = crud_friend.get_all_friends(db=db, user_id=user_id, status=status)
        friend_id = []
        for friend in friends:
            friend_id.append(friend.friend_id)
        list_friends = crud_user.get_list_user(db=db, user_id=friend_id)
        response = []
        for friend in list_friends:
            full_name = str(friend.last_name + ' ' + friend.first_name)
            if queryParams is None or queryParams.lower() in full_name.lower() \
                    or queryParams in str(friend.email).lower() or queryParams in str(friend.username).lower():
                response.append(friend)

        start_idx = (page - 1) * page_size
        end_idx = min(page * page_size, len(response))
        return {
            'items': response[start_idx:end_idx],
            'pagination': {
                'current_page': page,
                'page_size': page_size,
                'total_items': len(response)
            }
        }

    @staticmethod
    def remove_friend(user_id: str, friend_id: str, db=None):
        friend_request = crud_friend.get_friend_request(user_id=friend_id, friend_id=user_id, db=db)
        if friend_request.status == 1:
            crud_friend.remove(db=db, id=friend_request.id)
            friend_request = crud_friend.get_friend_request(user_id=user_id, friend_id=friend_id, db=db)
            crud_friend.remove(db=db, id=friend_request.id)
        else:
            crud_friend.remove(db=db, id=friend_request.id)
        