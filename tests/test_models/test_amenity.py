#!/usr/bin/env python3
"""
Test case for Amenity class
"""
import unittest
from models.amenity import Amenity


class TestUser(unittest.TestCase):
    """
    Define test cases for class Amenity
    """
    def test_default_attributes(self):
        """
        Test for empty attributes
        """
        a1 = Amenity()
        self.assertEqual(a1.name, "")

    def test_new_amenity_attributes(self):
        """
        Test new amenity attributes
        """
        a2 = Amenity()
        a2.name = "Swimming Pool"
        self.assertEqual(a2.name, "Swimming Pool")


if __name__ == "__main__":
    unittest.main()
