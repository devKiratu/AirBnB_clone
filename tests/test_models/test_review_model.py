#!/usr/bin/env python3
"""
Test case for Review class
"""
import unittest
import os
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    Define test cases for class Review
    """

    def setUp(self):
        '''
        Set up for Review model tests
        '''
        self.test_review = Review()
        self.file_path = "file.json"

    def tearDown(self):
        '''
        Clean up after tests
        '''

        del self.test_review

        if os.path.isfile(self.file_path):
            os.remove(self.file_path)

    def test_review_model_inheritance(self):
        '''
        Test if Review model inherits from BaseModel
        '''

        r = self.test_review
        self.assertIsInstance(r, BaseModel)

    def test_review_attributes(self):
        '''
        Test existing attributes for review model
        '''

        r = self.test_review
        self.assertTrue('place_id' in r.__dir__())
        self.assertTrue('user_id' in r.__dir__())
        self.assertTrue('text' in r.__dir__())

    def test_review_attribute_types(self):
        '''
        Test review attribute types
        '''

        r = self.test_review
        place_id = getattr(r, 'place_id')
        user_id = getattr(r, 'user_id')
        text = getattr(r, 'text')

        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)

    def test_review_default_values(self):
        """
        Test for default attribute values
        """

        r1 = self.test_review
        self.assertEqual(r1.place_id, "")
        self.assertEqual(r1.user_id, "")
        self.assertEqual(r1.text, "")

    def test_new_review_values(self):
        """
        Test new review attribute values
        """

        r2 = self.test_review
        r2.state_id = "254"
        r2.user_id = "0100"
        r2.text = "Very nice"
        self.assertEqual(r2.state_id, "254")
        self.assertEqual(r2.user_id, "0100")
        self.assertEqual(r2.text, "Very nice")


if __name__ == "__main__":
    unittest.main()
