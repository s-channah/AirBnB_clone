#!/usr/bin/env python3
"""
The Class Place that inherits from the BaseModel
"""
from models.base_model import BaseModel

class Place(BaseModel):
    """
    This is the class Place that inherits from the basemodel
    """
    city_id =""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    class_id = ""
    amenity_ids = []
    """
    Initialise amenity ids as a list
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
