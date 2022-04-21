import logging
from typing import List

from app.crud.crud_event import crud_event
from app.crud.crud_event_image import crud_event_image
from app.crud.crud_like_event import crud_like_event
from app.crud.crud_user_event_status import crud_user_event_status
from app.helpers.paging import PaginationParamsRequest
from app.models.like_event_model import LikeEvent
from app.models.user_event_status_model import UserEventStatus
from app.schemas.sche_event import EventCreateRequest, EventDetail, EventsRequest
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
        images = self.get_event_images(db=db, event_id=event_id)
        if event is None:
            raise CustomException(http_code=400, message='Event is not exist')
        if event.status == 1 or event.host_id == user_id:
            event.images = images
            return event
        else:
            user_event_status = crud_user_event_status.get_user_event_status(db=db, event_id=event_id, user_id=user_id)
            if user_event_status is not None and user_event_status.status == 2:
                event.images = images
                return event
            else:
                raise CustomException(http_code=400, message='User is not invited to the event')

    @staticmethod
    def get_event_requests(db=None, status=None, user_id: str = None):
        return {
            'event_requests': crud_user_event_status.get_event_requests(db=db, status=status, user_id=user_id)
        }

    def like_event(self, db=None, event_id: int = None, user_id: str = None):
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

    @staticmethod
    def unlike_event(db=None, event_id: int = None, user_id: str = None):
        like_event_detail = crud_like_event.get_like_event(db=db, event_id=event_id, user_id=user_id)
        if like_event_detail is None:
            raise CustomException(http_code=400, message='User cannot this access')
        else:
            crud_like_event.remove(db=db, id=like_event_detail.id)


event_srv = EventService()
