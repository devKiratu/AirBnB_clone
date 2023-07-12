#!/usr/bin/env python3
"""
Models City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Inherits from BaseModel
    """
    state_id = ""
    name = ""
