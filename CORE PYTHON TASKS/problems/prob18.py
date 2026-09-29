# # 🔴 Advanced Q25 — Mini Student Database

# For `{'Yash':[80,85,90], 'Rahul':[75,88,82], 'Amit':[90,92,95]}`, calculate each average and find the highest.

# **Expected Output:** `Yash Average: 85.0`, `Rahul Average: 81.67`, `Amit Average: 92.33`, `Top Student: Amit`, `Top Average: 92.33`

students = {
    "Yash": [80, 85, 90],
    "Rahul": [75, 88, 82],
    "Amit": [90, 92, 95]
}

averages = {}

for name, marks in students.items():
    average = sum(marks) / len(marks)
    averages[name] = average
    print(name, "Average:", round(average, 2))

top_student = max(averages, key=averages.get)

print("Top Student:", top_student)
print("Top Average:", round(averages[top_student], 2))