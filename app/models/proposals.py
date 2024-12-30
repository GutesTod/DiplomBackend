from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from app.core.database import Base
from sqlalchemy.orm import relationship
from .archives import Archive
from .moderations import Moderation
from app.schemas.proposal import StatusEnum, PriorityEnum

class Proposal(Base):
    __tablename__ = 'proposals'
    proposal_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(Enum(StatusEnum), nullable=False)
    category_id = Column(Integer, ForeignKey('category.category_id'), nullable=False)
    priority = Column(Enum(PriorityEnum), nullable=False)
    
    archive = relationship("Archive", backref="proposals")
    moderations = relationship("Moderation", backref="proposals")