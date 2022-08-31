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
        """Serialize __objects to the JSON file __file_path."""

        o_dict = FileStorage.__objects
        obj_dict = {obj: o_dict[obj].to_dict() for obj in o_dict.keys()}

        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""

        try:
            with open(FileStorage.__file_path) as file:
                object_dict = json.load(file)
                for obj in object_dict.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
