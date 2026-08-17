import json

# 1. Read JSON file
with open("students.json", "r") as f:
    data = json.load(f)


students = data["students"]


# 2. Print all students
print("All Students:")

for student in students:
    print(
        student["name"],
        "-",
        student["course"],
        "-",
        student["marks"]
    )


# 3. Students with marks greater than 80
print("\nStudents with marks greater than 80:")

for student in students:
    if student["marks"] > 80:
        print(student["name"], "-", student["marks"])


# 4. Calculate average marks
total = 0

for student in students:
    total += student["marks"]

average = total / len(students)

print("\nAverage Marks:", average)


# 5. Find student with highest marks
highest = students[0]

for student in students:
    if student["marks"] > highest["marks"]:
        highest = student

print("\nHighest Marks:")
print(highest["name"], "-", highest["marks"])