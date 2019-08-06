from functools import wraps
from time import time


def timeit(search_name):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            start = time()
            result = f(*args, **kwargs)
            end = time()
            print('Elapsed time for {}: {} ms'.format(search_name, (end - start) * 1000))
            return result

        return wrapper

    return decorator
