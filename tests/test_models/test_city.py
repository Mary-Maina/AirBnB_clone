#!/usr/bin/python3
"""
Unittest for City class
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Tests for the City class"""
    def setUp(self):
        """Set up the city instance"""
        self.city = City()

    def test_inheritance(self):
        """Test that City inherits from BaseModel"""
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """Test that City has the correct attributes"""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertIsInstance(self.city.name, str)
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_has_attributes(self):
        """Test if City instance has the required attributes."""
        attributes = ["id", "created_at", "updated_at", "state_id", "name"]
        for attr in attributes:
            self.assertTrue(hasattr(self.city, attr))


if __name__ == '__main__':
    unittest.main()
