from typing import List

from sqlalchemy.orm import Session

from app.crud.crud_base import CRUDBase
from app.models.event_image_model import EventImage
from app.schemas.sche_event_image import EventImageDetail


class CRUDEventImage(CRUDBase[EventImageDetail, EventImageDetail, EventImageDetail]):

    def get_event_images(self, db: Session, event_id: int):
        return db.query(self.model).filter(self.model.event_id == event_id).all()

    def delete_images(self, db: Session, image_urls: List[str]):
        obj = db.query(self.model).filter(self.model.image.in_(image_urls)).delete()
        db.commit()
        return obj


crud_event_image = CRUDEventImage(EventImage)
