from multiprocessing import synchronize
from fastapi import FastAPI,Response,HTTPException,status,Depends
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models,schemas,utils
from .database import engine,get_db
from .routers import user,post,auth



models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host='localhost',database='Social-App',user='postgres',password='Subh@m14308',cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful")
        break

    except Exception as error:
        print("Error connecting to the database")
        print("Error: ",error)
        time.sleep(2)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message":"Welcome to my Social App"}



