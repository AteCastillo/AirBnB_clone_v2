#!/usr/bin/python3
""" new subclass"""

from models.base_model import BaseModel


class User(BaseModel):
    """new subclass"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
