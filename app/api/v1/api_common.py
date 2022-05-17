from typing import List, Optional
from fastapi import APIRouter, File, UploadFile, Depends
from fastapi_mail import MessageSchema, FastMail
from pydantic import EmailStr
from sqlalchemy.orm import Session

from app.api import deps
from app.core import email_handle
from app.core.config import mail_config
from app.helpers.login_manager import login_required
from app.schemas.sche_base import DataResponse, ItemBaseModel
from app.schemas.sche_email import BodyEmail
from app.services.srv_common import CommonService

router = APIRouter()


class Image(ItemBaseModel):
    image_urls: List[str]


@router.post('/upload')
def upload_images(images: List[UploadFile] = File(...)):
    urls = CommonService.upload_list_images(images=images)
    return DataResponse().success_response(data=urls)


@router.delete('/delete')
def delete_images(request: Image, db: Session = Depends(deps.get_db)):
    data = CommonService.delete_image(image_urls=request.image_urls, db=db)
    return DataResponse().success_response(data=data)


@router.post('/email', dependencies=[Depends(login_required)])
async def send_mail(emails: List[EmailStr], body_mail: BodyEmail):
    message = MessageSchema(
        subject=body_mail.subject,
        recipients=emails,
        body=body_mail.body
    )
    fm = FastMail(mail_config)
    await fm.send_message(message)
    return {
        'message': 'email has been sent'
    }
