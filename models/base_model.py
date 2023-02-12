#!/usr/bin/python3
"""A BaseModel module"""
import uuid
from datetime import datetime


class BaseModel:
    """A BaseModel class"""
    def __init__(self):
        """Initializing the class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Print the representation of the BaseModel class"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) self.__dict__"

    def save(self):
        """Update the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """return a dictionary containing all keys/values of instance"""
        my_dict = self.__dict__
        my_dict["__class__"] = self.__class__name
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
