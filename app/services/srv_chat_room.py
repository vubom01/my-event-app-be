import logging

from app.crud.crud_event import crud_event
from app.crud.crud_event_image import crud_event_image
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

    def get_message(self, event_id: int, user_id: str, page: int, page_size: int, db):
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

    def get_rooms(self, user_id: str, event_name: str, page: int, page_size: int, db):
        events = []
        all_events = crud_event.get_all_events(db=db)
        for event in all_events:
            try:
                self.is_user_event(event.id, user_id, db)
                events.append(event)
            except:
                pass

        response = []
        if event_name:
            for event in events:
                if str(event_name).lower() in str(event.event_name).lower():
                    response.append(event)
        else:
            response = events

        events = []
        for event in response:
            last_message = crud_message.get_last_message(event_id=event.id, db=db)
            if last_message:
                event.user_id = last_message.user_id
                event.message = last_message.message
                events.append(event)

        start_idx = (page - 1) * page_size
        end_idx = min(page * page_size, len(response))

        response = events[start_idx:end_idx]
        for event in response:
            user_detail = crud_user.get(db=db, id=event.user_id)
            event.user_name = str(user_detail.last_name + ' ' + user_detail.first_name)
            event.images = self.get_event_images(db=db, event_id=event.id)
            event.event_id = event.id

        return {
            'items': response,
            'pagination': {
                'current_page': page,
                'page_size': page_size,
                'total_items': len(events)
            }
        }

    @staticmethod
    def get_event_images(db, event_id: int):
        event_images = crud_event_image.get_event_images(db=db, event_id=event_id)
        response = []
        for event_image in event_images:
            response.append(event_image.image)
        return response


chat_room_srv = ChatRoomService()
