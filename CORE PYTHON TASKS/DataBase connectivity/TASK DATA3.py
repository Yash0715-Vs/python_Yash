import pymysql


def get_connection():
    connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root',
            db='employee_login'
    )

#register
def register():
    id = int(input("enter the id: "))
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    course = input("Enter Course: ")

    # Check empty fields
    if id == "" or first_name == "" or last_name == "" or username == "" or password == "" or course == "":
        print("All fields are required.")
        return

    connection = get_connection()
    cursor = connection.cursor()

    # Check username already exists
    query = """
    SELECT * FROM employee_login
    WHERE username = %s
    """

    cursor.execute(query, (username,))

    existing_user = cursor.fetchone()

    if existing_user:
        print("Username already exists.")
        connection.close()
        return

    # Insert new user
    query = """
    INSERT INTO studentlogin
    (first_name, last_name, username, password, course)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        first_name,
        last_name,
        username,
        password,
        course
    )

    cursor.execute(query, values)

    connection.commit()

    print("Registration successful!")

    connection.close()


# ---------------- LOGIN ----------------

def login():

    print("\n===== LOGIN =====")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    connection = get_connection()
    cursor = connection.cursor()

    # Check username
    query = """
    SELECT * FROM studentlogin
    WHERE username = %s
    """

    cursor.execute(query, (username,))

    user = cursor.fetchone()

    if user is None:
        print("Wrong username.")
        connection.close()
        return

    # Check password
    if user[4] != password:
        print("Wrong password.")
        connection.close()
        return

    print("\nLogin successful!")
    print("Welcome,", user[1], user[2])
    print("Course:", user[5])

    connection.close()


# ---------------- MAIN PROGRAM ----------------

print("===== STUDENT SYSTEM =====")

choice = input("Enter 1 for Register or 2 for Login: ")

if choice == "1":

    register()

elif choice == "2":

    login()

else:

    print("Invalid choice.")