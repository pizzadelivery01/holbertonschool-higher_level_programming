#!/usr/bin/python3
"""
tests for Base class
"""

import unittest
import inspect
import pep8
import json
import sys
import os
from io import StringIO
from models import base
Base = base.Base

class TestBaseStyle(unittest.TestCase):
    """ checks pep8 and docstrings """
    @classmethod
    def test_pep8_base(self):
        """ models/base.py pep8 compliant """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstrings(self):
        """ test for module docstrings """
        self.assertTrue(len(base.__doc__) >= 1)

    def test_class_docstring(self):
        """ test for class docstrings """
        self.assertTrue(len(Base.__doc__) >= 1)

class TestBase(unittest.TestCase):
    """ Test to check Base class """
    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            b = Base(1, 1)

    def test_noid(self):
        """ test no id """
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_set(self):
        """ test id after set """
        b1106 = Base(b1106.id, 1106)

    def test_noid_afterset(self):
        """ test id None after previously set """
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_nb(self):
        """test nb_objects as private """
        b = Base(3)
        with self.assertRaises(AttributeError):
            print b.nb_objects
        with self.assertRaises(AttributeError):
            print b.__nb_objects

    def test_to_json_string(self):
        """ tests to json string """
        Base.__Base__nb_objects = 0
        d1 = {"id": 9, "width": 1, "height": 2, "x": 3, "y": 4}
        d2 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 5}
        jsonstr = Base.to_json_string([d1, d2])
        self.assertTrue(type(jsonstr) is str)
        d = json.loads(jsonstr)
        self.assertEqual(d, [d1, d2])

def test_None_to_json_String(self):
    """test None"""
        jsonstr = Base.to_json_string(None)
        self.assertTrue(type(jsonstr) is str)
        self.assertEqual(jsonstr, "[]")

    def test_from_json_string(self):
        """Tests from_json_string"""
        json_str = '[{"id": 9, "width": 5, "height": 6, "x": 7, "y": 8},
        {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}]'
        json_l = Base.from_json_string(json_str)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertEqual(json_l[0],
                         {"id": 1, "width": 2, "height": 4, "x": 5, "y": 5})
        self.assertEqual(json_l[1],
                         {"id": 2, "width": 3, "height": 3, "x": 4, "y": 6})

    def test_fjs_empty(self):
        """Tests from_json_string with an empty string"""
        self.assertEqual([], Base.from_json_string(""))

    def test_fjs_None(self):
        """Tests from_json_string with an empty string"""
        self.assertEqual([], Base.from_json_string(None))

if __name__ == "__main__":
    unitest.main()
