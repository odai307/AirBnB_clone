#!/usr/bin/python3
"""A BaseModel File"""

import uuid
"""Imports the uuid module"""

from datetime import datetime
"""Import the datetime module"""


class BaseModel:
    """A BaseModel Class"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Prints the name of the class"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all key/values of __dict__"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict


