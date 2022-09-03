#!/usr/bin/python3
"""Unittest module for the Place Class."""

import unittest

from models.place import Place
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    """Test Cases for the Place class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of Place class."""

        test_object = Place()
        self.assertEqual(str(type(test_object)),
                         "<class 'models.place.Place'>")
        self.assertIsInstance(test_object, Place)
        self.assertTrue(issubclass(type(test_object), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of Place class."""
        attributes = storage.attributes()["Place"]
        test_object = Place()
        for k, v in attributes.items():
            self.assertTrue(hasattr(test_object, k))
            self.assertEqual(type(getattr(test_object, k, None)), v)


if __name__ == "__main__":
    unittest.main()\
