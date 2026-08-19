employees = [
    {"name": "Ravi", "salary": 45000},
    {"name": "Anu", "salary": 60000},
    {"name": "Kabir", "salary": 35000},
    {"name": "Neha", "salary": 75000}
]

sorted_employees = sorted(
    employees,
    key=lambda employee: employee["salary"],
    reverse=True
)

print(sorted_employees)