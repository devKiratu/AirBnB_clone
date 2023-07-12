#!/usr/bin/env python3
"""
Test case for City class
"""
import unittest
from models.city import City


class TestUser(unittest.TestCase):
    """
    Define test cases for class City
    """
    def test_default_attributes(self):
        """
        Test for empty attributes
        """
        c1 = City()
        self.assertEqual(c1.state_id, "")
        self.assertEqual(c1.name, "")

    def test_new_city_attributes(self):
        """
        Test new city attributes
        """
        c2 = City()
        c2.state_id = "047"
        c2.name = "Nairobi"
        self.assertEqual(c2.state_id, "047")
        self.assertEqual(c2.name, "Nairobi")


if __name__ == "__main__":
    unittest.main()
