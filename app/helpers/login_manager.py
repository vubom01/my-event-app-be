from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.api import deps
from app.schemas.sche_user import UserDetail
from app.services.srv_user import UserService


def login_required(db: Session = Depends(deps.get_db),
                   http_authorization_credentials=Depends(UserService.reusable_oauth2)):
    return UserService.get_current_user(db, http_authorization_credentials)


class PermissionRequired:
    def __init__(self, *args):
        self.user = None
        self.permissions = args

    def __call__(self, current_user: UserDetail = Depends(login_required)):
        self.user = current_user
        if self.user.role not in self.permissions and self.permissions:
            raise HTTPException(status_code=400,
                                detail=f'User ' + self.user.username + f' can not access this api')
