from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from random import randrange
from fastapi import Response,HTTPException,status

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

def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/")
def root():
    return {"message":"Welcome to my Social App"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post:Post):
    post_dict=post.dict()
    post_dict['id']=randrange(0,1000000)
    my_posts.append(post_dict)
    return {
        "data": post_dict
        }

@app.get("/posts/{id}")
def get_post(id : int,response : Response):
    post=find_post(id)
    if not post :
        #response.status_code=status.HTTP_404_NOT_FOUND
        raise HTTPException(
            status_code=404, 
            detail=f"post with id {id} was not found"
            )
    return {
        "post_detail":post, 
    }

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id : int):
    #find index in the array
    index=find_index_post(id)
    if index == None:
        raise HTTPException(
            status_code=404, 
            detail=f"post with id {id} was not found"
            )
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id : int, post:Post):
    index=find_index_post(id)
    if index == None:
        raise HTTPException(
            status_code=404, 
            detail=f"post with id {id} was not found"
            )
    post_dict=post.dict()
    post_dict['id']=id
    my_posts[index]=post_dict
    return {"data": post_dict}