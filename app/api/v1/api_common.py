from typing import List
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session
from app.services.srv_common import CommonService
from app.helpers.login_manager import login_required
from fastapi_mail import FastMail, MessageSchema
from
router = APIRouter()

@router.post('/upload')
def upload_images(images: List[UploadFile] = File(...)):
    urls = []
    for image in images:
        file_name = " ".join(image.filename.strip().split())
        file_ext = file_name.split('.')[-1]
        if file_ext.lower() not in ('jpg', 'png', 'jpeg'):
            raise HTTPException(status_code=400, detail='Can not upload file ' + image.filename)
        urls.append(CommonService.upload_image(image=image.file))
    return {
        'urls': urls
    }
