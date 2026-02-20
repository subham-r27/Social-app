from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True #default value is true, if user left empty
    rating: Optional[int] = None

my_posts = [
    {"title":"test 1","content":"test 1 content","id":1},
    {"title":"Top Indian Foods","content":"Biryani, Chole Bhature, Pani Puri","id":2},
    ]

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p

@app.get("/")
def root():
    return {"message":"Welcome to my Social App"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post:Post):
    post_dict=post.dict()
    post_dict['id']=randrange(0,1000000)
    my_posts.append(post_dict)
    return {
        "data": post_dict
        }

@app.get("/posts/{id}")
def get_post(id : int):
    post=find_post(id)
    return {
        "post_detail":post, 
    }
