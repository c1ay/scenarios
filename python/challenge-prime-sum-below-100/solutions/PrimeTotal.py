# Define a function to check if a number is prime
def prime(n):
    # If n is less than 2, it is not a prime number
    if n < 2:
        return False
    # Check if n is divisible by any integer from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            # If n is divisible by i, it is not a prime number
            return False
    # If n is not divisible by any integer from 2 to the square root of n, it is a prime number
    return True


# Initialize a variable to store the sum of all prime numbers below 100
prime_sum = 0

# Loop through all numbers from 2 to 99
for i in range(2, 100):
    # Check if i is prime using the prime function
    if prime(i):
        # If i is prime, add it to the prime_sum variable
        prime_sum += i

# Print the sum of all prime numbers below 100
print(prime_sum)
