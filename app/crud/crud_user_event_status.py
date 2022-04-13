from app.crud.crud_base import CRUDBase
from app.models.user_event_status_model import UserEventStatus
from app.schemas.sche_user_event_status import UserEventStatusDetail


class CRUDUserEventStatus(CRUDBase[UserEventStatusDetail, UserEventStatusDetail, UserEventStatusDetail]):

    def create(self):
        pass


crud_user_event_status = CRUDUserEventStatus(UserEventStatus)

