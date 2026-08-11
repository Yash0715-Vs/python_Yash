# n = int(input("enter the no.: "))
# if n>=0:
#     print("positive")
# elif n<0:
#     print("negative")
# elif n==0:
#     print("zero")
# else:
#     print("invalid input")


# marks = int(input("Enter your marks: "))

# if(marks<=100 and marks>=90):
#     grade = "Ex"
# elif(marks<90 and marks>=80):
#     grade = "A"
# elif(marks<80 and marks>=70):
#     grade = "B"
# elif(marks<70 and marks>=60):
#     grade = "C"
# elif(marks<60 and marks>=50):
#     grade = "D"
# elif(marks<50):
#     grade = "F"

# print("Your grade is:", grade)


#calculator
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# choice = input("Enter operation (+, -, *, /): ")

# if choice == "+":
#     print(f"Result:, {num1 + num2}")

# elif choice == "-":
#     print(f"Result: {num1 - num2}")

# elif choice == "*":
#     print(f"Result: {num1 * num2}")

# elif choice == "/":
#     if num2 != 0:
#         print(f"Result: {num1 / num2}")
#     else:
#         print("Division by zero is not allowed.")

# else:
#     print("Invalid operation!")


salary = 55000
if salary >=100000:
    print("bonus is 20000")
elif salary >=50000:
    print("bonus is 10000")
elif salary >=20000:
    print("bonus is 4000")
else:
    print("no boonus")
