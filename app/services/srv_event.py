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
from app.schemas.sche_event import EventCreateRequest, EventDetail, EventsRequest, InfoEventRequestDetail, \
    EventWithHostInfo
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
            response = event

            host_detail = crud_user.get(db=db, id=event.host_id)
            response.host_fullname = str(host_detail.last_name + ' ' + host_detail.first_name)

            user_event_status = crud_user_event_status.get_user_event_status(db=db, event_id=event_id, user_id=user_id)
            if (user_event_status and user_event_status.status == 1) or (host_detail.id == user_id):
                response.joined = True

            like_event = crud_like_event.get_like_event(db=db, event_id=event_id, user_id=user_id)
            if like_event:
                response.liked = True

            return event

        raise CustomException(http_code=400, message='User cannot this access')

    @staticmethod
    def get_event_requests(db, user_id: str, query_params: str, page: int, page_size: int):
        event_requests = crud_user_event_status.get_event_requests(db=db, user_id=user_id)
        response = []
        for event_request in event_requests:
            user = crud_user.get(db=db, id=event_request.user_id)
            full_name = str(user.last_name + ' ' + user.first_name)
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
        if user_event_status.status == 0 or user_event_status.status == 1:
            return True
        return False

    @staticmethod
    def check_exist_event(db=None, event_id: int = None):
        event = crud_event.get(db=db, id=event_id)
        if event is None:
            raise CustomException(http_code=400, message='Event is not exist')

    @staticmethod
    def send_event_request(db=None, event_id: int = None, user_ids: List[str] = None, host_id: int = None):
        event_detail = crud_event.get(db=db, id=event_id)
        if event_detail is None:
            raise CustomException(http_code=400, message='Event is not exist')
        if event_detail.host_id != host_id:
            raise CustomException(http_code=400, message='User cannot this access')

        for user_id in user_ids:
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
    def delete_user_event(db, event_id: int, user_id: int, host_id: int):
        event_detail = crud_event.get(db=db, id=event_id)
        if event_detail is None:
            raise CustomException(http_code=400, message='Event is not exist')
        if event_detail.host_id != host_id:
            raise CustomException(http_code=400, message='User cannot this access')

        user_event_status = crud_user_event_status.get_user_event_status(db=db, event_id=event_id, user_id=user_id)
        if user_event_status is None:
            raise CustomException(http_code=400, message='Người dùng chưa được mời hoặc chưa tham gia sự kiện')
        crud_user_event_status.remove(db=db, id=user_event_status.id)
        if event_detail.status == 0:
            like_event = crud_like_event.get_like_event(db=db, event_id=event_id, user_id=user_id)
            if like_event:
                crud_like_event.remove(db=db, id=like_event.id)

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
            full_name = str(user.last_name + ' ' + user.first_name)
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

    @staticmethod
    def join_public_event(db, event_id: int, user_id: str):
        event_detail = crud_event.get(db=db, id=event_id)
        if event_detail is None:
            raise CustomException(http_code=400, message='Event is not exist')
        if event_detail.host_id == user_id:
            raise CustomException(http_code=400, message='User is host of event')
        if event_detail.status == 0:
            raise CustomException(http_code=400, message='Event is private')

        user_event_status = crud_user_event_status.get_user_event_status(db=db, event_id=event_id, user_id=user_id)
        if user_event_status:
            raise CustomException(http_code=400, message='Người dùng đã được mời hoặc đã tham gia sự kiện')

        user_event = UserEventStatus(
            event_id=event_id,
            user_id=user_id,
            status=1
        )
        crud_user_event_status.create(db=db, obj_in=user_event)

    @staticmethod
    def out_event(db, event_id: int, user_id: str):
        event = crud_event.get(db=db, id=event_id)
        if event is None:
            raise CustomException(http_code=400, message='Event is not exist')

        user_event_status = crud_user_event_status.get_user_event_status(db=db, event_id=event_id, user_id=user_id)
        if user_event_status is None or user_event_status.status == 0:
            raise CustomException(http_code=400, message='Người dùng chưa tham gia sự kiện')

        crud_user_event_status.remove(db=db, id=user_event_status.id)

        if event.status == 0:
            like_event = crud_like_event.get_like_event(db=db, event_id=event_id, user_id=user_id)
            if like_event:
                crud_like_event.remove(db=db, id=like_event.id)

    def get_events(self, db, req_data: EventsRequest, pagination: PaginationParamsRequest, user_id: str):
        events = []
        if req_data.type is None:
            list_event = crud_event.get_all_events(db=db)
            for event in list_event:
                if self.check_user_in_event(db=db, event_id=event.id, user_id=user_id) is True:
                    events.append(event)
        elif req_data.type.value == 'host':
            events = crud_event.get_events_by_host_id(db=db, user_id=user_id)
        elif req_data.type.value == 'join':
            user_events = crud_user_event_status.get_event_join(db=db, user_id=user_id)
            events = crud_event.get_events(db=db, event_ids=[user_event.event_id for user_event in user_events])
        elif req_data.type.value == 'like':
            like_events = crud_like_event.get_like_event_by_user_id(db=db, user_id=user_id)
            events = crud_event.get_events(db=db, event_ids=[like_event.event_id for like_event in like_events])

        response = []
        for event in events:
            check = True
            host_detail = crud_user.get(db=db, id=event.host_id)
            if req_data.host_info:
                query_params = str(req_data.host_info)
                full_name = str(host_detail.last_name + ' ' + host_detail.first_name)
                if query_params.lower() in full_name.lower() \
                        or query_params in str(host_detail.email).lower() \
                        or query_params in str(host_detail.username).lower():
                    pass
                else:
                    check = False
            if req_data.event_name:
                if str(req_data.event_name).lower() not in str(event.event_name).lower():
                    check = False
            if req_data.topic:
                if str(req_data.topic) not in str(event.topic):
                    check = False
            if req_data.start_at_start:
                if str(req_data.start_at_start) > str(event.start_at):
                    check = False
            if req_data.start_at_end:
                if str(req_data.start_at_end) < str(event.start_at):
                    check = False
            if req_data.end_at_start:
                if str(req_data.end_at_start) > str(event.end_at):
                    check = False
            if req_data.end_at_end:
                if str(req_data.end_at_end) < str(event.end_at):
                    check = False
            if check is True:
                res = event
                res.host_fullname = str(host_detail.last_name + ' ' + host_detail.first_name)
                res.host_username = host_detail.username
                res.host_email = host_detail.email
                res.images = self.get_event_images(db=db, event_id=event.id)
                response.append(res)

        start_idx = (pagination.page - 1) * pagination.page_size
        end_idx = min(pagination.page * pagination.page_size, len(response))

        return {
            'items': response[start_idx:end_idx],
            'pagination': {
                'current_page': pagination.page,
                'page_size': pagination.page_size,
                'total_items': len(response)
            }
        }

    def delete_event(self, event_id: int, user_id: str, db):
        if self.is_host_event(event_id, user_id, db) is False:
            raise CustomException(http_code=400, message="Don't have permission")
        crud_event.remove(db=db, id=event_id)

    def edit_event(self, event: EventCreateRequest, event_id: int, user_id: str, db):
        if self.is_host_event(event_id, user_id, db) is False:
            raise CustomException(http_code=400, message="Don't have permission")
        event_detail = crud_event.get(db=db, id=event_id)
        response = crud_event.update(db=db, db_obj=event_detail, obj_in=event.dict(exclude_none=True))

        image_requests = list()
        for image in event.images:
            image_request = EventImageDetail(
                event_id=event_id,
                image=image
            )
            image_requests.append(image_request)
        crud_event_image.create_multi(db=db, list_obj_in=image_requests)

        return response

    @staticmethod
    def is_host_event(event_id: int, user_id: str, db):
        event_detail = crud_event.get(db=db, id=event_id)
        if event_detail is None:
            raise CustomException(http_code=400, message='Event is not found')
        if event_detail.host_id == user_id:
            return True
        return False


event_srv = EventService()
