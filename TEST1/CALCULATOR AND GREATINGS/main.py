from utilities.calculator import add, subtract
from utilities.message import welcome, goodbye


welcome()

print(f"Addition: {add(20, 10)}")
print(f"Subtraction: {subtract(20, 10)}")

goodbye()