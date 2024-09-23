from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud, auth
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(
    prefix="/videos",
    tags=["videos"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(auth.get_db)):
    # Same as in users.py
    return auth.get_current_user(token, db)

@router.post("/", response_model=schemas.Video)
def create_video(video: schemas.VideoCreate, 
                db: Session = Depends(auth.get_db), 
                current_user: schemas.User = Depends(get_current_user)):
    return crud.create_video(db=db, video=video, user_id=current_user.id)

@router.get("/", response_model=List[schemas.Video])
def read_videos(skip: int = 0, limit: int = 10, db: Session = Depends(auth.get_db)):
    videos = crud.get_videos(db, skip=skip, limit=limit)
    return videos
