import time


def performance(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print(f"Function: {func.__name__}")
        print(f"Result: {result}")
        print(f"Time: {end - start:.4f}s")

        return result

    return wrapper


@performance
def multiply(a, b):
    return a * b


@performance
def add(a, b):
    return a + b


@performance
def power(a, b):
    return a ** b


multiply(20, 30)
add(10, 20)
power(2, 5)