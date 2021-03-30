#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from os import getenv
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == "db":
        # Puede empezar aca
        cities = relationship("City", backref="state", cascade="all,delete")
    else:
        @property
        def cities(self):
            cities = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    cities.append(city)
            return cities
