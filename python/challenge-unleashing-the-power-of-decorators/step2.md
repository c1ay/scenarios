# Logging Decorator

Create a decorator that can log the execution of a function and save the log to a file.

### TODO

In `log_it.py`, create a decorator called `log_it` that will take in a function as an argument and log its execution. The decorator should save the log to a file named `log.txt` in the current directory. The log should include the timestamp, the function name, and the arguments passed to the function.

### Examples

```python
@log_it
def my_function(x, y):
    return x + y

# Call the function
result = my_function(3, 4)
print(result) # Output: 7

# Check the log file
with open('log.txt', 'r') as f:
    print(f.read())
# Output: "Timestamp: 1636203200.123456, Function: my_function, Arguments: (3, 4), {}"
```
