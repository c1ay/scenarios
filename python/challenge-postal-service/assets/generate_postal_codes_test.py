import sys

sys.path.append("/home/labex/project")

import unittest
from generate_postal_codes import generate_postal_codes


class TestPostalService(unittest.TestCase):
    def test_generate_postal_codes(self):
        self.assertEqual(len(generate_postal_codes(5)), 5)
        self.assertEqual(len(generate_postal_codes(10)), 10)
        self.assertEqual(len(set(generate_postal_codes(100))), 100)


if __name__ == "__main__":
    unittest.main()
