class Employee:

    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def display(self):
        print("===== Employee Details =====")
        print(f"Name       : {self.name}")
        print(f"Salary     : ₹{self.salary}")
        print(f"Department : {self.department}")

    def increase_salary(self, amount):
        self.salary += amount
        print(f"Salary increased by ₹{amount}")


# Create object
employee1 = Employee("Yash", 30000, "IT")

# Display original details
employee1.display()

# Increase salary
employee1.increase_salary(5000)

# Display updated details
print()
employee1.display()