#!/usr/bin/env python3
"""
Test case for Place class
"""
import unittest
import os
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    Define test cases for class Place
    """

    def setUp(self):
        '''
        Set up for Place model tests
        '''

        self.test_place = Place()
        self.file_path = "file.json"

    def tearDown(self):
        '''
        Clean up after tests
        '''

        del self.test_place

        if os.path.isfile(self.file_path):
            os.remove(self.file_path)

    def test_place_inheritance(self):
        '''
        Test Place inherits from BaseModel
        '''

        p = self.test_place
        self.assertIsInstance(p, BaseModel)

    def test_place_attributes(self):
        '''
        Test existing atributes for place model
        '''

        p = self.test_place
        self.assertTrue('city_id' in p.__dir__())
        self.assertTrue('user_id' in p.__dir__())
        self.assertTrue('name' in p.__dir__())
        self.assertTrue('description' in p.__dir__())
        self.assertTrue('number_rooms' in p.__dir__())
        self.assertTrue('number_bathrooms' in p.__dir__())
        self.assertTrue('max_guest' in p.__dir__())
        self.assertTrue('price_by_night' in p.__dir__())
        self.assertTrue('latitude' in p.__dir__())
        self.assertTrue('longitude' in p.__dir__())
        self.assertTrue('amenity_ids' in p.__dir__())

    def test_place_attribute_types(self):
        '''
        Test place sttribute types
        '''

        p = self.test_place
        city_id = getattr(p, 'city_id')
        user_id = getattr(p, 'user_id')
        name = getattr(p, 'name')
        description = getattr(p, 'description')
        number_rooms = getattr(p, 'number_rooms')
        number_bathrooms = getattr(p, 'number_bathrooms')
        max_guest = getattr(p, 'max_guest')
        price_by_night = getattr(p, 'price_by_night')
        latitude = getattr(p, 'latitude')
        longitude = getattr(p, 'longitude')
        amenity_ids = getattr(p, 'amenity_ids')

        self.assertIsInstance(city_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(name, str)
        self.assertIsInstance(description, str)
        self.assertIsInstance(number_rooms, int)
        self.assertIsInstance(number_bathrooms, int)
        self.assertIsInstance(max_guest, int)
        self.assertIsInstance(price_by_night, int)
        self.assertIsInstance(latitude, float)
        self.assertIsInstance(longitude, float)
        self.assertIsInstance(amenity_ids, list)

    def test_place_default_values(self):
        """
        Test for empty attribute values
        """

        p1 = self.test_place
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

    def test_new_place_values(self):
        """
        Test new place attribute values
        """

        p2 = self.test_place
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
