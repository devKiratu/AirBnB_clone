#!/usr/bin/env python3
"""
Test case for State class
"""
import unittest
import os
from models.state import State
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Define test cases for class State
    """

    def setUp(self):
        '''
        Set up for state model tests
        '''

        self.test_state = State()
        self.file_path = "file.json"

    def tearDown(self):
        '''
        Clean up after tests
        '''

        del self.test_state

        if os.path.isfile(self.file_path):
            os.remove(self.file_path)

    def test_state_inheritance(self):
        '''
        Test state inherits from BaseModel
        '''

        self.assertIsInstance(self.test_state, BaseModel)

    def test_state_attributes(self):
        '''
        Test existing state attributes
        '''

        s = self.test_state
        self.assertTrue("name" in s.__dir__())

    def test_state_attribute_types(self):
        '''
        Test state attribute types
        '''

        name = getattr(self.test_state, 'name')
        self.assertIsInstance(name, str)

    def test_state_default_values(self):
        """
        Test for empty attribute values
        """

        s = self.test_state
        self.assertEqual(s.name, "")

    def test_new_state_attributes(self):
        """
        Test new state attribute values
        """

        s2 = self.test_state
        s2.name = "Kenya"
        self.assertEqual(s2.name, "Kenya")


if __name__ == "__main__":
    unittest.main()
