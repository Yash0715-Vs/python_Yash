class Employee:

    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

 

class Developer(Employee):

    def calculate_salary(self):
        bonus = self.base_salary * 20 / 100
        return self.base_salary + bonus


class Manager(Employee):

    def calculate_salary(self):
        bonus = self.base_salary * 30 / 100
        return self.base_salary + bonus


class Intern(Employee):

    def calculate_salary(self):
        bonus = self.base_salary * 5 / 100
        return self.base_salary + bonus


# Create employees
employees = [
    Developer("Yash", 50000),
    Manager("Rahul", 80000),
    Intern("Amit", 20000)
]


# Polymorphism
for employee in employees:
    print(employee.name, "→", employee.calculate_salary())