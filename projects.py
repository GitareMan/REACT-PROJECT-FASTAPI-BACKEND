from pydantic import BaseModel

class Project(BaseModel):
    title: str
    description: str
    longDescription: str
    video_link: str
    download_link: str
