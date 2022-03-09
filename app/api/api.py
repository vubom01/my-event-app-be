from fastapi import APIRouter

from app.api.v1 import api_healthcheck, api_login, api_register

router = APIRouter(prefix='/api')

router.include_router(api_healthcheck.router, tags=["healthcheck"], prefix="/healthcheck")
router.include_router(api_login.router, tags=["login"], prefix="/login")
router.include_router(api_register.router, tags=["register"], prefix="/register")
