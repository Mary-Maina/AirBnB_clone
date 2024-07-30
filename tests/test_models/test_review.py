#!/usr/bin/python3
""" unit test for Review """
import unittest
from models.review import Review
from datetime import datetime


class ReviewTestCase(unittest.TestCase):
    """ class for Review test """

    def setUp(self):
        """Set up a Review instance for each test."""
        self.review = Review()

    def test_review_attributes(self):
        """Test the existence and types of Review attributes."""
        self.assertTrue(hasattr(self.review, "id"))
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertTrue(hasattr(self.review, "updated_at"))
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
        
        """Test the type"""
        self.assertIsInstance(self.review.id, str)
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)


if __name__ == '__main__':
    unittest.main()
