students = [
    ("Yash", 85),
    ("Neel", 92),
    ("Aryan", 78),
    ("Preet", 95)
]

ascending = sorted(students, key=lambda x:x [1])
print("Students (Ascending Order):")
for student in ascending:
    print(student)

descending = sorted(students, key=lambda x:x [1], reverse=True)
print("Students (Descending Order):")
for student in descending:
    print(student)

topper = max(students, key=lambda x: x[1])
print(f"the topper: {topper}")

lowest_score= min(students, key=lambda x: x[1])
print(f"the lowest score: {lowest_score}")