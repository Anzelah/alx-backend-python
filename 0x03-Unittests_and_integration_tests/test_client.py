#!/usr/bin/env python3
"""Import your modules"""

import unittest
from unittest.mock import patch, PropertyMock
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
    def test_org(self, name, mock_getjson):
        """Test that the org function returns the correct value
        """
        instance = GithubOrgClient(name)
        instance.org()
        org_client = "https://api.github.com/orgs/{}".format(name)
        mock_getjson.assert_called_once_with(org_client)

    @parameterized.expand([
        ("some_url", {"repos_url": "https://urls.com"})
        ])
    def test_public_repos_url(self, name, expected_result):
        """Test the public repos url function of the githhuborgclient class
        """
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=expected_result)):
            result = GithubOrgClient(name)._public_repos_url
            self.assertEqual(result, expected_result["repos_url"])
