#!/usr/bin/python3
"""
class BaseModel is a superclass that defines all common
attributes/methods for other classes and all future classes
inherit from it
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """This is the superclass other classes will inherit from"""
    def __init__(self, *args, **kwargs):
        timef = "%Y-%m-%dT%H:%M:%S.%f"

        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            "if there is a keyword present"
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, timef))
                else:
                    setattr(self, key, value)

        models.storage.new(self)

    def __str__(self):
        """returns the string representation of an instance"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """saves to current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """used for serialziation"""
        inst_dict = self.__dict__.copy()
        inst_dict['__class__'] = self.__class__.__name__
        inst_dict['created_at'] = self.created_at.isoformat()
        inst_dict['updated_at'] = self.updated_at.isoformat()

        return inst_dict
