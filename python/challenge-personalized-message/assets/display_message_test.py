import sys

sys.path.append("/home/labex/project")

import unittest
from io import StringIO
from display_message import display_message


class TestDisplayMessage(unittest.TestCase):
    def test_display_message(self):
        test_cases = [
            {
                "input": ("Alice", 25),
                "expected_output": "Hello, my name is Alice and I am 25 years old.\n",
            },
            {
                "input": ("Bob", 32),
                "expected_output": "Hello, my name is Bob and I am 32 years old.\n",
            },
            {
                "input": ("Charlie", 18),
                "expected_output": "Hello, my name is Charlie and I am 18 years old.\n",
            },
        ]

        for test_case in test_cases:
            input_data = test_case["input"]
            expected_output = test_case["expected_output"]
            captured_output = StringIO()
            sys.stdout = captured_output
            display_message(*input_data)
            sys.stdout = sys.__stdout__
            self.assertEqual(captured_output.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
