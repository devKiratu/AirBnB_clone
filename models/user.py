#!/usr/bin/env python3
"""
Models User class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Inherits from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
