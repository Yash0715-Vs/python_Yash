class Employee:

    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary



class Developer(Employee):

    def calculate_salary(self):
        bonus = self.base_salary * 20 / 100
        return self.base_salary + bonus

    def display(self):
        print(f"Developer: {self.name}")
        print(f"Base Salary: ₹{self.base_salary}")
        print(f"Final Salary: ₹{self.calculate_salary()}")


class Manager(Employee):

    def calculate_salary(self):
        bonus = self.base_salary * 30 / 100
        return self.base_salary + bonus

    def display(self):
        print(f"Manager: {self.name}")
        print(f"Base Salary: ₹{self.base_salary}")
        print(f"Final Salary: ₹{self.calculate_salary()}")


class Intern(Employee):

    def calculate_salary(self):
        bonus = self.base_salary * 5 / 100
        return self.base_salary + bonus

    def display(self):
        print(f"Intern: {self.name}")
        print(f"Base Salary: ₹{self.base_salary}")
        print(f"Final Salary: ₹{self.calculate_salary()}")


# Create employees
employees = [
    Developer("Yash", 50000),
    Manager("Rahul", 80000),
    Intern("Amit", 20000)
]


# Polymorphism
for employee in employees:
    employee.display()
    print("--------------------")