from student.student import Student


students = []

try:
    s1 = Student("YASH", 101, "Computer", 85, 90, 88, 92)
    s2 = Student("NEEL", 102, "IT", 75, 80, 78, 82)
    s3 = Student("ARYAN", 103, "Computer", 95, 92, 94, 96)

    students.append(s1)
    students.append(s2)
    students.append(s3)

except ValueError:
    print("Invalid marks!")


print("STUDENT DETAILS")
print("=" * 30)

for student in students:
    student.display()


# Sort students by average
students.sort(key=lambda student: student.calculate_average(), reverse=True)

print("\nSTUDENTS SORTED BY AVERAGE")
print("=" * 30)

for student in students:
    print(
        student.name,
        "->",
        f"{student.calculate_average()}"
    )


# Find topper
topper = max(
    students,
    key=lambda student: student.calculate_average()
)

print("\nTOPPER")
print("=" * 30)

print(f"Name    : {topper.name}")
print(f"Average : {topper.calculate_average()}")
print(f"Grade   : {topper.calculate_grade()}")