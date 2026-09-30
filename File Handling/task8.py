filename = "File Handling/student.txt"
with open(filename, "r") as file:
    data= file.read()
    line= len(data.splitlines())
print(f"the no. of lines: {line}")