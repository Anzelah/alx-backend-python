#!/usr/bin/env python3
"""Import your modules"""

import requests
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json


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


class TestGetJson(unittest.TestCase):
    """Class to test the get json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, url, expected_result):
        """Test that the get_json() function returns expected results"""
        mock_get = patch('requests.get').start()

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = expected_result
        mock_get.return_value = mock_response

        result = get_json(url)
        self.assertEqual(result, expected_result)
        mock_get.assert_called_once_with(url)


if __name__ == '__main__':
    unittest.main()
