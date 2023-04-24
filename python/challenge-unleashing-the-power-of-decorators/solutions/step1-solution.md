# Timing Decorator

```python
import time

def time_it(func):
    """
    A decorator function that measures the execution time of a given function and prints the result.

    Parameters:
    -----------
    func : function
        The function to be timed.

    Returns:
    --------
    function
        A wrapper function that measures the execution time of the input function and returns its result.

    Example:
    --------
    @time_it
    def my_function():
        # code to be timed
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper
```
