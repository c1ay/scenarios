import unittest
from unittest.mock import patch, call
import sys

sys.path.append("/home/labex/project")
from authenticate import *
from io import StringIO


class TestAuthenticateDecorator(unittest.TestCase):
    def test_authenticate_valid_credentials(self):
        expected_output = "Authentication successful\n"
        with patch("builtins.input", side_effect=["myusername", "mypassword"]):
            with patch("sys.stdout", new=StringIO()) as fake_output:

                @authenticate
                def my_function():
                    print("Authentication successful")

                my_function()
                self.assertEqual(fake_output.getvalue(), expected_output)

    def test_authenticate_invalid_credentials(self):
        with self.assertRaises(Exception):
            with patch(
                "builtins.input", side_effect=["wrongusername", "wrongpassword"]
            ):

                @authenticate
                def my_function():
                    pass

                my_function()


if __name__ == "__main__":
    unittest.main()
