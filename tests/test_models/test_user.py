#!/usr/bin/python3
"""
Unittest for User class
"""
import unittest
from models.user import User
from models.base_model import BaseModel
import os
import models


class TestUser(unittest.TestCase):
    """Tests the user"""
    def setup(self):
        """create a temporary fole for saving data"""
        self.test_file = "test_file.json"
        models.storage.__file_path = self.test_file
        models.storage.save()

    def tearDown(self):
        """removes the temporary test file"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_user_attribute(self):
        """creates a brand new user"""
        test_user = User()
        """checks user email"""
        self.assertEqual(test_user.email, "")
        """checks user password"""
        self.assertEqual(test_user.password, "")
        """checks first name"""
        self.assertEqual(test_user.first_name, "")
        """checks for last name"""
        self.assertEqual(test_user.last_name, "")

    def test_user_inherits_from_base_model(self):
        """creates user instance"""
        test_user = User()
        """checks if user is a subclass"""
        test_user.email = "mary@example.com"
        test_user.first_name = "Mary"
        test_user.last_name = "John"
        test_user.password = "Mary123"
        """string represantation of user instance"""
        user_str = str(test_user)
        self.assertIn("User", user_str)
        self.assertIn("mary@example.com", user_str)
        self.assertIn("Mary", user_str)
        self.assertIn("John", user_str)
        self.assertIn("Mary123", user_str)

    def test_user_to_dict(self):
        """creates a new user instance"""
        test_user = User()
        """checks if user is a subclass"""
        test_user.email = "mary@example.com"
        test_user.first_name = "Mary"
        test_user.last_name = "John"
        test_user.save()
        """give the dict representation"""
        user_dict = test_user.to_dict()
        self.assertEqual(user_dict['email'], "mary@example.com")
        self.assertEqual(user_dict['first_name'], "Mary")
        self.assertEqual(user_dict["last_name"], "John")

    def test_user_instance_creation(self):
        """creates new user with arguments"""
        test_user = User(
                email="mary@example.com", password="Mary123", first_name="Mary", last_name="John")
        self.assertEqual(test_user.email, "mary@example.com")
        self.assertEqual(test_user.password, "Mary123")
        self.assertEqual(test_user.first_name, "Mary")
        self.assertEqual(test_user.last_name, "John")

    def test_user_instance_to_dict(self):
        """creates a new user with attributes value"""
        test_user = User(
                email="mary@example.com", password="Mary123", first_name="Mary", last_name="John")
        user_dict = test_user.to_dict()
        self.assertEqual(user_dict['email'], "mary@example.com")
        self.assertEqual(user_dict['password'], "Mary123")
        self.assertEqual(user_dict['first_name'], "Mary")
        self.assertEqual(user_dict["last_name"], "John")

    def test_user_id_generation(self):
        """generates two instances"""
        test_user = User()
        user2 = User()
        self.assertNotEqual(test_user.id, user2.id)


if __name__ == '__main__':
    unittest.main()
