class Student:

    def __init__(self, name, roll_no, department, *marks):
        self.name = name
        self.roll_no = roll_no
        self.department = department
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        return self.calculate_total() / len(self.marks)

    def calculate_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        else:
            return "Fail"

    def display(self):
        print(f"Name       : {self.name}")
        print(f"Roll No    : {self.roll_no}")
        print(f"Department : {self.department}")
        print(f"Marks      : {self.marks}")
        print(f"Total      : {self.calculate_total()}")
        print(f"Average    : {self.calculate_average()}")
        print(f"Grade      : {self.calculate_grade()}")
        print("-" * 30)