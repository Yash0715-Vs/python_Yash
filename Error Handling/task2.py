try:
    user1 = int(input("enter the no.: "))
    user2 = int(input("enter the no.: "))

    print(user1/user2)

except ValueError:
    print("plz enter the number.")

except ZeroDivisionError:
    print("Cannot divide by zero")
    
