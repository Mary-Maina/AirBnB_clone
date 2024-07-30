#!/usr/bin/python3
"""This is a file storage module"""
import json
from models.base_model import BaseModel
import os
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """class where the serilization will happen"""
    __file_path = 'file.json'
    __objects = {}

    def new(self, obj):
        """sets obj with key to __objects"""
        obj_name = obj.__class__.__name__
        key = "{}.{}".format(obj_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """returns file storage"""
        return FileStorage.__objects

    def save(self):
        """Serializes __objects to the JSON file (__file_path)"""
        all_obj = FileStorage.__objects
        obj_dict = {}

        for obj in all_obj.keys():
            obj_dict[obj] = all_obj[obj].to_dict()

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                try:
                    obj_dict = json.load(f)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')

                        cls = eval(class_name)
                        instance = cls(**value)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
