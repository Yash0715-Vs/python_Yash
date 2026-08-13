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
student = Student(0)

# Take input
marks = int(input("Enter marks: "))

# Use setter
student.set_marks(marks)

# Use getter
print("Marks:", student.get_marks())