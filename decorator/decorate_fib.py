from functools import wraps


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("{}, {}, {}, {}".format(func.__name__, args, kwargs, result))
        return result

    return wrapper


@trace
def fibonacci(n):
    if n in [0, 1]:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(4))
help(fibonacci)
