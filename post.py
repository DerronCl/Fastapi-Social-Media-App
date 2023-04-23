from fastapi import APIRouter, FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session
import models, schemas, utils, database
from sqlalchemy.sql.functions import mode 
from typing import Optional, List
import auth2 


router = APIRouter(
    prefix= "/posts",
    tags= ['Posts']
)


@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db),current_user: int = Depends(auth2.get_current_user)):
    posts = db.query(models.Post).all()
# def get_posts(): 
#     cursor.execute("""SELECT * FROM posts """)
#     posts = cursor.fetchall()
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def createposts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(auth2.get_current_user)):
    new_post = models.Post(**post.dict()) #Equivalent to longer version of new_post
    #new_post = models.Post(title=post.title, content=post.content, published=post.published)
    print(current_user)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(auth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first() #Anytime your looking for one posts, remove .all(). Waste of processing power 
    # cursor.execute("SELECT * FROM posts WHERE id = %s", (str(id)))
    # post = cursor.fetchone()
    # conn.commit()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail= f'post with id: {id} was not found' )
        response.status_code = status.HTTP_404_NOT_FOUND
    return post

@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(auth2.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, 
        detail= f'post with id: {id} does not exists')
    post.delete(synchronize_session= False)
    db.commit()
    return Response(status_code = status.HTTP_204_NO_CONTENT)
 # def delete_post(id: int):  
#     cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id)))
#     deleted_post = cursor.fetchone()
#     print(deleted_post)
#     conn.commit()

@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db),current_user: int = Depends(auth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'post with id: {id} does not exists' )
    post_query.update(updated_post.dict(), synchronize_session=False) #You can hard code in attributes as well
    db.commit()
    return post_query.first()

