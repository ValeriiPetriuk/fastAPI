from typing import List

from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username: str
    email: str


class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: int


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username: str


class Comments(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    text: str
    username: str


class PostDisplay(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    image_url: str
    image_url_type: str
    caption: str
    user: User
    comments: List[Comments] = []


class UserAuth(BaseModel):
    id: int
    username: str
    email: str


class CommentBase(BaseModel):
    username: str
    text: str
    post_id: int