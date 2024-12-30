from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ArchiveCreate(BaseModel):
    issue_id: Optional[int]
    proposal_id: Optional[int]
    vote_id: int
    archive_date: datetime

class ArchiveRead(BaseModel):
    archive_id: int
    issue_id: Optional[int]
    proposal_id: Optional[int]
    vote_id: int
    archive_date: datetime

    class Config:
        orm_mode = True
