employees = [
    ("Yash", 45000),
    ("Rahul", 60000),
    ("Amit", 35000),
    ("Priya", 80000)
]


# 1. Sort Salary in Ascending Order
ascending = sorted(employees, key=lambda emp: emp[1])

print("===== Salary Ascending =====")
for employee in ascending:
    print(employee)


# 2. Sort Salary in Descending Order
descending = sorted(employees, key=lambda emp: emp[1], reverse=True)

print("\n===== Salary Descending =====")
for employee in descending:
    print(employee)


# 3. Find Highest Salary
highest = max(employees, key=lambda emp: emp[1])

print("\n===== Highest Salary =====")
print(highest)


# 4. Find Lowest Salary
lowest = min(employees, key=lambda emp: emp[1])

print("\n===== Lowest Salary =====")
print(lowest)


# 5. Increase Salary by 10% using map()
updated_salaries = list(
    map(lambda emp: (emp[0], emp[1] * 1.10), employees)
)

print("\n===== Salary After 10% Increase =====")
for employee in updated_salaries:
    print(employee)


# 6. Employees earning above 50000 using filter()
high_earners = list(
    filter(lambda emp: emp[1] > 50000, employees)
)

print("\n===== Employees Earning Above 50000 =====")
for employee in high_earners:
    print(employee)