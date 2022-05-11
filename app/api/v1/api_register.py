import random

from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session

from app.api import deps
from app.helpers.constant import LENGTH_OF_TERMINAL_CODE, LETTERS
from app.schemas.sche_base import DataResponse
from app.schemas.sche_user import UserDetailRequest
from app.services.srv_user import user_srv

router = APIRouter()


def random_code() -> str:
    random_string = ""
    for number in range(LENGTH_OF_TERMINAL_CODE):
        random_string += random.choice(LETTERS)
    return random_string


@router.post('')
def register(background_tasks: BackgroundTasks, db: Session = Depends(deps.get_db), user: UserDetailRequest = None):
    user.id = random_code()
    user = user_srv.create_user(db=db, user=user, background_tasks=background_tasks)
    return DataResponse().success_response(data={'user_id': user.id})
