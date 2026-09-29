# 🟡 Intermediate Q17 — List of Dictionaries

# Find total salary for `[{'name':'Yash','salary':30000},{'name':'Rahul','salary':40000},{'name':'Amit','salary':35000}]`.

# **Expected Output:** `Total Salary: 105000`

# Write your solution here
datas = [{'name':'Yash','salary':30000},
         {'name':'Rahul','salary':40000},
         {'name':'Amit','salary':35000}]

total = 0
for data in datas:
    total+= data["salary"]

print(f"total salary: {total}")
