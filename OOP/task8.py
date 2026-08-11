class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary= salary

    def display(self):
        print(f"name: {self.name}")
        print(f"salary is: {self.salary}")



class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department

    def display(self):
        super().display()
        print(f"department: {self.department}")

manager = Manager("Yash",30000,"IT")
manager.display()
