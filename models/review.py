#!/usr/bin/env python3
"""
Class Reviw inherits from the base model.
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    This is a class Review that inheritsq from the base model
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
