
def login(user_name, password):
    currect_user_name="Yash"
    currect_password= "1234"

    if user_name != currect_user_name:
        return "invalid username"

    elif password != currect_password:
        return "wrong password"

    else:
        return "login succesfull"



username= input("enter the username: ")
password= input("enter the password: ")

result= login(username,password)
print(result)