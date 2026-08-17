username = input("enter the username: ")
def login_required(func):
    def wrapper(login):

        user = "Yash"

        if login == user:
            print("Login successful...")
            func(login)

        elif login == "":
            print("Please login first")

        else:
            print("Enter the valid username")

    return wrapper

@login_required
def dashboard(username):
    print(f"Welcome to Dashboard, {username}!")


dashboard(username)


@login_required
def profile(username):
    print(f"Opening profile for {username}...")


profile(username)