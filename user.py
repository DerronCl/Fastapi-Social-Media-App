from fastapi import APIRouter, FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from database import SessionLocal, engine, get_db
from sqlalchemy.orm import Session
import models, schemas, utils
from sqlalchemy.sql.functions import mode 
from typing import Optional, List

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    #hash password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail= f'USer with id: {id} does not exist' )
    return user 
