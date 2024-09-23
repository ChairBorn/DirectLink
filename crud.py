from sqlalchemy.orm import Session
from . import models, schemas

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate, hashed_password: str):
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_video(db: Session, video: schemas.VideoCreate, user_id: int):
    db_video = models.Video(**video.dict(), owner_id=user_id)
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video

def get_videos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Video).offset(skip).limit(limit).all()

def create_vote(db: Session, vote: schemas.VoteCreate, user_id: int):
    db_vote = models.Vote(**vote.dict(), user_id=user_id)
    db.add(db_vote)
    db.commit()
    db.refresh(db_vote)
    return db_vote

def get_votes_for_video(db: Session, video_id: int):
    return db.query(models.Vote).filter(models.Vote.video_id == video_id).count()
