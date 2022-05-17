from typing import List

from fastapi_mail import MessageSchema, FastMail
from pydantic import EmailStr

from app.core.config import mail_config
from app.schemas.sche_email import BodyEmail


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
