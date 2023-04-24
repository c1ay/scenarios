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
        return

    return wrapper


if __name__ == "__main__":

    @time_it
    def my_function():
        time.sleep(1)
        return "done"

    result = my_function()  # Output: "Execution time: 1.00123456789 seconds"

    @time_it
    def another_function(x, y):
        return x + y

    result = another_function(3, 4)  # Output: "Execution time: 0.00012345678 seconds"
