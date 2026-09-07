students = {}
#create an empty dictionary to store student information
n = int(input("Enter the number of students: "))

for i in range(n):
    print("\nstudent", i + 1   )
    rollno=input("Enter the student roll number: ")
    name=input("Enter the student name: ")
    marks=float(input("Enter Marks: "))

    students[rollno] = {"name": name, "marks": marks}
    #rollno is the key and name and marks are the values in the dictionary
    print(students)

print("\nStudent Information")
print("1. Display all students")
print("2. Search student name")
print("3. Display marks")
choice = int(input("Enter your choice: "))
if choice ==1:
    for rollno in students:
        print(rollno , students[rollno]['name'], students[rollno]['marks'])

elif choice ==2:
    for data in students.values():
        print(f"name: {data['name']}")

elif choice ==3:
    for data in students.values():
        print(f"marks: {data['marks']}")

else:
    print("Invalid choice")