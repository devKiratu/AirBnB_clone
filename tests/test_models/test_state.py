#!/usr/bin/env python3
"""
Test case for State class
"""
import unittest
from models.state import State


class TestUser(unittest.TestCase):
    """
    Define test cases for class State
    """
    def test_default_attributes(self):
        """
        Test for empty attributes
        """
        s1 = State()
        self.assertEqual(s1.name, "")

    def test_new_state_attributes(self):
        """
        Test new state attributes
        """
        s2 = State()
        s2.name = "Kenya"
        self.assertEqual(s2.name, "Kenya")


if __name__ == "__main__":
    unittest.main()
