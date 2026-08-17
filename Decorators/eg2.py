def log_decorator(func):
    def wrapper():
        print("Function started")
        func()
        print("Function finished")
    return wrapper

@log_decorator
def calculate():
    print("Calculating...")

calculate()