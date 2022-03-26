from app.crud.crud_base import CRUDBase
from app.models.event_image_model import EventImage
from app.schemas.sche_event_image import EventImageDetail


class CRUDEventImage(CRUDBase[EventImageDetail, EventImageDetail, EventImageDetail]):

    def filter(self):
        pass


crud_event_image = CRUDEventImage(EventImage)
