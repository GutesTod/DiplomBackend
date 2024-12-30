from .base_service import BaseService
from app.models import Proposal
from sqlalchemy.ext.asyncio import AsyncSession

class ProposalService(BaseService[Proposal]):
    def __init__(self, db_session: AsyncSession):
        super().__init__(Proposal, db_session)