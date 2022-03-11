from msilib.schema import File
import jwt
import logging

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from pydantic import ValidationError
from starlette import status
from sqlalchemy.orm import Session

from app.api import deps
from app.core.config import settings
from app.core.security import get_password_hash, verify_password
from app.crud.crud_user import crud_user
from app.helpers.exception_handler import CustomException
from app.schemas.sche_token import TokenPayload
from app.schemas.sche_user import UserDetail
import cloudinary.uploader
import app.core.connection

logger = logging.getLogger()

class CommonService:

    __instance = None

    reusable_oauth2 = HTTPBearer(
        scheme_name = 'Authorization'
    )

    @staticmethod
    def upload_image(image: File):
        folder = "my_app_event/"
        result = cloudinary.uploader.upload(image, folder=folder)
        url = result.get('url')
        return {
            'url': url
        }
