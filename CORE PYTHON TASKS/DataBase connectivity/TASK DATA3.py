import pymysql


def get_connection():
    try:
        connection = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root',
            database='employee_login'
        )
        return connection
    except pymysql.MySQLError as e:
        print(f"Database connection failed: {e}")
        return None
    except Exception as e:
        print(f"Unexpected database error: {e}")
        return None


# ---------------- REGISTER ----------------

def register():
    try:
        id = int(input("Enter the ID: "))
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        course = input("Enter Course: ")
    except EOFError:
        print("\nInput cancelled. Exiting register.")
        return

    # Check empty fields
    if first_name == "" or last_name == "" or username == "" or password == "" or course == "":
        print("All fields are required.")
        return

    connection = get_connection()
    if connection is None:
        return
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

    try:
        cursor.execute(query, values)
        connection.commit()
        print("Registration successful!")
    except pymysql.MySQLError as e:
        print(f"Registration failed: {e}")
        connection.rollback()
    finally:
        connection.close()


# ---------------- LOGIN ----------------

def login():

    print("\n===== LOGIN =====")

    try:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
    except EOFError:
        print("\nInput cancelled. Exiting login.")
        return

    connection = get_connection()
    if connection is None:
        return
    cursor = connection.cursor()

    # Check username
    query = """
    SELECT * FROM employee_login
    WHERE username = %s
    """

    try:
        cursor.execute(query, (username,))
        user = cursor.fetchone()
    except pymysql.MySQLError as e:
        print(f"Login failed: {e}")
        connection.close()
        return

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

print("===== EMPLOYEE SYSTEM =====")

try:
    choice = input("Enter 1 for Register or 2 for Login: ")
except EOFError:
    print("\nNo input received. Exiting program.")
    raise SystemExit

if choice == "1":
    register()
elif choice == "2":
    login()
else:
    print("Invalid choice.")