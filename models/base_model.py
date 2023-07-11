#!/usr/bin/python3
"""Defines the BaseModel class"""


import uuid
from datetime import datetime


class BaseModel:
    """defines all common attributes and methods to be reused by other classes
    """
    def __init__(self, *args, **kwargs):
        """initializes a BaseModel instance"""
        if kwargs:
            for key in kwargs.keys():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(kwargs[key]))
                else:
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """returns user readable string representation in the form
            '[<class name>] (<self.id>) <self.__dict__>'
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
            )

    def save(self):
        """updates the public instance attribute updated_at with the current
            datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
            of the instance, and adds '__class__' key with value name of class
        """
        new_dict = {}
        new_dict["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if type(v) is datetime:
                new_dict[k] = v.isoformat()
            else:
                new_dict[k] = v
        return new_dict
