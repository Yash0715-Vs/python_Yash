def logger(func):
    def wrapper(*args):
        print("calling add..")
        print("function finished")
        func(*args)
    return wrapper

@logger
def add(a,b):
    print(f"the add is: {a+b}")

add(20,30)