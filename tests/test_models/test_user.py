#!/usr/bin/env python3
"""
Test case for user class
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Define test for class User
    """
    def test_default_attributes(self):
        """
        Test for empty user attributes
        """
        new_user = User()
        self.assertEqual(new_user.email, "")
        self.assertEqual(new_user.password, "")
        self.assertEqual(new_user.first_name, "")
        self.assertEqual(new_user.last_name, "")

    def test_new_user_attributes(self):
        """
        Test new user attributes
        """
        u1 = User()
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
