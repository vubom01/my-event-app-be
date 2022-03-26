import logging

from app.crud.crud_event import crud_event
from app.schemas.sche_event import EventCreateRequest, EventDetail

logger = logging.getLogger()


class EventService:

    @staticmethod
    def create_event(db=None, event: EventCreateRequest = None, user_id: str = None):
        request = EventDetail(**event.dict())
        request.host_id = user_id
        event = crud_event.create(db=db, obj_in=request)
        return event
