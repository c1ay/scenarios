# This function takes a number as a parameter and prints its multiplication table up to 10.
def print_multiplication_table(num):
    # Iterate through the range 1 to 10 (inclusive).
    for i in range(1, 11):
        # Multiply the number by the current iterator value and print the result.
        print(f"{num} x {i} = {num * i}")
