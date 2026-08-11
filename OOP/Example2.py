class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")


student1 = Student("Yash", 21, "Python")
student2 = Student("Rahul", 22, "Java")

student1.display()

student2.display()