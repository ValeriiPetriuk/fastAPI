from sqlalchemy.orm import Session

from db.models import DbUser
from sqlalchemy.exc import IntegrityError
from routers.schemas import UserBase
from fastapi import HTTPException, status
from db.hashing import bcrypt_hash


def create_user(db: Session, request: UserBase):
    try:
        new_user = DbUser(
            username=request.username,
            email=request.email,
            password=bcrypt_hash(request.password)
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError as e:
        raise HTTPException(status_code=404, detail="username uses")


def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
