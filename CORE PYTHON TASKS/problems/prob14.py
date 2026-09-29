# # 🔴 Advanced Q18 — Highest Marks

# Find the student with highest marks from `{'Yash':85,'Rahul':92,'Amit':78,'Neha':88}`.

# **Expected Output:** `Top Student: Rahul`, `Marks: 92`

# Write your solution here
students = {'Yash':85,'Rahul':92,'Amit':78,'Neha':88}
top_student = max(students, key=students.get)

print("Top Student:", top_student)
print("Marks:", students[top_student])