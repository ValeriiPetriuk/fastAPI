from typing import List

from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from auth.oauth2 import get_current_user
from db.database import get_db
from db.db_comments import create, get_all
from routers.schemas import CommentBase, UserAuth, Comments

router = APIRouter(
    prefix="/comment",
    tags=['comment']
)


@router.post('/create', response_model=CommentBase)
def create_comment(request: CommentBase, db: Session = Depends(get_db),
                   current_user: UserAuth = Depends(get_current_user)):
    return create(db, request)


@router.get('/all/{post_id}')
def comments(post_id: int, db: Session = Depends(get_db)):
    return get_all(db, post_id)