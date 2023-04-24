import unittest
import sys

sys.path.append("/home/labex/project")

from advanced_functionality import advanced_evaluate_expression


class TestEvaluateExpression(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(advanced_evaluate_expression("1+2-3*4/2"), -3)
        self.assertAlmostEqual(advanced_evaluate_expression("2.5+1.5-3*4/2"), -2)

    def test_parentheses(self):
        self.assertAlmostEqual(
            advanced_evaluate_expression("(1+2)*(3-4)/(6+6) + 2**2"), 3.75
        )
        self.assertAlmostEqual(
            advanced_evaluate_expression("(1.5+2.5)*(3.5-4.5)/(2.5+5.5)"), -0.5
        )

    def test_modulo(self):
        self.assertEqual(advanced_evaluate_expression("9%4%2"), 1)
        self.assertEqual(advanced_evaluate_expression("10.5%4%1.5"), 1)

    def test_power(self):
        self.assertEqual(advanced_evaluate_expression("2**3**2"), 64)
        self.assertAlmostEqual(advanced_evaluate_expression("3**2**2"), 81, 10)

    def test_unary_minus(self):
        self.assertEqual(advanced_evaluate_expression("-2+-3*-4"), 10)
        self.assertEqual(advanced_evaluate_expression("1+-6/-3+4"), 7)

    def test_scientific_notation(self):
        self.assertEqual(
            advanced_evaluate_expression("1.23e4+2.34e3-3.45e2*4.56e1"), -1092
        )
        self.assertAlmostEqual(advanced_evaluate_expression("-1E-4*2E6+3E2"), 100)

    def test_constants(self):
        self.assertAlmostEqual(
            advanced_evaluate_expression("pi+e/2-1"), 3.5007335678193154, 10
        )
        self.assertAlmostEqual(
            advanced_evaluate_expression("2*pi+e**2"), 13.672241406110235, 10
        )

    def test_functions(self):
        self.assertAlmostEqual(
            advanced_evaluate_expression("sin(pi/6)+cos(pi/3)*tan(0)"),
            0.49999999999999994,
        )
        self.assertAlmostEqual(
            advanced_evaluate_expression("cos(sin(tan(pi/4)))"), 0.6663667453928807
        )
        with self.assertRaises(ZeroDivisionError):
            advanced_evaluate_expression("1/tan(0)")

    def test_complex_expression(self):
        self.assertAlmostEqual(
            advanced_evaluate_expression(
                "-3 * (4 + 2 / (1 + 3)) ** 2+sin(pi/4)+cos(pi/6)"
            ),
            -59.17686781502901,
            10,
        )

    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            advanced_evaluate_expression("1+")
        with self.assertRaises(ValueError):
            advanced_evaluate_expression("(1+2")
        with self.assertRaises(ZeroDivisionError):
            advanced_evaluate_expression("1/0")
        with self.assertRaises(ZeroDivisionError):
            advanced_evaluate_expression("5 % 0")


if __name__ == "__main__":
    unittest.main()
