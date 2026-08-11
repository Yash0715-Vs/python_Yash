password = "Yash123"

for i in range(3):
    user_password = input("Enter Password: ")

    if user_password == password:
        print("Login Successful")
        break
    else:
        print("Wrong Password")

else:
    print("Account Locked")