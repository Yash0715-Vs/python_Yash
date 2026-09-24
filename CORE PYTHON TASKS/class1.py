class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print(f"{self.name}h has score {self.marks} marks !")
        
Student = student("yash",85)
Student.display()
