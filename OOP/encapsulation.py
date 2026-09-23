class Student:
    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("invalid number")


# Create an instance with an initial value
student = Student(85)

# Manual access to the private attribute using name mangling
print("Manual marks access:", student._Student__marks)

# Take input
marks = int(input("Enter marks: "))

# Use setter to update the private attribute safely
student.set_marks(marks)

# Use getter to read the value
print("Marks:", student.get_marks())