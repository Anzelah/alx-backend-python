#!/usr/bin/env python3
"""Import your modules"""

import unittest
from nose.tools import assert_equal


class TestAccessNestedMap(unittest.TestCase):
    """Class to test the nested map fuction
    """
    @parameterized.expand([
                ({"a": 1}, ["a"], 1),
                ({"a": {"b": 2}}, ["a"], 2),
                (({"a": {"b": 2}}, ["a", "b"])
            ])
    def test_access_nested_map(nested_map, path, result):
        """Method holding all the tests or the nested_map function
        """
        assert_equal((nested_map, path), result)
