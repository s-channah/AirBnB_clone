#!/usr/bin/env python3
"""
This is the File Storage Modelui for the Class Files
Storage which serialises the instances into a JSON file and deserialises
afterxwards into instances
"""
import json
import os.path

class FileStorage:
    """
    File Storage Class
    serialises into JASOn and back into instances
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self) -> None:
        """
        This initialises the  class filestorage
        """
        pass

    def all(self):
        """
        Returns a dictionary of __objects
        class.id as key and obj as value/class
        """
        return fileStorage.__objects

    def save(self):
        """
        This method adds a new object to the storage
        """
        dict_ = {k: v.to_dict() for k, v in FileStorage.__object.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as json_file:
            json.dump(dict_, json_file)

    def new(self, obj):
        """
        Adds in __objects the obj with key 
        <obj class name>.id
        """
        class_name = obj.__class__.__name__
        FileStorage.__objects[class_name + "." + obj.id] = obj

    def classes(self):
        """
        This is the method that returns a dictionary of all
        Valid Classes
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.review import Review
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        
        my_classes = {"BaseModel": BaseModel,
                      "User": User,
                      "State": State,
                      "Review": Review,
                      "Place": Place,
                      "City": City,
                      "Amenity": Amenity
                      }
        return my_classes

    def reload(self):
        """
        Deserialises existing JSON files
        Returns ll objs saved in file
        """
        try:
            with open(FileStorage.__file_path, "r") as file:
                dict_ = json.load(file)
                for k, v in dict__.items():
                    FileStorage.__objects[k] = my_classes[v["__class__"]](**v)
        except Exception:
            pass

    def destroy(self, key):
        if key in FileStorage.__objects:
            del (FileStorage.__objects[key])
        with open(FileStorage.__file_path, "w") as file:
            json.dump(FileStorage.__objects, file)
                    
