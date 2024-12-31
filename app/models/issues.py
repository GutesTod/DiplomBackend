from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from app.core.database import Base
from sqlalchemy.orm import relationship
from .archives import Archive
from .moderations import Moderation
from app.schemas.issue import StatusEnum, PriorityEnum

class Issue(Base):
    __tablename__ = 'issues'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(Enum(StatusEnum), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    priority = Column(Enum(PriorityEnum), nullable=False)
    
    archive = relationship("Archive", backref="issues", cascade="all, delete-orphan")
    moderations = relationship("Moderation", backref="issues", cascade="all, delete-orphan")
    
