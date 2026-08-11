class Employee:

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def display(self):
        print(f"Name       : {self.name}")
        print(f"Salary     : ₹{self.salary}")
        print(f"Department : {self.department}")
        print(f"Bonus      : ₹{self.calculate_bonus()}")
        print("-" * 35)

    def calculate_bonus(self):

        if self.salary > 50000:
            return self.salary * 0.10

        elif self.salary >= 30000:
            return self.salary * 0.05

        else:
            return 0

    def increase_salary(self):
        self.salary = self.salary * 1.10