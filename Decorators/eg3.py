def decorator(func):
    def wrapper(*args):
        print("hello...")
        print("calculation started")
        func(*args)
    return wrapper

@decorator
def add(a,b,c):
    print(f"the add is: {a+b+c}")

add(2,3,4)