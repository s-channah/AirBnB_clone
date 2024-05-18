#!/usr/bin/env python3
"""
This is the Class Module for user that inherits from BaseModel
"""
from model.base_model import BaseModel

class User(BaseModel):
    """
    This is a User class that defines all the
    Attributes of the User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
