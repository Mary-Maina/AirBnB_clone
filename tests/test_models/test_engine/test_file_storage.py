import unittest
import os
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageInstatiation(unittest.TestCase):
    """Test the instatiation of the filestorage"""
    def test_FileStorage_instatiation_no_args(self):
        """checks when there is no arguments"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instatiation_with_args(self):
        """checks if there is an argument"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initialization(self):
        """checks for initialization storage"""
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage(unittest.TestCase):
    """Tests for FileStorage Class"""
    def setUp(self):
        """Set up test environment"""
        self.test_file = "test_file.json"
        FileStorage._FileStorage__file_path = self.test_file
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up test environment"""
        if os.path.isfile(self.test_file):
            os.remove(self.test_file)

    def test_storage_returns_dict(self):
        """checks if all methods return dict"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        """Tests new method by creating and storing new objects"""
        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        models.storage.new(obj)
        self.assertIn("BaseModel.{}".format(obj.id), models.storage.all())

    def test_new_with_args(self):
        """creates new with args to show if there is typeerror"""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        """with None raise an Attribute error"""
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_and_reload(self):
        """Test that it saves and reloads properly to the JSON file"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        models.storage.new(obj1)
        models.storage.new(obj2)
        models.storage.save()

        n_s = FileStorage()
        n_s.reload()

        obj1_key = "BaseModel.{}".format(obj1.id)
        obj2_key = "BaseModel.{}".format(obj2.id)
        """checks if relaoded object matches the obj"""
        self.assertTrue(n_s.all().get(obj1_key) is not None)
        self.assertTrue(n_s.all().get(obj2_key) is not None)

    def test_to_save_file(self):
        """check if file was created"""
        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        self.assertTrue(os.path.exists(self.test_file))

    def test_reload_empty_file(self):
        """checks if it reloads empty file"""
        with self.assertRaises(TypeError):
            models.storage()
            models.storage.reload()


if __name__ == '__main__':
    unittest.main()
