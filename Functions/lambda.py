#1
add = lambda a,b: a+b
print(add(3,4))

#2
l =[2,3,3,4,5,6,8]
even = list(filter(lambda x: x % 2 == 0, l))
print(even)

#3
numbers = [2, 3, 4, 5, 6]

cube = list(map(lambda x: x ** 3, numbers))

print(f"Original List : {numbers}")
print(f"Cube List     : {cube}")

#4
numbers = [10, 25, 50, 60, 75, 90, 45]

result = list(filter(lambda x: x > 50, numbers))

print(f"Original List : {numbers}")
print(f"Numbers > 50  : {result}")

#5
students = [
    ("Yash", 85),
    ("Rahul", 92),
    ("Amit", 78),
    ("Priya", 95)
]

ascending = sorted(students, key=lambda student: student[1])
descending = sorted(students, key=lambda student: student[1], reverse=True)
top_student = max(students, key=lambda student: student[1])

print("Students (Ascending Order):")
for student in ascending:
    print(student)
print("Students (Descending Order):")
for student in descending:
    print(student)
print(f"Top Student: {top_student}")