from sqlalchemy.orm import Session

from app.crud.crud_base import CRUDBase
from app.helpers.paging import PaginationParams
from app.models.message_model import Message
from app.schemas.sche_message import MessageDetail


class CRUDMessage(CRUDBase[MessageDetail, MessageDetail, MessageDetail]):

    def get_message(self, event_id: int, page: int, page_size: int, db: Session):
        query = db.query(self.model).filter(self.model.event_id == event_id)
        pagination = PaginationParams(
            page=page,
            page_size=page_size,
            sort_by='created_at',
            direction='desc'
        )
        message = self.paginate(query, pagination)
        return message


crud_message = CRUDMessage(Message)
