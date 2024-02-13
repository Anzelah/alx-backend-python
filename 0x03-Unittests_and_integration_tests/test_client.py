#!/usr/bin/env python3
"""Import your modules"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @patch('client.get_json')
    def test_public_repos(self, mock_json):
        """Unit testing for the public_repos function
        """
        payload = [{'name': 'Youtube'}, {'name': 'iTv'}]
        mock_json.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock:
            mock.return_value = 'value'
            results = GithubOrgClient('name').public_repos()

            self.assertEqual(results, ['Youtube', 'iTv'])

            mock_json.assert_called_once()
            mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo, license_key, expected_res):
        """Unit test the has_licence function in GithubOrgClient class
        """
        results = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(results, expected_res)



@parameterized_class(['org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'],
        TEST_PAYLOAD
        )
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Implement an integration test
    """
    @classmethod
    def setUpClass(cls):
        """Called before tests in an individual class are run
        """
        cls.get_patcher = patch('requests.get', side_effect=[
            cls.org_payload, cls.repos_payload])
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Called after tests in an individual class have run
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Testing public_repos() in an integration test
        """
        results = GithubOrgClient('example.com/org').public_repos()
        self.assertEqual(results, self.expected_repos)
        
    def test_public_repos_plus_license(self):
        """Test the public_repos() with license"""
        results = GithubOrgClient('example.com/org').public_repos(license='apache2')
        self.assertEqual(results, self.apache2_repos)
