import sys

sys.path.append("/home/labex/project")
from basic_functionality import evaluate_expression


def test_evaluate_expression():
    assert evaluate_expression("20 + 3 * 4") == 32
    assert evaluate_expression("(2 + 3) * 4") == 20
    assert evaluate_expression("3 + 4 * 2 / ( 1 - 5 )") == 1
    assert evaluate_expression("2 ** 3 % 3") == 2
    assert evaluate_expression("2 ** (3 % 2)") == 2
    assert evaluate_expression("10 % 3 * 2") == 2
    assert evaluate_expression("1 + 2 + 3 + 4 + 5") == 15
    assert evaluate_expression("(1 + 2) * (3 + 4)") == 21
    assert evaluate_expression("1 * 2 + 3 * 4") == 14
    assert evaluate_expression("(1 + 2 + 3 + 4 + 5) / 5") == 3
    assert evaluate_expression("(1 + 2 + 3 + 4 + 5) % 5") == 0
    assert evaluate_expression("((1 + 2) * (3 + 4)) / (1 + 2)") == 7.0
    print("All test cases passed")


if __name__ == "__main__":
    test_evaluate_expression()
