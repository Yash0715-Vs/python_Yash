students = []


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "Fail"


def add_student(name, roll_number, department, *marks):
    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)

    student = {
        "name": name,
        "roll_number": roll_number,
        "department": department,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student)

    return student


def display_student(student):
    print("\n===== STUDENT DETAILS =====")
    print(f"Name       : {student['name']}")
    print(f"Roll Number: {student['roll_number']}")
    print(f"Department : {student['department']}")
    print(f"Marks      : {student['marks']}")
    print(f"Total      : {student['total']}")
    print(f"Average    : {student['average']}")
    print(f"Grade      : {student['grade']}")


# Add students
student1 = add_student("Yash", 101, "Computer", 85, 90, 78, 88)
student2 = add_student("Rahul", 102, "IT", 92, 95, 90, 88)
student3 = add_student("Amit", 103, "Computer", 70, 75, 68, 72)
student4 = add_student("Priya", 104, "IT", 95, 98, 92, 96)

# Display students
display_student(student1)
display_student(student2)
display_student(student3)
display_student(student4)


# Sort students by average marks
sorted_students = sorted(
    students,
    key=lambda student: student["average"],
    reverse=True
)



for student in sorted_students:
    print(f"{student['name']} - {student['average']}")


# Find topper
topper = max(students, key=lambda student: student["average"])

print("\n===== TOPPER =====")
print(f"Name    : {topper['name']}")
print(f"Average : {topper['average']}")
print(f"Grade   : {topper['grade']}")