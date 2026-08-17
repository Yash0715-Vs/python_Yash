def decorator(func):
    def wrapper(*args):
        print("calculating result...")
        func(*args)
    return wrapper

@decorator
def multiply(a, b):
    print(f"the multiplcation is: {a * b}")

multiply(4,5)