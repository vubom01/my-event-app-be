from typing import Any

import jwt
import logging

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from pydantic import ValidationError
from starlette import status
from sqlalchemy.orm import Session

from app.api import deps
from app.core.config import settings
from app.core.error import error_code, message
from app.core.security import get_password_hash, verify_password
from app.crud.crud_user import crud_user
from app.helpers.exception_handler import CustomException, ValidateException
from app.schemas.sche_token import TokenPayload
from app.schemas.sche_user import UserDetail, UserUpdateRequest

logger = logging.getLogger()


class UserService:

    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name='Authorization'
    )

    @staticmethod
    def authentication(db=None, username: str = None, password: str = None):
        user = crud_user.get_user_by_filter(db=db, username=username)

        if not user:
            raise CustomException(http_code=400, message='Incorrect username or password')
        if not verify_password(password, user.password):
            raise CustomException(http_code=400, message='Incorrect username or password')

        return user

    @staticmethod
    def get_current_user(db: Session = Depends(deps.get_db), http_authorization_credentials=Depends(reusable_oauth2),
                         user_id: int = None):
        if user_id is not None:
            return crud_user.get(db=db, id=user_id)
        else:
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
        user_detail = crud_user.get_user_by_filter(db=db, username=user.username)
        if user_detail:
            raise CustomException(http_code=400, message='Username is already in use')

        user_detail = crud_user.get_user_by_filter(db=db, email=user.email)
        if user_detail:
            raise CustomException(http_code=400, message='Email is already in use')

        user.password = get_password_hash(user.password)
        user = crud_user.create(db=db, obj_in=user)
        return user

    @staticmethod
    def update_user(db=None, user: UserUpdateRequest = None, user_detail: Any = None):
        if crud_user.get_user_by_filter(db=db, email=user.email):
            raise CustomException(http_code=400, message='Email is already in use')

        crud_user.update(db=db, db_obj=user_detail, obj_in=user.dict(exclude_none=True))
        return

    @staticmethod
    def update_password(db=None, current_password: str = None, update_password: str = None, user_detail: Any = None):
        if not verify_password(current_password, user_detail.password):
            raise ValidateException(error_code.ERROR_004_PASSWORD_IS_WRONG, message.MESSAGE_004_PASSWORD_IS_WRONG)
        crud_user.update(db=db, db_obj=user_detail, obj_in={'password': get_password_hash(update_password)})
        return

    @staticmethod
    def get_list_users(db=None, query_params: str = None, page: int = None, page_size: int = None, user_id: int = None):
        users = crud_user.get_all_users(db=db)

        response = []
        for user in users:
            full_name = str(user.last_name + user.first_name)
            if user.id == user_id:
                continue
            if query_params is None or query_params.lower() in full_name.lower() \
                    or query_params in str(user.email).lower() or query_params in str(user.username).lower():
                response.append(user)

        start_idx = (page - 1) * page_size
        end_idx = min(page * page_size, len(response))
        return {
            'items': response[start_idx:end_idx],
            'pagination': {
                'current_page': page,
                'page_size': page_size,
                'total_items': len(response)
            }
        }