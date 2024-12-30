from .base_service import BaseService
from app.models import User
from sqlalchemy.ext.asyncio import AsyncSession

class UserService(BaseService[User]):
    def __init__(self, db_session: AsyncSession):
        super().__init__(User, db_session)