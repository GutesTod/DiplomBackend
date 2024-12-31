from fastapi import Depends
from app.core import get_session
from .base_service import BaseService
from app.models import User
from sqlalchemy.ext.asyncio import AsyncSession

class UserService(BaseService[User]):
    def __init__(self, db_session: AsyncSession):
        super().__init__(User, db_session)
        
def get_user_service(
    db_session: AsyncSession = Depends(get_session),
) -> UserService:
    return UserService(db_session)