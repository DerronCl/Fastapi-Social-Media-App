
from fastapi.params import Body
from multiprocessing import synchronize
from typing import Optional, List
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
from passlib.context import CryptContext
import psycopg2
from psycopg2.extras import RealDictCursor
import time 
import models as models
import auth2
import schemas as schemas
import utils as utils 
from sqlalchemy.sql.functions import mode 
from database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session
from typing import List
from router import post, user, auth

# POST: to create data.
# GET: to read data.
# PUT: to update data.
# DELETE: to delete data.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated ="auto")
models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/") #Decorator where .get("/") is Path operation code or Route code 
async def root(): #path operation
    return {"message": "The grind begins"}

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

while True:
    try: 
        conn = psycopg2.connect(host ='localhost', database='fastapi', 
        user='postgres', password='Coltsfan123', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Database connection was successful')
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error:", error)
        time.sleep(2)


my_posts = [{"title": "title of post 1", 
"content": "content of post 1", 
"id" : 1}, {"title" : "favortie foods", "content": "I like pizza", "id" : 2}]

def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p 

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
