#!/usr/bin/env python3
"""Import your modules"""

import unittest
import utils


class TestAccessNestedMap(unittest.TestCase):
    """Class to test the nested map fuction
    """
    @parameterized.expand('nested_map', 'path', 'result',
            [
                ({"a": 1}, ["a"], 1),
                ({"a": {"b": 2}}, ["a"], 2),
                (({"a": {"b": 2}}, ["a", "b"])
            ])
    def TestAccessNestedMap.test_access_nested_map(nested_map, path, result):
        """Method holding all the tests or the nested_map function
        """
        assert utils.access_nested_map(nested_map, path) == result
