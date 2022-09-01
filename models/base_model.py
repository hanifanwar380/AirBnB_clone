#!/usr/bin/python3
"""Defining the base model for the package
    """

from datetime import datetime

from uuid import uuid4
import models


class BaseModel:
    """The Base Model for the AirBnB project
    """

    def __init__(self, *args, **kwargs):
        """Initialize a new Base model

        Args:
            *args: Not used.
            **kwargs: Key Value pair of attributes.

        """

        time_format = "%Y-%m-%dT%H:%M:%S.%f"

        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """To update update_at with the current date time
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair of __class__ representing
        the class name of the object
        """

        mod_dict = self.__dict__.copy()
        mod_dict["created_at"] = self.created_at.isoformat()
        mod_dict["updated_at"] = self.created_at.isoformat()
        mod_dict["__class__"] = self.__class__.__name__

        return mod_dict

    def __str__(self):
        """Return the modified representation of this Base Model"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".\
            format(class_name, self.id, self.__dict__)
