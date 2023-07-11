#!/usr/bin/python3
"""Defines test cases for module base_model.py"""


import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Defines tests for class BaseModel"""
    def test_ids(self):
        """checks if instance ids are unique"""
        m1 = BaseModel()
        m2 = BaseModel()
        self.assertNotEqual(m1.id, m2.id)

    def test_save(self):
        """checks if save method updates 'updated_at' attribute"""
        m1 = BaseModel()
        updated_at_1 = m1.updated_at
        m1.save()
        self.assertNotEqual(updated_at_1, m1.updated_at)

    def test_to_dict(self):
        """checks if 'to_dict' method successfully returns the
            required dictionary
        """
        m1 = BaseModel()
        m1.name = "My First Model"
        m1.my_number = 89
        new_dict = m1.to_dict()
        self.assertIsInstance(new_dict["updated_at"], str)
        self.assertIsInstance(new_dict["created_at"], str)
        self.assertIsInstance(new_dict["my_number"], int)
        self.assertIsInstance(new_dict["id"], str)
        self.assertEqual(new_dict["__class__"], "BaseModel")

    def test_creating_BaseModel_from_dict(self):
        """create BaseModel instance from a dictionary"""
        m1 = BaseModel()
        m1.name = "My_First_Model"
        m1.my_number = 89
        my_dict = m1.to_dict()
        m2 = BaseModel(**my_dict)
        self.assertEqual(m1.id, m2.id)
        self.assertEqual(m1.name, m2.name)
        self.assertEqual(m1.my_number, m2.my_number)
        self.assertFalse(m1 is m2)
        self.assertIsInstance(m1.created_at, datetime)
        self.assertIsInstance(m1.updated_at, datetime)
