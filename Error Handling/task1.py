def addition(*numbers):
    return numbers[0] + numbers[1]


def subtraction(*numbers):
    return numbers[0] - numbers[1]


def multiplication(*numbers):
    return numbers[0] * numbers[1]


def division(*numbers):
    if numbers[1] == 0:
        raise ZeroDivisionError

    return numbers[0] / numbers[1]


def modulus(*numbers):
    if numbers[1] == 0:
        raise ZeroDivisionError

    return numbers[0] % numbers[1]


def power(*numbers):
    return numbers[0] ** numbers[1]


while True:

    print("\n========== CALCULATOR ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 7:
            print("Calculator Closed!")
            break

        if choice < 1 or choice > 7:
            print("Invalid Choice! Please Try Again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        except ValueError:
            print("Invalid Number! Please enter numbers only.")
            continue

        try:

            if choice == 1:
                result = addition(num1, num2)

            elif choice == 2:
                result = subtraction(num1, num2)

            elif choice == 3:
                result = multiplication(num1, num2)

            elif choice == 4:
                result = division(num1, num2)

            elif choice == 5:
                result = modulus(num1, num2)

            elif choice == 6:
                result = power(num1, num2)

            print(f"Result = {result}")

        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")

    except ValueError:
        print("Invalid Menu Input! Please enter a number.")