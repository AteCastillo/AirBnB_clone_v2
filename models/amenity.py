#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    '''Amenities Class'''
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary="place_amenity")
