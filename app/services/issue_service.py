from fastapi import Depends
from app.core import get_session
from .base_service import BaseService
from app.models import Issue
from sqlalchemy.ext.asyncio import AsyncSession

class IssueService(BaseService[Issue]):
    def __init__(self, db_session: AsyncSession):
        super().__init__(Issue, db_session)
        
def get_issue_service(
    db_session: AsyncSession = Depends(get_session),
) -> IssueService:
    return IssueService(db_session)
        