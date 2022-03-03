from fastapi import APIRouter

from app.api.v1 import api_healthcheck

router = APIRouter(prefix='/api')

router.include_router(api_healthcheck.router, tags=["healthcheck"], prefix="/healthcheck")
