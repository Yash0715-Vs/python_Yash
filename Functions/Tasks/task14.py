def student(name, *marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "Fail"

    print(f"Student Name : {name}")
    print(f"the sum is: {sum(marks)}")
    print(f"the avg is: {sum(marks)/len(marks)}")
    print(f"Grade: {grade}")


# Function Calls
student("Yash", 85, 90, 78, 88, 95)

print()

student("Preet", 70, 75, 68, 72, 65)

print()

student("Aryan", 40, 55, 50, 45, 35)
print()