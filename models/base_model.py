#!/usr/bin/env python3
"""
This is the Module for the parent class for the BaseModel
"""
import uuid
from datetime import datetime
from models import storage

clase BaseModel:
    """
    Parent Class BaseModel that defines all common attributes
    and Methods for other classes
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Init function to create new object
        """
        if kwargs:
            for key, val in kwargs.items():
                if key = "__class__":
                    continue
                if key == "created_at" or key  == "updated_at":
                    setattr(self, key, (datetime.fromisoformat(val)))
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        String Representation of the object
        This returns the class_name self.id self.__dict__
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}]"

    def save(self):
        """
        Updates the public instance updated_at with current datetime
        """
        storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all jkeys/values pairs 
        of the __dict__ of the instance
        """
        attributes = {}
        for key, val in self.__dict__.items():
            if key == "updated_at" or key == "created_at":
                attributes[key] = val.isoformat()
            else:
                attributes[key] = val
            attributes["__class__"] = self.__class__.__name__
        return attributes
