from fastapi import APIRouter, Depends
from pydantic.main import BaseModel
from sqlalchemy.orm import Session

from app.api import deps
from app.core.security import create_access_token
from app.helpers.exception_handler import CustomException
from app.schemas.sche_base import DataResponse
from app.schemas.sche_token import Token
from app.services.srv_user import UserService

router = APIRouter()


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post('', response_model=DataResponse[Token])
def login(db: Session = Depends(deps.get_db), request: LoginRequest = None):
    user = UserService.authentication(db=db, username=request.username, password=request.password)
    if not user:
        raise CustomException(http_code=400, message='Incorrect username or password')
    return DataResponse().success_response(Token(access_token=create_access_token(user_id=user.id)))


