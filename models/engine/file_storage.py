#!/usr/bin/python3
"""Contains class that enables data persistence via file storage"""
import json


class FileStorage:
    """Handles serialization and deserialization of objects to and from file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
            Args:
                obj: the object to store
        """
        new_obj = obj.to_dict()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = new_obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """deserializes the JSON file to __objects
            (only if the JSON file (__file_path) exists
        """
        try:
            with open(self.__file_path, "r") as f:
                objs = json.load(f)
                if objs:
                    self.__objects = objs
        except Exception:
            pass
