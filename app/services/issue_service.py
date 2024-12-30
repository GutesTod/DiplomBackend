from .base_service import BaseService
from app.models import Issue
from sqlalchemy.ext.asyncio import AsyncSession

class IssueService(BaseService[Issue]):
    def __init__(self, db_session: AsyncSession):
        super().__init__(Issue, db_session)