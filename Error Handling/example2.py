try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "1234":
        print("Login successful")
    else:
        print("Invalid credentials")

except Exception as e:
    print("Something went wrong:", e)