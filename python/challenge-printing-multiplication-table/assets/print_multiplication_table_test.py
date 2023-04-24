import sys

sys.path.append("/home/labex/project")

import unittest
from io import StringIO
from print_multiplication_table import print_multiplication_table


class TestPrintMultiplicationTable(unittest.TestCase):
    def test_print_multiplication_table(self):
        test_cases = [
            {
                "input": 5,
                "expected_output": "5 x 1 = 5\n5 x 2 = 10\n5 x 3 = 15\n5 x 4 = 20\n5 x 5 = 25\n5 x 6 = 30\n5 x 7 = 35\n5 x 8 = 40\n5 x 9 = 45\n5 x 10 = 50\n",
            },
            {
                "input": 7,
                "expected_output": "7 x 1 = 7\n7 x 2 = 14\n7 x 3 = 21\n7 x 4 = 28\n7 x 5 = 35\n7 x 6 = 42\n7 x 7 = 49\n7 x 8 = 56\n7 x 9 = 63\n7 x 10 = 70\n",
            },
            {
                "input": 2,
                "expected_output": "2 x 1 = 2\n2 x 2 = 4\n2 x 3 = 6\n2 x 4 = 8\n2 x 5 = 10\n2 x 6 = 12\n2 x 7 = 14\n2 x 8 = 16\n2 x 9 = 18\n2 x 10 = 20\n",
            },
        ]

        for test_case in test_cases:
            input_data = test_case["input"]
            expected_output = test_case["expected_output"]
            captured_output = StringIO()
            sys.stdout = captured_output
            print_multiplication_table(input_data)
            sys.stdout = sys.__stdout__
            self.assertEqual(captured_output.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
