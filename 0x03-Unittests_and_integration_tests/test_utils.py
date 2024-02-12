#!/usr/bin/env python3
"""Import your modules"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Class to test the nested map fuction
    """
    @parameterized.expand([
                ({"a": 1}, ["a"], 1),
                ({"a": {"b": 2}}, ["a"], {"b": 2}),
                ({"a": {"b": 2}}, ["a", "b"], 2)
            ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Method holding all the tests or the nested_map function
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)
    
    @parameterized.expand([
        ({}, ["a"]),
        ({"a": 1}, ["a", "b"])
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that a key error is raised for inputs"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


if __name__ == '__main__':
    unittest.main()
