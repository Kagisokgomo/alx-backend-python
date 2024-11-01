#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json
from unittest.mock import patch, Mock
from utils import memoize
from unittest.mock import patch
from unittest.mock import patch, MagicMock
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos
from parameterized import parameterized_class

class TestAccessNestedMap(unittest.TestCase):
    """Test cases for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map with various inputs."""
        self.assertEqual(access_nested_map(nested_map, path), expected)
 @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map raises KeyError for invalid paths."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{path[-1]}'")

class TestGetJson(unittest.TestCase):
    """Test cases for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')  # Mock the requests.get method
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json returns expected payload from URL."""
        # Create a mock response object with a json method
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the get_json function
        result = get_json(test_url)

        # Assertions
        mock_get.assert_called_once_with(test_url)  # Ensure get was called once with the correct URL
        self.assertEqual(result, test_payload)  # Ensure the result matches the expected payload

class TestMemoize(unittest.TestCase):
    """Test cases for the memoize decorator."""

    def test_memoize(self):
        """Test that memoization works as expected."""

        class TestClass:
            """Class for testing memoization."""

            def a_method(self):
                """Returns a constant value."""
                return 42

            @memoize
            def a_property(self):
                """Memoized property that calls a_method."""
                return self.a_method()

        # Create an instance of TestClass
        test_instance = TestClass()

        # Patch the a_method
        with patch.object(test_instance, 'a_method') as mock_method:
            mock_method.return_value = 42

            # Call the memoized property twice
            result_first_call = test_instance.a_property()
            result_second_call = test_instance.a_property()

            # Check the results
            self.assertEqual(result_first_call, 42)
            self.assertEqual(result_second_call, 42)

            # Ensure that a_method is called only once
            mock_method.assert_called_once()

class TestGithubOrgClient(unittest.TestCase):
    """Test cases for the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        # Arrange
        expected_value = {"name": org_name}  # Example expected output
        mock_get_json.return_value = expected_value

        # Create an instance of GithubOrgClient
        client = GithubOrgClient(org_name)

        # Act
        result = client.org()

        # Assert
        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')
        self.assertEqual(result, expected_value)

class TestGithubOrgClient(unittest.TestCase):
    """Test cases for the GithubOrgClient class."""

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org):
        """Test that _public_repos_url returns the correct value based on org."""
        # Arrange: Set up the mock return value for the org property
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/testorg/repos"
        }

        # Act: Create an instance of GithubOrgClient and access _public_repos_url
        client = GithubOrgClient("testorg")
        result = client._public_repos_url

        # Assert: Check that the result matches the expected URL
        expected_url = "https://api.github.com/orgs/testorg/repos"
        self.assertEqual(result, expected_url)

class TestGithubOrgClient(unittest.TestCase):
    """Test cases for the GithubOrgClient class."""

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the correct list of repos."""
        # Arrange: Set up the mock return value for get_json
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        
        # Mock the _public_repos_url property
        with patch('client.GithubOrgClient._public_repos_url', new_callable=property) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/orgs/testorg/repos"

            # Act: Create an instance of GithubOrgClient and call public_repos
            client = GithubOrgClient("testorg")
            repos = client.public_repos()

            # Assert: Check the result and that mocks were called
            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(repos, expected_repos)
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/testorg/repos")
            mock_public_repos_url.assert_called_once()

class TestGithubOrgClient(unittest.TestCase):
    """Test cases for the GithubOrgClient class."""

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that has_license correctly identifies license presence."""
        # Arrange: Create an instance of GithubOrgClient
        client = GithubOrgClient("testorg")

        # Act: Call the has_license method
        result = client.has_license(repo, license_key)

        # Assert: Check that the result matches the expected value
        self.assertEqual(result, expected)
@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    [
        (org_payload, repos_payload, expected_repos, apache2_repos),
    ],
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the GithubOrgClient class."""

    @classmethod
    def setUpClass(cls):
        """Set up the patcher for requests.get."""
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()
        
        # Define the side effects based on the expected URLs
        cls.mock_get.side_effect = lambda url: MockResponse(cls.org_payload if "orgs" in url else cls.repos_payload)

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test that public_repos returns the correct list of repos."""
        # Arrange
        client = GithubOrgClient("testorg")

        # Act
        repos = client.public_repos()

        # Assert
        self.assertEqual(repos, self.expected_repos)

class MockResponse:
    """Mock response to mimic requests.get().json() behavior."""
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        """Return the mocked JSON data."""
        return self.json_data

@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    [
        (org_payload, repos_payload, expected_repos, apache2_repos),
    ],
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the GithubOrgClient class."""

    @classmethod
    def setUpClass(cls):
        """Set up the patcher for requests.get."""
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()
        
        # Define the side effects based on the expected URLs
        cls.mock_get.side_effect = lambda url: MockResponse(cls.org_payload if "orgs" in url else cls.repos_payload)

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test that public_repos returns the correct list of repos."""
        # Arrange
        client = GithubOrgClient("testorg")

        # Act
        repos = client.public_repos()

        # Assert
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test that public_repos returns the correct repos filtered by license."""
        # Arrange
        client = GithubOrgClient("testorg")

        # Act
        repos_with_license = client.public_repos(license="apache-2.0")

        # Assert
        self.assertEqual(repos_with_license, self.apache2_repos)

class MockResponse:
    """Mock response to mimic requests.get().json() behavior."""
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        """Return the mocked JSON data."""
        return self.json_data

if __name__ == "__main__":
    unittest.main()
