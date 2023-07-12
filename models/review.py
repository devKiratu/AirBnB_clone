#!/usr/bin/env python3
"""
Models Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
