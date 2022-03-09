from typing import Optional

from fastapi import Request, Depends
from fastapi.security import HTTPBearer
from fastapi.security.utils import get_authorization_scheme_param

from app.auth0.auth0 import Auth0Service
from app.helpers.exception_handler import Unauthorized
from app.schemas.sche_user import UserDetail

authorize_header = HTTPBearer(
    scheme_name='Authorization', auto_error=False
)


async def get_current_user(request: Request = None, raw_token=Depends(authorize_header)) -> Optional[UserDetail]:
    if raw_token:
        scheme = 'bearer'
        token = raw_token
    else:
        scheme, token = get_authorization_scheme_param(request.headers.get('Authorization'))
    if scheme.lower() == "bearer":
        if not isinstance(token, str):
            token = token.credentials
        payload = Auth0Service().verify(token)

        if not payload:
            raise Unauthorized

        if payload.get("status") == "error":
            raise Unauthorized

        iam_info = UserDetail(id=payload.get('sub'))
        iam_info.name = payload.get('https://name.com')
        iam_info.email = payload.get('email')
        iam_info.permissions = payload.get('scope').split(' ') if payload.get('scope') else []
        iam_info.profile_picture = payload.get('picture')

        return iam_info
    raise Unauthorized
