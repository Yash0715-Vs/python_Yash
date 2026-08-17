username = input("enter the username: ")
def login_required(func):
    def wrapper(login):

        user = "Yash"

        if login == user:
            print("Login successful...")
            func()

        elif login == "":
            print("Please login first")

        else:
            print("Enter the valid username")

    return wrapper

@login_required
def dashboard():
    print("Welcome to Dashboard")

dashboard(username)
        