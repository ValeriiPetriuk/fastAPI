import shutil
from typing import List

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session

from auth.oauth2 import get_current_user
from db.database import get_db
from db.db_post import create_post, all_posts, delete_post
from routers.schemas import PostBase, PostDisplay, UserAuth
import uuid

router = APIRouter(
    prefix="/post",
    tags=['post']
)

image_url_types = ['absolute', 'relative']


@router.post('/', response_model=PostDisplay)
def create(request: PostBase,  db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(status_code=422, detail='images url can only take values  absolute or relative')

    return create_post(db, request)


@router.get('/all', response_model=List[PostDisplay])
def get_all_posts(db: Session = Depends(get_db)):
    return all_posts(db)


@router.post('/image')
def upload_image(image: UploadFile = File(...), current_user: UserAuth = Depends(get_current_user)):
    rand_str = f'_{uuid.uuid4()}.'
    filename = rand_str.join(image.filename.rsplit('.', 1))
    path = f"images/{filename}"

    with open(path, 'wb') as buffer:
        shutil.copyfileobj(image.file, buffer)
    return {'filename': path}


@router.delete('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return delete_post(db, id, current_user.id)