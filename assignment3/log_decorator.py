# Task 1: Writing and Testing a Decorator

import logging
from functools import wraps

# Setup the logger
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
handler = logging.FileHandler("./decorator.log", "a")
logger.addHandler(handler)

def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        # Format log strings
        func_name = func.__name__
        pos_args = args if args else "none"
        kw_args = kwargs if kwargs else "none"
        return_val = result

        log_message = (
            f"\nfunction: {func_name}\n"
            f"positional parameters: {pos_args}\n"
            f"keyword parameters: {kw_args}\n"
            f"return: {return_val}\n"
        )

        logger.info(log_message)
        return result
    return wrapper

# 1. Function with no parameters
@logger_decorator
def greet():
    print("Hello, World!")

# 2. Function with variable positional arguments
@logger_decorator
def accept_positional(*args):
    return True

# 3. Function with only keyword arguments
@logger_decorator
def accept_keyword(**kwargs):
    return logger_decorator  # Just return the decorator itself as required

if __name__ == "__main__":
    # Call greet()
    greet()

    # Call accept_positional() with some sample argss
    accept_positional(10, 20, 30)

    # Call accept_keyword() with some keyword args
    accept_keyword(name="Hetal", course="Python", week=3)