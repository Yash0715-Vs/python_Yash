class AgeError(Exception):
    pass
age = 15
try:
    if age > 18:
        raise AgeError("valid age")
    else:
        raise AgeError(f"age must be above 18!, your age is {age}")

except AgeError as e:
    print(e)