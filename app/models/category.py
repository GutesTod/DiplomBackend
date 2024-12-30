from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .issues import Issue
from .proposals import Proposal
from app.core.database import Base

class Category(Base):
    __tablename__ = 'category'
    category_id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String, nullable=False)
    
    issues = relationship("Issue", backref="category")
    proposals = relationship("Proposal", backref="category")