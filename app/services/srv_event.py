import logging
from typing import List

from app.crud.crud_event import crud_event
from app.crud.crud_event_image import crud_event_image
from app.schemas.sche_event import EventCreateRequest, EventDetail
from app.schemas.sche_event_image import EventImageDetail

logger = logging.getLogger()


class EventService:

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
            crud_event_image.create(db=db, obj_in=image_request)
            image_requests.append(image_request)
        # crud_event_image.create_multi(db=db, list_obj_in=image_requests)

        return {
            "id": response.id
        }
