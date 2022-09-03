#!/usr/bin/python3
"""Defines unittests for console.py.
    Unittest classes:

"""

from console import HBNBCommand
from models.engine.file_storage import FileStorage
import unittest
import datetime
from unittest.mock import patch
import sys
from io import StringIO
import re
import os
