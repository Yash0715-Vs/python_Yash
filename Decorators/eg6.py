import time


def timer(func):

    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        print(f"{func.__name__} took {time.time() - start:.4f}s")

        return result

    return wrapper


@timer
def slow_square(n):
    return n * n


print(slow_square(10))