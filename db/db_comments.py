from sqlalchemy import select
from sqlalchemy.orm import Session
from db.models import DbComment
from routers.schemas import CommentBase


def create(db: Session,  request: CommentBase):
    new_comment = DbComment(
        text=request.text,
        username=request.username,
        post_id=request.post_id,
    )

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def get_all(db: Session, post_id: int):

    query = select(DbComment).where(DbComment.id == post_id)
    return db.execute(query).scalars().all()
