
from pydantic import BaseModel


class Post(BaseModel):
    id: str
    title: str
    text: str
    slug: str
    author: str
    youtube_link: str
    published_date: str
    picture: str


class PostUpdateModel(BaseModel):
    title: str
    text: str
    slug: str
    author: str
    youtube_link: str
    published_date: str
    picture: str



