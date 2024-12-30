from pydantic import BaseModel
from typing import Optional
import enum

class StatusEnum(enum.Enum):
    NEW = 'new'
    IN_PROGRESS = 'inProgress'
    FINALLY = 'finally'

class PriorityEnum(enum.Enum):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

class ProposalCreate(BaseModel):
    user_id: int
    title: str
    description: Optional[str]
    status: StatusEnum
    category_id: int
    priority: PriorityEnum

class ProposalRead(BaseModel):
    proposal_id: int
    user_id: int
    title: str
    description: Optional[str]
    status: StatusEnum
    category_id: int
    priority: PriorityEnum

    class Config:
        orm_mode = True
