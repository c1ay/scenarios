# Math Expression Evaluator

In this challenge, you need to complete an `evaluate_expression` function that evaluates a string arithmetic expression, and follow the requirements below.

## Requirements

Please complete the `evaluate_expression` function in the file `/home/labex/project/basic_functionality.py`.

Your task is to create a Python function that can evaluate a string expression consisting of arithmetic operators (`+`, `-`, `*`, `/`) and parentheses. The function should follow the standard order of operations (PEMDAS) and return the result of the expression.

The function should have the following signature:

## Constraints:

- The input expression will contain only digits, parentheses, and the four basic arithmetic operators: `+`, `-`, `*`, and `/`.
- The input expression will be a valid arithmetic expression.
- The input expression may contain spaces, but these should be ignored.
- The input expression will have no more than 10000 characters.
- Implement support for the modulo operator (`%`) and the power operator (`**`).
- You cannot use the `eval` function.

## Example:

```python
>>> evaluate_expression("2 + 3 * 4")
14
>>> evaluate_expression("(2 + 3) * 4")
20
>>> evaluate_expression("3 + 4 * 2 / ( 1 - 5 )")
5.5
>>> evaluate_expression("2 ** 3 % 3")
2
>>> evaluate_expression("2 ** (3 % 2)")
2
>>> evaluate_expression("10 % 3 * 2")
2
```
