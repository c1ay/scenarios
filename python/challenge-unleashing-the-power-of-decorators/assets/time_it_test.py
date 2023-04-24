import unittest
from unittest.mock import Mock
import sys

sys.path.append("/home/labex/project")
from time_it import *


class TestTimeIt(unittest.TestCase):
    @time_it
    def mock_func(self):
        return 42

    @time_it
    def slow_func(self):
        time.sleep(1)

    def test_decorator_should_return_result_of_the_decorated_function(self):
        result = self.mock_func()
        self.assertEqual(result, 42)

    def test_decorator_should_print_execution_time(self):
        with unittest.mock.patch("builtins.print") as mock_print:
            self.slow_func()

            mock_print.assert_called_once()
            call_args = mock_print.call_args.args[0]
            self.assertIn("Execution time", call_args)


if __name__ == "__main__":
    unittest.main()
