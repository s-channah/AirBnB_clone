#!/user/bin/env python3
"""
This is the module that inherits from the BaseModel
"""
from models.base_model import BaseModel

class State(BaseModel):
    """
    This is the class state
    """
    name = ""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
