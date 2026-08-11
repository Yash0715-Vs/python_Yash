
employees = {
    101: {"Name": "Yash", "Department": "IT", "Salary": 50000},
    102: {"Name": "Sahik", "Department": "HR", "Salary": 45000},
    103: {"Name": "Preet", "Department": "Finance", "Salary": 60000},
    104: {"Name": "Neel", "Department": "Marketing", "Salary": 55000},
    105: {"Name": "Anup", "Department": "Sales", "Salary": 48000}
}

print(employees)

print(f"the highest salary: {max(50000, 45000, 60000, 55000, 48000)}")#higest salary
print(f"the avg salary: {(50000+ 45000+ 60000+ 55000+ 48000)/5}")#avg

emp_id = int(input("Enter Employee ID: "))# Search employee
print(employees.get(emp_id, "Employee Not Found"))

employees[104] ["salary"] =50000 
print(f"the salary is: {employees[104] ["salary"]}")

del employees[101]
print(employees)