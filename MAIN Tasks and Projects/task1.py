students = [
    {
        "name": "Yash",
        "marks": [85, 78, 92, 88, 76]
    },
    {
        "name": "Sahil",
        "marks": [72, 81, 69, 75, 80]
    },
    {
        "name": "Preet",
        "marks": [95, 91, 89, 94, 96]
    },
    {
        "name": "Aryan",
        "marks": [60, 65, 70, 58, 64]
    }
]


def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    return sum(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def analyze_student(student):
    marks = student["marks"]

    total = calculate_total(marks)
    average = calculate_average(marks)
    highest = max(marks)
    lowest = min(marks)
    grade = calculate_grade(average)

    return {
        "name": student["name"],
        "marks": marks,
        "total": total,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "grade": grade
    }


results = []

for student in students:
    result = analyze_student(student)
    results.append(result)


results.sort(key=lambda student: student["average"], reverse=True)


print("===== STUDENT PERFORMANCE =====")

for student in results:
    print(f"\nName     : {student['name']}")
    print(f"Marks    : {student['marks']}")
    print(f"Total    : {student['total']}")
    print(f"Average  : {student['average']:.2f}")
    print(f"Highest  : {student['highest']}")
    print(f"Lowest   : {student['lowest']}")
    print(f"Grade    : {student['grade']}")


print("\n===== RANKING =====")

for rank, student in enumerate(results, start=1):
    print(
        f"{rank}. {student['name']} "
        f"- Average: {student['average']:.2f}"
    )