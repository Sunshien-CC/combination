import time
import functools


def timer(fn):

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = fn(*args, **kwargs)
        end_time = time.perf_counter()
        print(f'Duration: {end_time - start_time}s')
        return result

    return wrapper
