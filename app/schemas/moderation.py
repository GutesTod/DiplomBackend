from pydantic import BaseModel
from datetime import datetime
from typing import Optional
import enum

class ModerationStatusEnum(enum.Enum):
    SUCCESS = 'success'
    NONSUCCESS = 'nonsuccess'

class ModerationCreate(BaseModel):
    issue_id: Optional[int]
    proposal_id: Optional[int]
    moderator_id: int
    moderation_date: datetime
    status: ModerationStatusEnum
    comment: Optional[str]

class ModerationRead(BaseModel):
    moderation_id: int
    issue_id: Optional[int]
    proposal_id: Optional[int]
    moderator_id: int
    moderation_date: datetime
    status: ModerationStatusEnum
    comment: Optional[str]

    class Config:
        orm_mode = True
