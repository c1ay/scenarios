# Sub-Challenge 3: Authentication Decorator

```python
def authenticate(func):
    """
    A decorator function that prompts the user to enter a username and password before running the decorated function.

    Parameters:
    -----------
    func : function
        The function to be authenticated.

    Returns:
    --------
    function
        A wrapper function that prompts the user to enter a username and password before running the decorated function.

    Raises:
    -------
    Exception
        If the username or password is invalid.

    Example:
    --------
    @authenticate
    def my_function():
        # code to be authenticated
    """
    def wrapper(*args, **kwargs):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == "myusername" and password == "mypassword":
            return func(*args, **kwargs)
        else:
            raise Exception("Invalid username or password")
    return wrapper
```
