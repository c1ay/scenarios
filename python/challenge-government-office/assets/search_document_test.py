import sys

sys.path.append("/home/labex/project")

import unittest
from search_document import search_document


class TestSearchDocument(unittest.TestCase):
    def test_search_document(self):
        inventory = {"document1": "A1", "document2": "B2", "document3": "C3"}
        document_name = "document2"
        expected_output = "B2"
        self.assertEqual(search_document(inventory, document_name), expected_output)

        inventory = {"document1": "A1", "document2": "B2", "document3": "C3"}
        document_name = "document4"
        expected_output = "Document not found."
        self.assertEqual(search_document(inventory, document_name), expected_output)


if __name__ == "__main__":
    unittest.main()
