class InvalidAgeError(Exception):
    pass


try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise InvalidAgeError("Age cannot be negative")

    print(f"Your age is: {age}")

except InvalidAgeError as e:
    print(f"Error: {e}")