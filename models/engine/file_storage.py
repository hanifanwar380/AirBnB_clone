#!/usr/bin/python3
"""File Storage for the Base Model
    """

import json
from models.base_model import BaseModel


class FileStorage:
    """A storage engine for the base model

    Attributes:
        __file_path (str): The string - path to the JSON file.
        __objects (dict): A dictionary to store all objects created.

    """

    __file_path = "file.json"
    __objects = {}
    
    
    def all(self):
        """
        Returns:
            A dictionary object
        """
        return FileStorage.__objects

    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """

        object_class_name = obj.__class__.__name__
        
        FileStorage.__objects["{}.{}".format(object_class_name, obj.id)] = obj
    
    
    def save(self):
        pass
    
    def reload(self):
        pass