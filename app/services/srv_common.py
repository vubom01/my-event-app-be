import logging

import cloudinary.uploader
import app.core.connection

from typing import List
from fastapi import HTTPException, File

from app.crud.crud_event_image import crud_event_image

logger = logging.getLogger()


class CommonService:

    @staticmethod
    def upload_image(image: File):
        folder = "my_app_event/"
        result = cloudinary.uploader.upload(image, folder=folder)
        url = result.get('url')
        return {
            'url': url
        }

    @staticmethod
    def upload_list_images(images: List[File]):
        urls = []
        for image in images:
            file_name = " ".join(image.filename.strip().split())
            file_ext = file_name.split('.')[-1]
            if file_ext.lower() not in ('jpg', 'png', 'jpeg'):
                raise HTTPException(status_code=400, detail='Can not upload file ' + image.filename)
            urls.append(CommonService.upload_image(image=image.file))
        return urls

    @staticmethod
    def delete_image(image_urls: List[str]):
        crud_event_image.delete_images(image_urls)
        
