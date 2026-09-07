class StudentInfo:
    """this class is used to store the student information like name and roll number"""
    def __init__(self, student_name, student_rollno):
        self.name = student_name
        self.rollno = student_rollno

class StudentMarks:
    """this class is used to store the student marks in three subjects"""

    def __init__(self, student_rollno, marks1, marks2, marks3):
        self.rollno = student_rollno
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3


class main:
    def calculate_grade(self, marks1, marks2, marks3):
        if marks1 > 100 or marks2 > 100 or marks3 > 100:
            return None, "Invalid Marks"

        average = (marks1 + marks2 + marks3) / 3

        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "Fail"

        return average, grade

    def start(self):
        n = int(input("Enter the number of students: "))
        for i in range(n):
            print("\nenter the student information for student", i + 1)
            name = input("Enter the student name: ")
            rollno = input("Enter the student roll number: ")
            student1 = StudentInfo(name, rollno)

            marks1 = float(input("Enter Marks of Subject 1: "))
            marks2 = float(input("Enter Marks of Subject 2: "))
            marks3 = float(input("Enter Marks of Subject 3: "))

            student2 = StudentMarks(rollno, marks1, marks2, marks3)

            average, grade = self.calculate_grade(
                student2.marks1,
                student2.marks2,
                student2.marks3
            )

            print("\nStudent Result")
            print("Roll No:", student1.rollno)
            print("Name:", student1.name)

            if grade == "Invalid Marks":
                print("Result:", grade)
            else:
                print("Average:", average)
                print("Grade:", grade)


obj = main()
obj.start()