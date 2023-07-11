#!usr/bin/env python3
"""
Test cases for module file_storage
"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Define tests for class FileStorage
    """
    def setUp(self):
        """
        Set up for tests
        """
        self.file_path = "file.json"
        self.storage = FileStorage()

    def tearDown(self):
        """
        Clean up after tests
        """
        if os.path.isfile(self.file_path):
            os.remove(self.file_path)

    def test_all_returns_dict(self):
        """
        Test for all objects
        """
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_save_new_obj(self):
        """
        Test case: adding new instance
        """
        new_model = BaseModel()
        new_model.name = "New_Model"
        new_model.my_number = 89
        self.storage.new(new_model)
        all_objs = self.storage.all()
        key = f"BaseModel.{new_model.id}"
        self.assertIn(key, all_objs)
        self.assertEqual(all_objs[key], new_model.to_dict())

    def test_create_json_file_on_save(self):
        """
        Test case: save() create JSON file
        """
        self.storage.save()
        self.assertTrue(os.path.isfile(self.file_path))

    def test_reload_loads_object_from_file(self):
        """
        Test case: object reloaded from file
        """
        model_1 = BaseModel()
        model_2 = BaseModel()

        self.storage.new(model_1)
        self.storage.new(model_2)
        self.storage.save()

        FileStorage__objects = {}

        self.storage.reload()

        key1 = model_1.__class__.__name__ + '.' + model_1.id
        key2 = model_2.__class__.__name__ + '.' + model_2.id

        self.assertIn(key1, self.storage.all())
        self.assertIn(key2, self.storage.all())


if __name__ == "__main__":
    unittest.main()
