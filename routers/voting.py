from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, auth

router = APIRouter(
    prefix="/voting",
    tags=["voting"],
)

@router.post("/", response_model=schemas.Vote)
def create_vote(vote: schemas.VoteCreate, 
               db: Session = Depends(auth.get_db), 
               current_user: schemas.User = Depends(auth.get_current_user)):
    # Check if user has already voted for this video
    existing_vote = db.query(crud.models.Vote).filter(
        crud.models.Vote.user_id == current_user.id,
        crud.models.Vote.video_id == vote.video_id
    ).first()
    if existing_vote:
        raise HTTPException(status_code=400, detail="Already voted for this video")
    return crud.create_vote(db=db, vote=vote, user_id=current_user.id)

@router.get("/video/{video_id}/count", response_model=int)
def get_vote_count(video_id: int, db: Session = Depends(auth.get_db)):
    return crud.get_votes_for_video(db, video_id=video_id)
