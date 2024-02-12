#!/usr/bin/env python3
"""Import your modules"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Function to test the github org class
    """
    @parameterized.expand([
        ("google"),
        ("abc")
        ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_getjson):
        """Test that the org function returns the correct value
        """
        instance = GithubOrgClient(org_name)
        instance.org()
        org_client = "https://api.github.com/orgs/{}".format(org_name)
        mock_getjson.assert_called_once_with(org_client)
