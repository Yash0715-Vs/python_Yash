filename = "File Handling/students.txt"

try:
    with open(filename, "r") as file:

        for line in file:
            try:
                name, marks = line.strip().split(",")
                marks = int(marks)

                print(name, "-", marks)

            except ValueError:
                print("Invalid marks for", name)

except FileNotFoundError:
    print("File not found")