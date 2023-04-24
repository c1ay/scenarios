# NumPy Dot Product

## Problem Statement

You are given a dataset containing the weights of 10,000 people and their corresponding heights. You need to find the covariance matrix of the data using NumPy's dot function.

Write a function called `calculate_covariance_matrix()` that takes in two NumPy arrays of the same shape, representing the weights and heights of the individuals. The function should return the covariance matrix of the data using NumPy's dot function.

The covariance matrix is defined as follows:

```
covariance_matrix = 1/n * ((X - mean(X)).T @ (X - mean(X)))
```

where `X` is a matrix of shape `(n_samples, n_features)`, and `n` is the number of samples.

## Input

- `weights`: A NumPy array of shape `(n_samples, 1)` representing the weights of the individuals
- `heights`: A NumPy array of shape `(n_samples, 1)` representing the heights of the individuals

## Output

- A NumPy array of shape `(2, 2)` representing the covariance matrix of the data.

## Example

```python
import numpy as np

# Generate some sample data
weights = np.random.normal(loc=70, scale=10, size=(10000, 1))
heights = np.random.normal(loc=1.75, scale=0.1, size=(10000, 1))

# Calculate the covariance matrix
covariance_matrix = calculate_covariance_matrix(weights, heights)

print("Covariance matrix:")
print(covariance_matrix)

# Output:
"""
The result of the example code will vary each time it is executed due to the use of random data. However, the output will be a 2x2 NumPy array representing the covariance matrix of the weights and heights data. Here's an example of what the output might look like:
Covariance matrix:
[[ 101.19801587   -0.05747012]
 [  -0.05747012    0.01015618]]

"""
```
