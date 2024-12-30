from sqlalchemy import Column, Integer, String, Enum
from app.core.database import Base
from sqlalchemy.orm import relationship
from .issues import Issue
from .proposals import Proposal
from .votes import Vote
from app.schemas.user import RoleEnum

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    secondname = Column(String)
    role = Column(Enum(RoleEnum), nullable=False)

    issues = relationship("Issue", backref="users")
    proposals = relationship("Proposal", backref="users")
    votes = relationship("Vote", backref="users")
    moderations = relationship("Moderation", backref="users")
