from fastapi import APIRouter, status, HTTPException
from config import settings

from typing import List

from data import posts, tutors, projects, globals
from tutors import Tutorial
from posts import *
from projects import Project
from globals import Global

router = APIRouter(
    prefix= settings.API_V1_STR
)


@router.get("/posts", response_model=List[Post])
async def get_all_posts():
    return posts


#@app.post("/api/v1/posts", status_code=status.HTTP_201_CREATED)
#async def create_a_post(post_data: Post) -> dict:
#   new_post = post_data.model_dump()

    posts.append(new_post)

    return new_post



@router.get("/post/{slug}")
async def get_post(slug: str) -> dict:
    for post in posts:
        if post["slug"] == slug:
            return post

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


#@app.patch("/api/v1/post/{post_id}")
#async def update_post(post_id: str,post_update_data:PostUpdateModel) -> dict:

    for post in posts:
        if post['id'] == post_id:
            post['title'] = post_update_data.title
            post['text'] = post_update_data.text
            post['author'] = post_update_data.author
            post['picture'] = post_update_data.picture
            post['published_date'] = post_update_data.published_date
            post['youtube_link'] = post_update_data.youtube_link
            post['slug'] = post_update_data.slug

            return post

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")


#@app.delete("/api/v1/post/{post_id}",status_code=status.HTTP_204_NO_CONTENT)
#async def delete_post(post_id: str):
    for post in posts:
        if post["id"] == post_id:
            posts.remove(post)

            return {}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")




@router.get("/tutorials", response_model=List[Tutorial])
async def get_all_tutorials():
    return tutors




@router.get("/projects", response_model=List[Project])
async def get_all_projects():
    return projects



@router.get("/globals", response_model=List[Global])
async def get_all_globals():
    return globals
