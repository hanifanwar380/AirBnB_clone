#!/usr/bin/python3
"""Unittest module for the State Class."""

import unittest
from models.state import State
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    """Test Cases for the State class."""

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
        """Tests instantiation of State class."""

        test_object = State()
        self.assertEqual(str(type(test_object)),
                         "<class 'models.state.State'>")
        self.assertIsInstance(test_object, State)
        self.assertTrue(issubclass(type(test_object), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of State class."""
        attributes = storage.attributes()["State"]
        test_object = State()
        for key, value in attributes.items():
            self.assertTrue(hasattr(test_object, key))
            self.assertEqual(type(getattr(test_object, key, None)), value)


if __name__ == "__main__":
    unittest.main()
