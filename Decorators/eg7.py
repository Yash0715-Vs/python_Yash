import time

def timer(func):
    def wrapper(*args,**kwargs):
        start= time.time()
        result = func(*args, **kwargs)

        print(f"{func.__name__} took {time.time() - start:.4f}s")

        return result

    return wrapper

@timer
def calculate_sum(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total

print(calculate_sum(10000000))