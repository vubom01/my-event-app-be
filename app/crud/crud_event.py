from app.crud.crud_base import CRUDBase
from app.models.event_model import Event
from app.schemas.sche_event import EventDetail


class CRUDEvent(CRUDBase[EventDetail, EventDetail, EventDetail]):

    def filter(self):
        pass


crud_event = CRUDEvent(Event)
