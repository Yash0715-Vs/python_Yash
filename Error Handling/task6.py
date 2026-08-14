try:
    a = float(input("enter the 1st no: "))
    b = float(input("enter the 2nd no: "))
    print("\n1. Add")
    print("\n2. Sub")
    print("\n3. Multiply")
    print("\n4. Div")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        result = a + b

    elif choice == 2:
        result = a - b

    elif choice == 3:
        result = a * b

    elif choice == 4:
        result = a / b

    else:
        raise ValueError("Invalid menu choice")

except ValueError as e:
    print(f"Error: {e}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

else:
    print(f"Result: {result}")

finally:
    print("Calculator program finished.")