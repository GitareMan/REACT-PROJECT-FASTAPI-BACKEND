from pydantic import BaseModel


class Global(BaseModel):
    site_domain: str
    site_name: str
    site_title: str
    site_author: str
    site_email: str