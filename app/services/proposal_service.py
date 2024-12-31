from fastapi import Depends
from app.core import get_session
from .base_service import BaseService
from app.models import Proposal
from sqlalchemy.ext.asyncio import AsyncSession

class ProposalService(BaseService[Proposal]):
    def __init__(self, db_session: AsyncSession):
        super().__init__(Proposal, db_session)
        
def get_proposal_service(
    db_session: AsyncSession = Depends(get_session),
) -> ProposalService:
    return ProposalService(db_session)