#!/usr/bin/python3

"""Defines unittests for models/base_model.py.


Unittest classes:
    TestBaseModel_instant
    TestBaseModel_save
    TestBaseModel_to_dict
    """

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instant(unittest.TestCase):
    """Unittests for testing instance of the BaseModel class."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_two_models_with_unique_ids(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)


if __name__ == "__main__":
    unittest.main()
