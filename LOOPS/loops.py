# n = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")

# fruits = ["Apple", "Banana", "Mango", "Orange"]

# for index, value in enumerate(fruits):
#     print(index, ":", value)

# while loop
# while True:
#     print("\n----- Calculator Menu -----")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Exit")

#     choice = int(input("Enter your choice (1-5): "))

#     if choice == 5:
#         print("Exiting Calculator...")
#         break

#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))

#     if choice == 1:
#         print("Result:", num1 + num2)

#     elif choice == 2:
#         print("Result:", num1 - num2)

#     elif choice == 3:
#         print("Result:", num1 * num2)

#     elif choice == 4:
#         if num2 != 0:
#             print("Result:", num1 / num2)
#         else:
#             print("Division by zero is not allowed.")

#     else:
#         print("Invalid Choice!")

#break
students= ["yash","sahil","preet"]
for student in students:
    
        if student == "sahil":
            print("found")
            break
else:
    print("not found")
