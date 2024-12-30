from sqlalchemy import Column, Integer, ForeignKey, DateTime
from app.core.database import Base

class Archive(Base):
    __tablename__ = 'archive'
    archive_id = Column(Integer, primary_key=True, autoincrement=True)
    issue_id = Column(Integer, ForeignKey('issues.issue_id'), nullable=True)
    proposal_id = Column(Integer, ForeignKey('proposals.proposal_id'), nullable=True)
    vote_id = Column(Integer, ForeignKey('votes.vote_id'), nullable=False)
    archive_date = Column(DateTime, nullable=False)
