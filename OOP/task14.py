class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

   


class EngineeringStudent(Student):

    def calculate_grade(self):

        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "D"


class MedicalStudent(Student):

    def calculate_grade(self):

        if self.marks >= 85:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "D"


# Create multiple students
students = [
    EngineeringStudent("Yash", 88),
    EngineeringStudent("Rahul", 55),
    MedicalStudent("Amit", 90),
    MedicalStudent("Raj", 65)
]


# Display grades
for student in students:
    print(student.name, ":", student.calculate_grade())