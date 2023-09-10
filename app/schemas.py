from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class userCreate(BaseModel):
    email : EmailStr
    password : str

class userOut(BaseModel):
    id: int
    email: EmailStr
    created_at : datetime

    class Config:
        from_attributes = True
        # orm_mode = True
    

class BlogCreate(BaseModel):
    blog_title : str
    blog_content : str
    published : bool = True


class BlogOut(BlogCreate):
    blog_id : int
    created_at : datetime
    user_id : int


class token(BaseModel):
    access_token: str
    token_type: str


class tokenData(BaseModel):
    id: Optional[int] = None