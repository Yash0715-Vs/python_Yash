
a = "10"
b = 0

# Write your logic here
try:
    c = int(a)
    print(c)
    print(c/b)

except ValueError:
    print("plz enter the number.")

except ZeroDivisionError:
    print("Cannot divide by zero")