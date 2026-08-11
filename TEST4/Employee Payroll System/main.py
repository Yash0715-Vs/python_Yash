from employee.employee import Employee


employees = [
    ("Yash", 45000, "IT"),
    ("Rahul", 60000, "HR"),
    ("Amit", 35000, "IT"),
    ("Priya", 80000, "Manager")
]


# Convert tuples into Employee objects
employee_objects = list(
    map(
        lambda emp: Employee(emp[0], emp[1], emp[2]),
        employees
    )
)


print("EMPLOYEE DETAILS")
print("=" * 35)

for employee in employee_objects:
    employee.display()


# Increase everyone's salary by 10%
employee_objects = list(
    map(
        lambda employee: (
            employee.increase_salary() or employee
        ),
        employee_objects
    )
)


print("\nSALARIES AFTER 10% INCREASE")
print("=" * 35)

for employee in employee_objects:
    print(
        f"{employee.name} -> "
        f"₹{employee.salary}"
    )


# Filter employees earning above 50,000
high_salary_employees = list(
    filter(
        lambda employee: employee.salary > 50000,
        employee_objects
    )
)


print("\nEMPLOYEES EARNING ABOVE ₹50,000")
print("=" * 35)

for employee in high_salary_employees:
    print(
        f"{employee.name} -> "
        f"₹{employee.salary}"
    )


# Sort employees by salary
employee_objects.sort(
    key=lambda employee: employee.salary,
    reverse=True
)


print("\nEMPLOYEES SORTED BY SALARY")
print("=" * 35)

for employee in employee_objects:
    print(
        f"{employee.name} -> "
        f"₹{employee.salary}"
    )


# Find highest-paid employee
highest_paid = max(
    employee_objects,
    key=lambda employee: employee.salary
)


print("\nHIGHEST-PAID EMPLOYEE")
print("=" * 35)

print(f"Name   : {highest_paid.name}")
print(f"Salary : ₹{highest_paid.salary}")