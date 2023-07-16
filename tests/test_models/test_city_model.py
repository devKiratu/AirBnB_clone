#!/usr/bin/env python3
"""
Test case for City class
"""
import unittest
import os
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    Define test cases for class City
    """

    def setUp(self):
        '''
        Set up for city model tests
        '''

        self.test_city = City()
        self.file_path = "file.json"

    def tearDown(self):
        '''
        Clean up after tests
        '''

        del self.test_city

        if os.path.isfile(self.file_path):
            os.remove(self.file_path)

    def test_city_inheritance(self):
        '''
        Test City inherits from BaseModel
        '''

        self.assertIsInstance(self.test_city, BaseModel)

    def test_city_attributes(self):
        '''
        Test existing city attributes
        '''

        c = self.test_city
        self.assertTrue("state_id" in c.__dir__())
        self.assertTrue("name" in c.__dir__())

    def test_city_attribute_types(self):
        '''
        Test city attribute types
        '''

        state_id = getattr(self.test_city, 'state_id')
        name = getattr(self.test_city, 'name')

        self.assertIsInstance(state_id, str)
        self.assertIsInstance(name, str)

    def test_state_default_values(self):
        """
        Test for empty attributes value
        """

        c1 = self.test_city
        self.assertEqual(c1.state_id, "")
        self.assertEqual(c1.name, "")

    def test_new_city_attributes(self):
        """
        Test new city attributes
        """

        c2 = self.test_city
        c2.state_id = "047"
        c2.name = "Nairobi"
        self.assertEqual(c2.state_id, "047")
        self.assertEqual(c2.name, "Nairobi")


if __name__ == "__main__":
    unittest.main()
