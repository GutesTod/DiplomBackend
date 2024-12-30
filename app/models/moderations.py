# app/models/moderation.py
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum, String
from app.core.database import Base
from app.schemas.moderation import ModerationStatusEnum

class Moderation(Base):
    __tablename__ = 'moderation'
    moderation_id = Column(Integer, primary_key=True, autoincrement=True)
    issue_id = Column(Integer, ForeignKey('issues.issue_id'), nullable=True)
    proposal_id = Column(Integer, ForeignKey('proposals.proposal_id'), nullable=True)
    moderator_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    moderation_date = Column(DateTime, nullable=False)
    status = Column(Enum(ModerationStatusEnum), nullable=False)
    comment = Column(String)
