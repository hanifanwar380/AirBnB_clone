#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    """Test Cases for the Amenity class."""

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
        """Tests instantiation of Amenity class."""

        test_object = Amenity()
        self.assertEqual(str(type(test_object)),
                         "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(test_object, Amenity)
        self.assertTrue(issubclass(type(test_object), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of Amenity class."""
        attributes = storage.attributes()["Amenity"]
        test_object = Amenity()
        for key, value in attributes.items():
            self.assertTrue(hasattr(test_object, key))
            self.assertEqual(type(getattr(test_object, key, None)), value)


if __name__ == "__main__":
    unittest.main()
