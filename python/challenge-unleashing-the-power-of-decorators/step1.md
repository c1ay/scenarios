# Timing Decorator

Create a decorator that can time the execution of a function and print the execution time.

### TODO

In `time_it.py`, create a decorator called `time_it` that will take in a function as an argument and time its execution. The decorator should print out the execution time in seconds.

### Examples

```python
@time_it
def my_function():
    time.sleep(1)
    return "done"

result = my_function() # Output: "Execution time: 1.00123456789 seconds"

@time_it
def another_function(x, y):
    return x + y

result = another_function(3, 4) # Output: "Execution time: 0.00012345678 seconds"
```
