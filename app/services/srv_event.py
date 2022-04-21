import logging
from typing import List

from app.crud.crud_event import crud_event
from app.crud.crud_event_image import crud_event_image
from app.crud.crud_like_event import crud_like_event
from app.crud.crud_user import crud_user
from app.crud.crud_user_event_status import crud_user_event_status
from app.helpers.paging import PaginationParamsRequest
from app.models.like_event_model import LikeEvent
from app.models.user_event_status_model import UserEventStatus
from app.schemas.sche_event import EventCreateRequest, EventDetail, EventsRequest, InfoEventRequestDetail
from app.schemas.sche_event_image import EventImageDetail
from app.helpers.exception_handler import CustomException

logger = logging.getLogger()


class EventService(object):

    @staticmethod
    def create_event(db=None, event: EventCreateRequest = None, user_id: str = None):
        request = EventDetail(**event.dict())
        request.host_id = user_id
        response = crud_event.create(db=db, obj_in=request)

        image_requests = list()
        for image in event.images:
            image_request = EventImageDetail(
                event_id=response.id,
                image=image
            )
            image_requests.append(image_request)
        crud_event_image.create_multi(db=db, list_obj_in=image_requests)

        return {
            "id": response.id
        }

    @staticmethod
    def get_event_images(db, event_id: int):
        event_images = crud_event_image.get_event_images(db=db, event_id=event_id)
        response = []
        for event_image in event_images:
            response.append(event_image.image)
        return response

    def get_detail(self, db, event_id: int, user_id: str):
        event = crud_event.get(db=db, id=event_id)
        if event is None:
            raise CustomException(http_code=400, message='Event is not exist')
        if self.check_user_in_event(db=db, event_id=event_id, user_id=user_id):
            images = self.get_event_images(db=db, event_id=event_id)
            event.images = images
            return event
        raise CustomException(http_code=400, message='User cannot this access')

    @staticmethod
    def get_event_requests(db, user_id: str, query_params: str, page: int, page_size: int):
        event_requests = crud_user_event_status.get_event_requests(db=db, user_id=user_id)
        response = []
        for event_request in event_requests:
            user = crud_user.get(db=db, id=event_request.user_id)
            full_name = str(user.last_name + user.first_name)
            if query_params is None or query_params.lower() in full_name.lower() \
                    or query_params in str(user.email).lower() or query_params in str(user.username).lower():
                event = crud_event.get(db=db, id=event_request.event_id)
                res = InfoEventRequestDetail(
                    event_id=event.id,
                    event_name=event.event_name,
                    event_description=event.description,
                    host_id=user.id,
                    host_username=user.username,
                    host_email=user.email,
                    host_fullname=full_name
                )
                response.append(res)

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

    def like_event(self, db=None, event_id: int = None, user_id: str = None):
        self.check_exist_event(db=db, event_id=event_id)
        like_event_detail = crud_like_event.get_like_event(db=db, event_id=event_id, user_id=user_id)
        if like_event_detail:
            raise CustomException(http_code=400, message='User has liked this event')

        like_event = LikeEvent(
            event_id=event_id,
            user_id=user_id
        )
        if self.check_user_in_event(db=db, event_id=event_id, user_id=user_id):
            crud_like_event.create(db=db, obj_in=like_event)
        else:
            raise CustomException(http_code=400, message='User cannot this access')

    def unlike_event(self, db=None, event_id: int = None, user_id: str = None):
        self.check_exist_event(db=db, event_id=event_id)
        like_event_detail = crud_like_event.get_like_event(db=db, event_id=event_id, user_id=user_id)
        if like_event_detail is None:
            raise CustomException(http_code=400, message='User cannot this access')
        else:
            crud_like_event.remove(db=db, id=like_event_detail.id)

    @staticmethod
    def check_user_in_event(db=None, event_id: int = None, user_id: str = None):
        event_detail = crud_event.get(db=db, id=event_id)
        if event_detail.status == 1:
            return True
        if event_detail.host_id == user_id:
            return True
        user_event_status = crud_user_event_status.get_user_event_status(db=db, event_id=event_id, user_id=user_id)
        if user_event_status is None:
            return False
        if user_event_status.status == 1:
            return True
        return False

    @staticmethod
    def check_exist_event(db=None, event_id: int = None):
        event = crud_event.get(db=db, id=event_id)
        if event is None:
            raise CustomException(http_code=400, message='Event is not exist')

    @staticmethod
    def send_event_request(db=None, event_id: int = None, user_id: int = None, host_id: int = None):
        event_detail = crud_event.get(db=db, id=event_id)
        if event_detail.host_id != host_id:
            raise CustomException(http_code=400, message='User cannot this access')

        user_event_status = crud_user_event_status.get_user_event_status(db=db, event_id=event_id, user_id=user_id)
        if user_event_status:
            if user_event_status.status == 0:
                raise CustomException(http_code=400, message='Request has sent')
            if user_event_status.status == 1:
                raise CustomException(http_code=400, message='User attended the event')
        else:
            user_event_status = UserEventStatus(
                event_id=event_id,
                user_id=user_id
            )
            crud_user_event_status.create(db=db, obj_in=user_event_status)

    def approve_event_request(self, db, event_id: int, user_id: int, approve: str):
        self.check_exist_event(db=db, event_id=event_id)

        user_event_status = crud_user_event_status.get_user_event_status(db=db, event_id=event_id, user_id=user_id)
        if user_event_status is None:
            raise CustomException(http_code=400, message='Request has not sent')
        else:
            if user_event_status.status == 1:
                raise CustomException(http_code=400, message='User attended the event')
            if approve == 'approved':
                crud_user_event_status.update(db=db, db_obj=user_event_status, obj_in={'status': 1})
            else:
                crud_user_event_status.remove(db=db, id=user_event_status.id)

    @staticmethod
    def get_event_requests_of_event(db, event_id: int, query_params: str,
                                    page: int, page_size: int, host_id: str, status: int):
        event_detail = crud_event.get(db=db, id=event_id)
        if event_detail.host_id != host_id:
            raise CustomException(http_code=400, message='User cannot this access')

        user_event_status = crud_user_event_status.get_event_requests_by_event_id(db=db, event_id=event_id,
                                                                                  status=status)
        user_ids = [user_event.user_id for user_event in user_event_status]
        users = crud_user.get_list_user(db=db, user_id=user_ids)
        response = []
        for user in users:
            full_name = str(user.last_name + user.first_name)
            if query_params is None or query_params.lower() in full_name.lower() \
                    or query_params in str(user.email).lower() or query_params in str(user.username).lower():
                response.append(user)

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


event_srv = EventService()
