#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models
from models.state import State


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
<<<<<<< HEAD
    places = relationship('Place', cascade='all, delete', backref='cities')
=======
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", backref='cities', cascade='all, delete, delete-orphan')
>>>>>>> 51d937ac3739ff8e0036437a77c3c1c646846a48
