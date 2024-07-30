#!/usr/bin/python3


import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests the basemodel"""

    def test_init(self):
        """ensures all attributes have values"""
        the_model = BaseModel()
        self.assertIsInstance(the_model, BaseModel)
        self.assertIsNotNone(the_model.id)
        self.assertIsInstance(the_model.created_at, datetime)
        self.assertIsInstance(the_model.updated_at, datetime)

    def test_save(self):
        """ensures the attribute is saved once updated"""
        the_model = BaseModel()
        start_updated_at = the_model.updated_at
        the_model.save()
        self.assertNotEqual(start_updated_at, the_model.updated_at)

    def test_to_dict(self):
        """ensures that serialization happens"""
        bm = BaseModel()
        obj_dict = bm.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], bm.id)
        self.assertEqual(obj_dict['created_at'], bm.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], bm.updated_at.isoformat())

    def test_str(self):
        """tests the representation of the string in basemodel"""
        bm = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(bm.id, bm.__dict__)
        self.assertEqual(str(bm), expected_str)


if __name__ == '__main__':
    unittest.main()
