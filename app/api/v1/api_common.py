from typing import List, Optional
from fastapi import APIRouter, File, UploadFile, Depends
from fastapi_mail import MessageSchema, FastMail
from pydantic import EmailStr

from app.core.config import mail_config
from app.helpers.login_manager import login_required
from app.schemas.sche_base import DataResponse, ItemBaseModel
from app.services.srv_common import CommonService

router = APIRouter()


# class BodyEmail(ItemBaseModel):
#     subject: Optional[str]
#     body: str


@router.post('/upload')
def upload_images(images: List[UploadFile] = File(...)):
    urls = CommonService.upload_list_images(images=images)
    return DataResponse().success_response(data=urls)


# @router.post('/email', dependencies=[Depends(login_required)])
# async def send_mail(emails: List[EmailStr], body_mail: BodyEmail):
#     message = MessageSchema(
#         subject=body_mail.subject,
#         recipients=emails,
#         body=body_mail.body
#     )
#     fm = FastMail(mail_config)
#     await fm.send_message(message)
#     return {
#         'message': 'email has been sent'
#     }
