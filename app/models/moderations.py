# app/models/moderation.py
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum, String
from app.core.database import Base
from app.schemas.moderation import ModerationStatusEnum

class Moderation(Base):
    __tablename__ = 'moderation'
    id = Column(Integer, primary_key=True, autoincrement=True)
    issue_id = Column(Integer, ForeignKey('issues.id'), nullable=True)
    proposal_id = Column(Integer, ForeignKey('proposals.id'), nullable=True)
    moderator_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    moderation_date = Column(DateTime, nullable=False)
    status = Column(Enum(ModerationStatusEnum), nullable=False)
    comment = Column(String)
