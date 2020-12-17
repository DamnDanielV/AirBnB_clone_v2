#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """ Model State """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ returns the city """
            from models import storage
            li_ci = storage.all('City')
            return [v for k, v in li_ci.items() if v.state_id == self.id]
