#!/usr/bin/env python3
"""
This is the amenity modele handling the amenity class that inherits from the basemodel
"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    This is the amenity cklass that inherits from the BaseModel
    """
    name = ""
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
