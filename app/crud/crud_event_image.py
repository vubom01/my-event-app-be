from typing import List
from sqlalchemy.orm import Session

from app.crud.crud_base import CRUDBase
from app.models.event_image_model import EventImage
from app.schemas.sche_event_image import EventImageDetail


class CRUDEventImage(CRUDBase[EventImageDetail, EventImageDetail, EventImageDetail]):

    def get_event_images(self, db: Session, event_id: int):
        return db.query(self.model).filter(self.model.event_id == event_id).all()

<<<<<<< Updated upstream
    def delete_images(self, db: Session, image_urls: list[str]):
=======
    def delete_images(self, db: Session, image_urls: List[str]):
>>>>>>> Stashed changes
        obj = db.query(self.model).filter(self.model.image.in_(image_urls)).all()
        db.delete(obj)
        db.commit()




crud_event_image = CRUDEventImage(EventImage)
