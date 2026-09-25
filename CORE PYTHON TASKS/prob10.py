class employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class developer(employee):

    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.bonus + 10000


class manager(employee):

    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.bonus + 20000


employees = [
    developer("Yash", 50000, 0),
    manager("Rahul", 50000, 0)
]

salaries = [50000, 50000]

for employee, amount in zip(employees, salaries):
    print(employee.name, employee.calculate_salary())