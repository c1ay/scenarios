def evaluate_expression(expression: str) -> float:
    """
    Evaluates a string arithmetic expression consisting of +,-,*,/,%,** and () operators.

    Args:
        expression (str): A valid arithmetic expression containing only numbers, parentheses, and
        +,-,*,/,%,** operators.

    Returns:
        float: The result of evaluating the arithmetic expression.

    Raises:
        ValueError: If the input expression contains invalid characters or is not well-formed.
    """

    # Remove spaces from the input expression
    expression = expression.replace(" ", "")
    # The symbol "**" is represented by a letter, such as m, so that the program can iterate through them one by one.
    # expression = expression.replace("**", "m")

    # Use a regular expression to tokenize the input expression into numbers, operators, and parentheses
    import re

    pattern = r"[+\-/%()]|(?<!\*)\*(?!\*)|\*\*|\d+"
    tokens = re.findall(pattern, expression)
    # Define the operator precedence
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2, "**": 3}

    # Define functions for each operator
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("division by zero")
        return a / b

    def modulo(a, b):
        if b == 0:
            raise ZeroDivisionError("modulo (%) by zero")
        return a % b

    def power(a, b):
        return a**b

    # Evaluate the expression using the shunting yard algorithm
    output_queue = []
    operator_stack = []
    for token in tokens:
        # If the token is a number, append it to the output queue
        if re.match(r"[0-9]+", token):
            output_queue.append(float(token))
        # If the token is an operator, pop operators from the stack and append them to the output queue
        # until an operator of lower precedence is at the top of the stack, then push the token onto the stack.
        elif token in precedence:
            while (
                operator_stack
                and operator_stack[-1] != "("
                and precedence[token] <= precedence[operator_stack[-1]]
            ):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        # If the token is a left parenthesis, push it onto the stack.
        elif token == "(":
            operator_stack.append(token)
        # If the token is a right parenthesis, pop operators from the stack and append them to the output
        # queue until a left parenthesis is at the top of the stack, then discard the parentheses.
        elif token == ")":
            while operator_stack[-1] != "(":
                output_queue.append(operator_stack.pop())
            operator_stack.pop()

    while operator_stack:
        output_queue.append(operator_stack.pop())
    # Evaluate the postfix expression using a stack
    operand_stack = []
    for token in output_queue:
        if isinstance(token, float):
            operand_stack.append(token)
        else:
            try:
                b = operand_stack.pop()
                a = operand_stack.pop()
            except IndexError:  # not enough arguments for an operator
                raise ValueError("invalid expression")
            if token == "+":
                result = add(a, b)
            elif token == "-":
                result = subtract(a, b)
            elif token == "*":
                result = multiply(a, b)
            elif token == "/":
                result = divide(a, b)
            elif token == "%":
                result = modulo(a, b)
            elif token == "**":
                result = power(a, b)
            operand_stack.append(result)

    # The final value on the stack is the result
    return operand_stack[0]
