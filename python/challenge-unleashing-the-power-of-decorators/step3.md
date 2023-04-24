# Authentication Decorator

Create a decorator that can authenticate a user before allowing them to execute a function.

### TODO

In `authenticate.py`, create a decorator called `authenticate` that will take in a function as an argument and authenticate the user before allowing them to execute the function. The decorator should prompt the user to enter their username and password. If the username and password are correct, the function should be executed. If the username and password are incorrect, the decorator should raise an exception.

### Examples

```python
@authenticate
def my_function():
    print("Access granted")

my_function()
```

In this example, the authenticate decorator is used to authenticate the user before calling the `my_function()` function.

- The function doesn't take any arguments and prints "Access granted" to the console if the user enters the correct username and password.
- If the user enters an incorrect username or password, the decorator raises an exception with the message "Invalid username or password".

When the script is run, the user is prompted to enter a username and password.

- If they enter "myusername" and "mypassword", the `my_function()` function is called and "Access granted" is printed to the console.
- If they enter an incorrect username or password, the decorator raises an exception and the program terminates.
