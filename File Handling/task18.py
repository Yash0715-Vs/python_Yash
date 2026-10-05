def write_data(n):

    filename = "File Handling/studentInfo.txt"
    filename2 = "File Handling/MarksInfo.txt"

  

    with open(filename, "w") as file:

        for i in range(n):

            roll_no = input("Enter your roll_no: ")
            name = input("Enter your name: ")

            file.write(roll_no + "-" + name + "\n")

            print("StudentInfo updated!")
    

    with open(filename2, "w") as file:

        for i in range(n):

            roll_no = input("Enter roll_no: ")

            mark1 = input("Enter marks of subject 1: ")
            mark2 = input("Enter marks of subject 2: ")
            mark3 = input("Enter marks of subject 3: ")

            file.write( roll_no + "-" + mark1 + "-" + mark2 + "-" + mark3 + "\n")
            

            print("Marks updated!")

    students = {}

    with open(filename, "r") as file:

        for line in file:

            line = line.strip()

            # Skip empty lines
            if line == "":
                continue

            data = line.split("-")

            roll_no = data[0]
            name = data[1]

            students[roll_no] = name


    results = []

    with open(filename2, "r") as file:

        for line in file:

            line = line.strip()

            # Skip empty lines
            if line == "":
                continue

            data = line.split("-")

            roll_no = data[0]

            mark1 = int(data[1])
            mark2 = int(data[2])
            mark3 = int(data[3])

            # Calculate average
            average = (mark1 + mark2 + mark3) / 3

            if average >= 80:
                grade = "A"

            elif average >= 60:
                grade = "B"

            elif average >= 40:
                grade = "C"

            else:
                grade = "Fail"


            # Get name using roll number
            name = students[roll_no]

            # Store result
            results.append((roll_no, name, average, grade))
    results.sort( key=lambda x: x[2], reverse=True)



    with open("Agrade.txt", "w") as file:
        for roll_no, name, average, grade in results:
            if grade == "A":
                file.write( roll_no + "-" + name + "-" + str(average) + "\n")

    with open("Bgrade.txt", "w") as file:
        for roll_no, name, average, grade in results:
            if grade == "B":
                file.write( roll_no + "-" + name + "-" + str(average) + "\n")

    with open("Cgrade.txt", "w") as file:
        for roll_no, name, average, grade in results:
            if grade == "C":
                file.write( roll_no + "-" + name + "-" + str(average) + "\n")

                


n = int(input("Enter number of students: "))

write_data(n)

print("Agrade.txt created")
print("Bgrade.txt created")
print("Cgrade.txt created")