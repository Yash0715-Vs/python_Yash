def show_profile():
    print("name:yash")
    print("cource :B.tech it")
    print("sem:7th")

def show_marks():
    print("python:40")
    print("dbms:30")
    print("java:35")

def show_addtendance():
    print("Attendance: 89")

def exit_program():
    print("thank you exit the program")

while True:
    print("1. show profile")
    print("2. show mark")
    print("3. attendance")
    print("4. exit")

    choice = int(input("enter the choice (1-4): "))


    if choice == 1:
        show_profile()

    elif choice == 2:
        show_marks()

    elif choice == 3:
        show_addtendance()

    elif choice == 4:
        exit_program()
        break
    else:
        print("invalid chooice")