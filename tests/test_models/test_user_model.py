#!/usr/bin/env python3
"""
Test case for user class
"""
import unittest
import os
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Define test for class User
    """

    def setUp(self):
        '''
        Setup for user model tests

        '''
        self.test_user = User()
        self.file_path = "file.json"

    def tearDown(self):
        '''
        Clean up after user model tests
        '''

        del self.test_user

        if os.path.isfile(self.file_path):
            os.remove(self.file_path)

    def test_user_inheritance(self):
        '''
        Test that user inherits from BaseModel
        '''

        self.assertIsInstance(self.test_user, BaseModel)

    def test_user_attributes(self):
        '''
        Test for existing user attributes
        '''

        u = self.test_user
        self.assertTrue("email" in u.__dir__())
        self.assertTrue("password" in u.__dir__())
        self.assertTrue("first_name" in u.__dir__())
        self.assertTrue("last_name" in u.__dir__())

    def test_user_attribute_types(self):
        '''
        Test user attribute types
        '''

        u = self.test_user
        email = getattr(u, 'email')
        self.assertIsInstance(email, str)
        passwd = getattr(u, 'password')
        self.assertIsInstance(passwd, str)
        fname = getattr(u, 'first_name')
        self.assertIsInstance(fname, str)
        lname = getattr(u, 'last_name')
        self.assertIsInstance(lname, str)

    def test_user_default_value(self):
        """
        Test for empty user attributes values
        """

        u = self.test_user
        self.assertEqual(u.email, "")
        self.assertEqual(u.password, "")
        self.assertEqual(u.first_name, "")
        self.assertEqual(u.last_name, "")

    def test_new_user_attributes(self):
        """
        Test new user attributes
        """
        u1 = self.test_user
        u1.first_name = "Monty"
        u1.last_name = "Python"
        u1.email = "monty.python@email.com"
        u1.password = "passwd"
        self.assertEqual(u1.email, "monty.python@email.com")
        self.assertEqual(u1.password, "passwd")
        self.assertEqual(u1.first_name, "Monty")
        self.assertEqual(u1.last_name, "Python")


if __name__ == "__main__":
    unittest.main()
