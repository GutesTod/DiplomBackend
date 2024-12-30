from .base_service import BaseService
from app.models import Moderation
from sqlalchemy.ext.asyncio import AsyncSession

class ModerationService(BaseService[Moderation]):
    def __init__(self, db_session: AsyncSession):
        super().__init__(Moderation, db_session)