
import uvicorn
from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from tutors import Tutorial
from posts import *
from projects import Project
from globals import Global

from data import *

app = FastAPI(debug=True)

origins = [
    "http://localhost:8080",
    # Add more origins here
]

api_slug = "/api/v1/"

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/api/v1/posts", response_model=List[Post])
async def get_all_posts():
    return posts


#@app.post("/api/v1/posts", status_code=status.HTTP_201_CREATED)
#async def create_a_post(post_data: Post) -> dict:
#   new_post = post_data.model_dump()

    posts.append(new_post)

    return new_post



@app.get("/api/v1/post/{slug}")
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




@app.get("/api/v1/tutorials", response_model=List[Tutorial])
async def get_all_tutorials():
    return tutors




@app.get("/api/v1/projects", response_model=List[Project])
async def get_all_projects():
    return projects



@app.get("/api/v1/globals", response_model=List[Global])
async def get_all_globals():
    return globals



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)