#!/usr/bin/python3
"""Testing base_model file"""
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """A class to test the BaseModel class"""
    def test_init_BaseModel(self):
        """test if an object belongs to the BaseModel class"""
        my_object = BaseModel()
        self.assertIsInstance(my_object, BaseModel)

    def test_save(self):
        """test if=date updates when saved"""
        my_object = BaseModel()
        first_updated = my_object.updated_at()
        my_object.save()
        second_
        
