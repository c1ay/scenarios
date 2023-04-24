import sys

sys.path.append("/home/labex/project")

import unittest
from record_visitor import record_visitor


class TestRecordVisitor(unittest.TestCase):
    def test_record_visitor(self):
        self.assertEqual(
            record_visitor("John Smith", "visa application"),
            "Visitor John Smith has come to the embassy for visa application.",
        )
        self.assertEqual(
            record_visitor("Jane Doe", "diplomatic mission"),
            "Visitor Jane Doe has come to the embassy for diplomatic mission.",
        )
        self.assertEqual(
            record_visitor("Bob Johnson", "consular services"),
            "Visitor Bob Johnson has come to the embassy for consular services.",
        )


if __name__ == "__main__":
    unittest.main()
