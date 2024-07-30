#!/usr/bin/python3
"""
The model for the user class
"""
from model.base_model import BaseModel


class User(BaseModel):
    """Deals with the user's information"""
    email = ""
    password = ""
    first_time = ""
    last_time = ""
