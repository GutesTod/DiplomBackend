from pydantic import BaseModel
import enum

class VoteEnum(enum.Enum):
    YES = 'yes'
    NO = 'no'

class VoteCreate(BaseModel):
    user_id: int
    vote_type: VoteEnum

class VoteRead(BaseModel):
    vote_id: int
    user_id: int
    vote_type: VoteEnum

    class Config:
        orm_mode = True
