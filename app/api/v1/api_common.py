from typing import List
from fastapi import APIRouter, File, UploadFile

from app.schemas.sche_base import DataResponse
from app.services.srv_common import CommonService

router = APIRouter()


@router.post('/upload')
def upload_images(images: List[UploadFile] = File(...)):
    urls = CommonService.upload_list_images(images=images)
    return DataResponse().success_response(data=urls)
