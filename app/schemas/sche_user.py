from typing import Optional, List

from pydantic.main import BaseModel


class UserDetail(BaseModel):
    id: str
    email: Optional[str] = ''
    name: Optional[str] = ''
    profile_picture: Optional[str] = ''
    permissions: Optional[List[str]]
