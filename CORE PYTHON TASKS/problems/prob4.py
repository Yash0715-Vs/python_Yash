class student:
    def __init__(self,marks):
        self.__marks= 0
        self.set_marks(marks)

    def set_marks(self,marks):
        if 0<= marks <= 100:
            self.__marks=marks
        else:
            print("invalid marks")


    def get_marks(self):
        return self.__marks

Student =student(85)
print(f"marks:{Student.get_marks()}")
Student.set_marks(95)
print(f"update marks: {Student.get_marks()}")


