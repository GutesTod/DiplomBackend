from fastapi import Depends
from app.core import get_session
from .base_service import BaseService
from app.models import Moderation
from sqlalchemy.ext.asyncio import AsyncSession

class ModerationService(BaseService[Moderation]):
    def __init__(self, db_session: AsyncSession):
        super().__init__(Moderation, db_session)
        
def get_moderation_service(
    db_session: AsyncSession = Depends(get_session),
) -> ModerationService:
    return ModerationService(db_session)