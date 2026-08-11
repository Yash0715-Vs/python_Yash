def addition(a, b):
    print(f"Result = {a + b}")

def subtraction(a, b):
    print(f"Result = {a - b}")

def multiplication(a, b):
    print(f"Result = {a * b}")

def division(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(f"Result = {a / b}")

def modulus(a,b):
    if b==0:
        print("error")
    else:
        print(f"result: {a%b}")

def power(a,b):
    print(f"result: {a**b}")


while True:

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. modulus")
    print("6. power")
    print("7. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 7:
        print("Calculator Closed!")
        break

    if choice < 1 or choice > 7:
        print("Invalid Choice! Please Try Again.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        addition(num1, num2)

    elif choice == 2:
        subtraction(num1, num2)

    elif choice == 3:
        multiplication(num1, num2)

    elif choice == 4:
        division(num1, num2)

    elif choice == 5:
        modulus(num1, num2)

    elif choice == 6:
        power(num1, num2)