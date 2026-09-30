students = ["Yash", "Rahul", "Amit", "Neha"]
filename = "File Handling/student.txt"
with open(filename,"w") as file:
    for student in students:
        file.write(student + "\n")