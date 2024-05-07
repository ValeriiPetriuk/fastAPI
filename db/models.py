import datetime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import String, DateTime, ForeignKey
from .database import Base
from typing import List
from sqlalchemy.sql import func


class DbUser(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(255), unique=True)
    email: Mapped[str]
    password: Mapped[str]
    items: Mapped[List["DbPost"]] = relationship(back_populates="user")


class DbPost(Base):
    __tablename__ = 'post'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    image_url: Mapped[str]
    image_url_type: Mapped[str] = mapped_column(String(10))
    caption: Mapped[str]
    timestamp: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped["DbUser"] = relationship(back_populates="items")
    comments: Mapped[List["DbComment"]] = relationship(back_populates="post")


class DbComment(Base):
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    text: Mapped[str]
    username: Mapped[str] = mapped_column(String(255))
    timestamp: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'))
    post: Mapped["DbPost"] = relationship(back_populates='comments')







