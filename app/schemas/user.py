from pydantic import BaseModel
from typing import Optional
import enum

class RoleEnum(enum.Enum):
    ADMIN = 'admin'
    USER = 'user'
    MODERATOR = 'moderator'

class UserCreate(BaseModel):
    email: str
    name: str
    surname: str
    secondname: Optional[str]
    role: RoleEnum

class UserRead(BaseModel):
    user_id: int
    email: str
    name: str
    surname: str
    secondname: Optional[str]
    role: RoleEnum

    class Config:
        orm_mode = True
