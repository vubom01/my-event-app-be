from fastapi import APIRouter

from app.api.v1 import api_healthcheck, api_login, api_register, api_user, api_common, api_event, api_friend, \
    api_chat_room

router = APIRouter(prefix='/api')

router.include_router(api_healthcheck.router, tags=["healthcheck"], prefix="/healthcheck")
router.include_router(api_common.router, tags=["common"], prefix="/common")
router.include_router(api_login.router, tags=["login"], prefix="/login")
router.include_router(api_register.router, tags=["register"], prefix="/register")
router.include_router(api_user.router, tags=["users"], prefix="/users")
router.include_router(api_event.router, tags=["events"], prefix="/events")
router.include_router(api_friend.router, tags=["friends"], prefix='/friends')
router.include_router(api_chat_room.router, tags=["chat room"], prefix='/chat_room')
