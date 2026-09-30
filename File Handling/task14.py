filename = "File Handling/student.txt"
max_marks = 0
top_student = ""
with open(filename,"r") as file:
    for line in file:
        name,marks = line.strip().split(",")
        marks = int(marks)

        if marks> max_marks:
            max_marks = marks
            top_student = name
    
print(f"top student: {top_student}")
print(f"max marks: {max_marks}")