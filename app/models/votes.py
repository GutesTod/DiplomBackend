from sqlalchemy import Column, Integer, ForeignKey, Enum
from app.core.database import Base
from .archives import Archive
from sqlalchemy.orm import relationship
from app.schemas.vote import VoteEnum

class Vote(Base):
    __tablename__ = 'votes'
    vote_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    vote_type = Column(Enum(VoteEnum), nullable=False)
    
    archive = relationship("Archive", backref="votes")
