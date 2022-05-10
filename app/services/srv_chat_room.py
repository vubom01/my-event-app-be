import logging

from app.crud.crud_event import crud_event
from app.crud.crud_message import crud_message
from app.crud.crud_user import crud_user
from app.crud.crud_user_event_status import crud_user_event_status
from app.helpers.exception_handler import CustomException
from app.schemas.sche_message import Message

logger = logging.getLogger()


class ChatRoomService(object):

    @staticmethod
    def is_user_event(event_id, user_id, db):
        event_detail = crud_event.get(db, event_id)
        if event_detail is None:
            raise CustomException(http_code=400, message="Event not found")

        user_event_status = crud_user_event_status.get_user_event_status(db, event_id, user_id)
        if (user_event_status is None or user_event_status.status == 0) and event_detail.host_id != user_id:
            raise CustomException(http_code=400, message="Don't have permission")

    def send_message(self, event_id: int, user_id: str, message: str, db):
        self.is_user_event(event_id, user_id, db)
        data = Message(
            event_id=event_id,
            user_id=user_id,
            message=message
        )
        resp = crud_message.create(db=db, obj_in=data)
        return resp.id

    def get_message(self, event_id: int, user_id: int, page: int, page_size: int, db):
        self.is_user_event(event_id, user_id, db)

        message = crud_message.get_message(event_id=event_id, page=page, page_size=page_size, db=db)
        for item in message.items:
            user_detail = crud_user.get(db=db, id=item.user_id)
            full_name = str(user_detail.last_name + ' ' + user_detail.first_name)
            item.user_name = full_name
            item.user_image = user_detail.avatar

        event_detail = crud_event.get(db=db, id=event_id)

        return {
            'event_id': event_id,
            'event_name': event_detail.event_name,
            'items': message.items,
            'pagination': message.pagination
        }


chat_room_srv = ChatRoomService()
