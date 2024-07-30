#!/usr/bin/python3
"""
Unittest for State class
"""
import unittest
from datetime import datetime
from models.state import State
from models.base_model import BaseModel


class StateTestCase(unittest.TestCase):
    """ class for State test """

    def setUp(self):
        """Set up a State instance for each test."""
        self.state = State()  # Create a State object before each test

    def test_state_attributes(self):
        """Test the existence and types of State attributes."""
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))
        self.assertTrue(hasattr(self.state, "name"))

        """the type"""
        self.assertIsInstance(self.state.id, str)
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)
        self.assertIsInstance(self.state.name, str)
        self.assertEqual(self.state.name, "")


if __name__ == '__main__':
    unittest.main()
