#!/usr/bin/env python3
"""
Class City that inherits from the basemodel
"""
from  models.base_model import BaseModel

class City(BaseModel):
    """
    The Class City tha  t inherts from the BaseModel
    """
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
