from sqlalchemy import Column, Integer, ForeignKey, DateTime
from app.core.database import Base

class Archive(Base):
    __tablename__ = 'archive'
    id = Column(Integer, primary_key=True, autoincrement=True)
    issue_id = Column(Integer, ForeignKey('issues.id'), nullable=True)
    proposal_id = Column(Integer, ForeignKey('proposals.id'), nullable=True)
    vote_id = Column(Integer, ForeignKey('votes.id'), nullable=False)
    archive_date = Column(DateTime, nullable=False)
