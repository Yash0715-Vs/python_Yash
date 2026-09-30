filename = "File Handling/student.txt"

with open(filename, "r") as f:
    data= f.readlines()
print(data)