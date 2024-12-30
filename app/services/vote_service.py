from .base_service import BaseService
from app.models import Vote
from sqlalchemy.ext.asyncio import AsyncSession

class VoteService(BaseService[Vote]):
    def __init__(self, db_session: AsyncSession):
        super().__init__(Vote, db_session)