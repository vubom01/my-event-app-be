from app.core.config import settings
import cloudinary as cloudinary
import fastapi_mail
cloudinary.config(
    cloud_name = settings.CLOUD_NAME,
    api_key=settings.API_KEY,
    api_secret=settings.API_SECRET
)
