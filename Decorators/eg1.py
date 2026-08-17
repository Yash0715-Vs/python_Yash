def greeting_decorator(func):
    def wrapper():
        print("Welcome to python")
        func()
    return wrapper

@greeting_decorator
def hello():
    print("hello Yash")
hello()