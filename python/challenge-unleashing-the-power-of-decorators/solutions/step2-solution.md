# Logging Decorator

```python
import logging, time

def log_it(func):
    """
    A decorator function that logs the timestamp, name of the decorated function, and its arguments to a file.

    Parameters:
    -----------
    func : function
        The function to be logged.

    Returns:
    --------
    function
        A wrapper function that logs the timestamp, name of the decorated function, and its arguments to a file.

    Example:
    --------
    @log_it
    def my_function():
        # code to be logged
    """
    logging.basicConfig(filename='log.txt', level=logging.INFO)
    def wrapper(*args, **kwargs):
        logging.info(f"Timestamp: {time.time()}, Function: {func.__name__}, Arguments: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper
```
