
# from flask import Flask, render_template, request

# app = Flask(__name__)


# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/about")
# def about():
#     return "This is About Page"
# @app.route("/user", methods=["POST"])
# def user():

#     name = request.form.get("name")
#     course = request.form.get("course")
#     age = request.form.get("age")

#     return f"Name: {name}, <br>Course: {course}, <br>Age: {age}"

# @app.route("/user")
# def user():
#     name = request.args.get("name")
#     course = request.args.get("course")

    # return f"Name: {name}, Course: {course}" 

# if __name__ == "__main__":
#     app.run(debug=True)




# add MySQL connection + INSERT student data
from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


# -------------------------------
# Database Connection
# -------------------------------
def get_connection():
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="flask_db"
        )

        return connection

    except pymysql.Error as e:
        print("Database connection error:", e)
        return None


# -------------------------------
# Home Page
# -------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------------------
# About Page
# -------------------------------
@app.route("/about")
def about():
    return "This is About Page"


# -------------------------------
# Add Student
# -------------------------------
@app.route("/user", methods=["POST"])
def user():

    # Get data from HTML form
    name = request.form.get("name")
    course = request.form.get("course")
    age = request.form.get("age")

    # Check if any field is empty
    if not name or not course or not age:
        return "Please fill all the fields."


    # Connect to database
    connection = get_connection()

    if connection is None:
        return "Database connection failed."


    cursor = None

    try:
        # Create cursor
        cursor = connection.cursor()

        # SQL query
        query = """
        INSERT INTO students (name, course, age)
        VALUES (%s, %s, %s)
        """

        # Execute query
        cursor.execute(query, (name, course, age))

        # Save changes
        connection.commit()

        return f"""
        <h2>Student Added Successfully!</h2>

        Name: {name}<br>
        Course: {course}<br>
        Age: {age}
        """

    except pymysql.Error as e:

        # If database error occurs
        connection.rollback()

        return f"Database error: {e}"

    finally:

        # Close cursor
        if cursor:
            cursor.close()

        # Close database connection
        connection.close()


# -------------------------------
# Run Flask Application
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)