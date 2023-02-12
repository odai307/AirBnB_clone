#!/usr/bin/python3
"""A module to test the base_model class"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test for class BaseModel"""
    def test_init_model(self):
        """check if an instance created belongs to the BaseModel class"""
        my_object = BaseModel()
        self.assertIsInstance(my_object, BaseModel)

    def test_unique_id(self):
        """Tests to verify if each object of the BaseModel class have a unique id"""
        object_1 = BaseModel()
        object_2 = BaseModel()
        self.assertNotEqual(object_1.id, object_2.id)
    
    def test_save(self):
        item = BaseModel()
        first_save = item.updated_at
        item.save()
        second_save = item.updated_at
        self.assertNotEqual(first_save, second_save)

    def test_str(self):
        obj1 = BaseModel()
        dictionary = obj1.__dict__
        self.assertEqual(str(obj1), f"[BaseModel] ({obj1.id}) {dictionary}")

