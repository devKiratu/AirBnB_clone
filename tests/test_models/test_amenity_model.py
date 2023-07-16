#!/usr/bin/env python3
"""
Test case for Amenity class
"""
import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Define test cases for class Amenity
    """

    def setUp(self):
        '''
        Set up for amenity model tests
        '''

        self.test_amenity = Amenity()
        self.file_path = "file.json"

    def tearDown(self):
        '''
        Clean up after tests
        '''

        del self.test_amenity

        if os.path.isfile(self.file_path):
            os.remove(self.file_path)

    def test_city_inheritance(self):
        '''
        Test Amenity inherits from BaseModel
        '''

        a = self.test_amenity
        self.assertIsInstance(a, BaseModel)

    def test_amenity_attributes(self):
        '''
        Test existing amenity attributes
        '''

        a = self.test_amenity
        self.assertTrue("name" in a.__dir__())

    def test_amenity_attribute_types(self):
        '''
        Test amenity attribute types
        '''

        a = self.test_amenity
        name = getattr(a, 'name')
        self.assertIsInstance(name, str)

    def test_amenity_default_values(self):
        """
        Test for default attribute values
        """

        a1 = self.test_amenity
        self.assertEqual(a1.name, "")

    def test_new_amenity_values(self):
        """
        Test new amenity attribute values
        """

        a2 = self.test_amenity
        a2.name = "Swimming Pool"
        self.assertEqual(a2.name, "Swimming Pool")


if __name__ == "__main__":
    unittest.main()
