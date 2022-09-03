#!/usr/bin/python3
"""Unittest module for City Class."""

import unittest

from models.city import City

from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    """Test Cases for the City class."""

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
        """Tests instantiation of City class."""

        test_object = City()
        self.assertEqual(str(type(test_object)), "<class 'models.city.City'>")
        self.assertIsInstance(test_object, City)
        self.assertTrue(issubclass(type(test_object), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of City class."""
        attributes = storage.attributes()["City"]
        test_object = City()
        for key, value in attributes.items():
            self.assertTrue(hasattr(test_object, key))
            self.assertEqual(type(getattr(test_object, key, None)), value)

if __name__ == "__main__":
    unittest.main()
