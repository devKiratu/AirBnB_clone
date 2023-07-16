#!/usr/bin/env python3
"""
Test case for Place class
"""
import unittest
from models.place import Place


class TestUser(unittest.TestCase):
    """
    Define test cases for class Place
    """
    def test_default_attributes(self):
        """
        Test for empty attributes
        """
        p1 = Place()
        self.assertEqual(p1.city_id, "")
        self.assertEqual(p1.user_id, "")
        self.assertEqual(p1.name, "")
        self.assertEqual(p1.description, "")
        self.assertEqual(p1.number_rooms, 0)
        self.assertEqual(p1.number_bathrooms, 0)
        self.assertEqual(p1.max_guest, 0)
        self.assertEqual(p1.price_by_night, 0)
        self.assertEqual(p1.latitude, 0.0)
        self.assertEqual(p1.longitude, 0.0)
        self.assertEqual(p1.amenity_ids, [])

    def test_new_place_attributes(self):
        """
        Test new place attributes
        """
        p2 = Place()
        p2.city_id = "047"
        p2.user_id = "0100"
        p2.name = "Grand Villa"
        p2.description = "A place to be"
        p2.number_rooms = 5
        p2.number_bathrooms = 6
        p2.max_guest = 25
        p2.price_by_night = 25000
        p2.latitude = 100025498.35687
        p2.longitude = 1025498.3568702
        p2.amenity_ids = [23, 25, 78]
        self.assertEqual(p2.city_id, "047")
        self.assertEqual(p2.user_id, "0100")
        self.assertEqual(p2.name, "Grand Villa")
        self.assertEqual(p2.description, "A place to be")
        self.assertEqual(p2.number_rooms, 5)
        self.assertEqual(p2.number_bathrooms, 6)
        self.assertEqual(p2.max_guest, 25)
        self.assertEqual(p2.price_by_night, 25000)
        self.assertEqual(p2.latitude, 100025498.35687)
        self.assertEqual(p2.longitude, 1025498.3568702)
        self.assertEqual(p2.amenity_ids, [23, 25, 78])


if __name__ == "__main__":
    unittest.main()
