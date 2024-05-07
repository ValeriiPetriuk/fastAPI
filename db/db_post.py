from fastapi import HTTPException
from sqlalchemy.orm import Session

from db.models import DbPost
from routers.schemas import PostBase


def create_post(db: Session, request: PostBase):

    new_post = DbPost(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        user_id=request.creator_id
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def all_posts(db: Session):
    return db.query(DbPost).all()


def delete_post(db: Session, id: int, user_id: int):
    post = db.query(DbPost).filter(DbPost.id == id).first()
    if not post:
        raise HTTPException(status_code=404, detail='Post not found')
    if post.user_id != user_id:
        raise HTTPException(status_code=403, detail='Only post creator can delete post')
    db.delete(post)
    db.commit()
    return 'ok'
