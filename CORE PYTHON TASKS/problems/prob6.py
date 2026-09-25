class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        return (f"{self.name} earns {self.salary}")
        pass

class manager(employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department

    def display(self):
        return (f"{self.name} earns {self.salary} and manages {self.department} Department!")
        pass

E = manager("YASH", 50000, "IT")
print(E.display())