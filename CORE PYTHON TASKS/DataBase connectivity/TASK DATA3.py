import pymysql


# Connect Python with MySQL
def get_connection():

    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="employee_login"
    )

    return connection


# ---------------- REGISTER ----------------

def register():

    print("\n===== REGISTER =====")

    id = int(input("Enter ID: "))
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    course = input("Enter Course: ")

    # Check empty fields
    if first_name == "" or last_name == "" or username == "" or password == "" or course == "":
        print("All fields are required.")
        return

    # Connect to database
    connection = get_connection()

    # Create cursor
    cursor = connection.cursor()

    # Check username
    query = """
    SELECT * FROM employee_login
    WHERE username = %s
    """

    cursor.execute(query, (username,))

    user = cursor.fetchone()

    if user:
        print("Username already exists.")
        connection.close()
        return

    # Insert user
    query = """
    INSERT INTO employee_login
    (id, first_name, last_name, username, password, course)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        id,
        first_name,
        last_name,
        username,
        password,
        course
    )

    cursor.execute(query, values)

    # Save data
    connection.commit()

    print("Registration successful!")

    connection.close()


# ---------------- LOGIN ----------------

def login():

    print("\n===== LOGIN =====")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    # Connect to database
    connection = get_connection()

    # Create cursor
    cursor = connection.cursor()

    # Find username
    query = """
    SELECT * FROM employee_login
    WHERE username = %s
    """

    cursor.execute(query, (username,))

    user = cursor.fetchone()

    # Username not found
    if user is None:
        print("Wrong username.")
        connection.close()
        return

    # Check password
    if user[4] != password:
        print("Wrong password.")
        connection.close()
        return

    # Login successful
    print("\nLogin successful!")
    print("Welcome,", user[1], user[2])
    print("Course:", user[5])

    connection.close()


# ---------------- MAIN PROGRAM ----------------

print("===== EMPLOYEE SYSTEM =====")

choice = input("Enter 1 for Register or 2 for Login: ")

if choice == "1":

    register()

elif choice == "2":

    login()

else:

    print("Invalid choice.")