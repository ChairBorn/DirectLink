from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class VoteBase(BaseModel):
    video_id: int

class VoteCreate(VoteBase):
    pass

class Vote(VoteBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class VideoBase(BaseModel):
    title: str
    url: str

class VideoCreate(VideoBase):
    pass

class Video(VideoBase):
    id: int
    owner_id: int
    created_at: datetime
    votes: List[Vote] = []

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    videos: List[Video] = []

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
