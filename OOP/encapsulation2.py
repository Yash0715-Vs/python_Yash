class User:

    def __init__(self):
        self.__username = ""
        self.__age = 0

    # Getter for username
    def get_username(self):
        return self.__username

    # Setter for username
    def set_username(self, username):
        if username != "":
            self.__username = username
        else:
            print("Invalid username")

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, age):
        if 13 <= age <= 100:
            self.__age = age
        else:
            print("Invalid age")


# Create object
user = User()

# Take input
username = input("Enter username: ")
age = int(input("Enter age: "))

# Use setters
user.set_username(username)
user.set_age(age)

# Use getters
print("\nUser Information:")
print("Username:", user.get_username())
print("Age:", user.get_age())