def retry(func):
    def wrapper(*args,**kwargs):
        for attempt in range(1,4):
            try:
                result = func(*args,**kwargs)
                return result
            except Exception as e:
                print(f"attempt{attempt} failed!")

        print("all attempt fail")
    return wrapper

@retry
def test():

    print("Trying...")

    raise ValueError("Something went wrong")
test()