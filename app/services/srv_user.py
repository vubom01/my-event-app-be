import jwt
import logging

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from pydantic import ValidationError
from starlette import status

from app.core.config import settings
from app.core.security import get_password_hash
from app.crud.crud_user import crud_user
from app.schemas.sche_token import TokenPayload
from app.schemas.sche_user import UserDetail

logger = logging.getLogger()


class UserService:

    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def get_current_user(db=None, http_authorization_credentials=Depends(reusable_oauth2)):
        try:
            payload = jwt.decode(
                http_authorization_credentials.credentials, settings.SECRET_KEY,
                algorithms=[settings.SECURITY_ALGORITHM]
            )
            token_data = TokenPayload(**payload)
        except(jwt.PyJWTError, ValidationError):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Could not validate credentials",
            )
        return crud_user.get(db=db, id=token_data.user_id)

    @staticmethod
    def create_user(db=None, user: UserDetail = None):
        user.password = get_password_hash(user.password)
        user = crud_user.create(db=db, obj_in=user)
        return user.username
