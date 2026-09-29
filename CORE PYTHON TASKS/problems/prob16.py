# # 🔴 Advanced Q23 — Pass/Fail Dictionary

# Group `{'Yash':85,'Rahul':35,'Amit':72,'Neha':28}` into Pass (>=40) and Fail.

# **Expected Output:** `Pass: {'Yash': 85, 'Amit': 72}` and `Fail: {'Rahul': 35, 'Neha': 28}`

# Write your solution here
students= {'Yash':85,'Rahul':35,'Amit':72,'Neha':28}
passed = {}
failed = {}

for name,marks in students.items():
    if marks >= 40:
        passed[name] = marks
    else:
        failed[name] = marks

print(f"pass: {passed}")
print(f"failed: {failed}")
    