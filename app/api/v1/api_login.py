from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import deps
from app.schemas.sche_base import DataResponse
from app.schemas.sche_user import UserDetail
from app.services.srv_user import UserService

router = APIRouter()




