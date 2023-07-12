#!/usr/bin/env python3
"""
Test case for Review class
"""
import unittest
from models.review import Review


class TestUser(unittest.TestCase):
    """
    Define test cases for class Review
    """
    def test_default_attributes(self):
        """
        Test for empty attributes
        """
        r1 = Review()
        self.assertEqual(r1.place_id, "")
        self.assertEqual(r1.user_id, "")
        self.assertEqual(r1.text, "")

    def test_new_review_attributes(self):
        """
        Test new review attributes
        """
        r2 = Review()
        r2.state_id = "254"
        r2.user_id = "0100"
        r2.text = "Very nice"
        self.assertEqual(r2.state_id, "254")
        self.assertEqual(r2.user_id, "0100")
        self.assertEqual(r2.text, "Very nice")


if __name__ == "__main__":
    unittest.main()
