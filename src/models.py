import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User (Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    email = Column(String(250))
    password = Column(String(10))
    favorites = relationship("favorites")

class Favorites (Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key = True)
    planet_name = Column(String(100))
    person_name = Column(String(100))
    user_id = Column(Integer, ForeignKey("users.id"))
    planet_id = Column(Integer, ForeignKey("planets.id"))
    person_id = Column(Integer, ForeignKey("people.id"))

class People (Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    homeland = Column(String(100))
    favorites = relationship("favorites")

class Planet (Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    population = Column(Integer(100))
    favorites = relationship("favorites")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')