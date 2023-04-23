from email.policy import default
from tkinter import CASCADE
from database import Base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import psycopg2
from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text 
from sqlalchemy.sql.sqltypes import TIMESTAMP

class Post(Base):
    __tablename__="posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable = False)
    published = Column(Boolean, server_default= "True", nullable="False")
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')) 
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)


class User(Base):
    __tablename__ = "users"
    id =  Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()')) 
