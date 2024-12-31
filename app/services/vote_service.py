from fastapi import Depends
from app.core import get_session
from .base_service import BaseService
from app.models import Vote
from sqlalchemy.ext.asyncio import AsyncSession

class VoteService(BaseService[Vote]):
    def __init__(self, db_session: AsyncSession):
        super().__init__(Vote, db_session)
        
def get_vote_service(
    db_session: AsyncSession = Depends(get_session),
) -> VoteService:
    return VoteService(db_session)