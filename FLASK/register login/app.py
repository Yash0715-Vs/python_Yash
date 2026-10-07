from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

# Required for flash messages
app.secret_key = "mysecretkey"

# ---------------- DATABASE CONNECTION ----------------

def get_connection():

    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="flaskDB2"
    )

    return connection


# ---------------- HOME ----------------

@app.route("/")
def home():

    return redirect(url_for("login"))


# ---------------- REGISTER ----------------

@app.route("/register", methods=["GET", "POST"])
def register():

    # If user opens /register
    if request.method == "GET":

        return render_template("register.html")


    # Get data from HTML form
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    username = request.form.get("username")
    password = request.form.get("password")


    # Connect to MySQL
    connection = get_connection()

    cursor = connection.cursor()


    try:

        # SQL query
        query = """
        INSERT INTO users
        (first_name, last_name, username, password)
        VALUES (%s, %s, %s, %s)
        """


        # Execute query
        cursor.execute(
            query,
            (first_name, last_name, username, password)
        )


        # Save changes
        connection.commit()


        # Temporary message
        flash("Registration successful! Please login.")


        # Go to login page
        return redirect(url_for("login"))


    except pymysql.IntegrityError:

        # Cancel database operation
        connection.rollback()


        # Show error message
        flash("Username already exists. Please choose another username.")


        # Go back to register page
        return redirect(url_for("register"))


    finally:

        # Close cursor
        cursor.close()

        # Close database connection
        connection.close()


# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():

    # If user opens /login
    if request.method == "GET":

        return render_template("login.html")


    # Get data from HTML form
    username = request.form.get("username")
    password = request.form.get("password")


    # Connect to MySQL
    connection = get_connection()

    cursor = connection.cursor()


    # SQL query
    query = """
    SELECT first_name, last_name, password
    FROM users
    WHERE username = %s
    """


    # Execute query
    cursor.execute(query, (username,))


    # Get user from database
    user = cursor.fetchone()


    # Close database
    cursor.close()
    connection.close()


    # Check username and password
    if user and user[2] == password:

        first_name = user[0]
        last_name = user[1]


        # Send first name and last name to welcome.html
        return render_template(
            "welcome.html",
            first_name=first_name,
            last_name=last_name
        )


    else:

        # Wrong username or password
        flash("Invalid username or password.")


        # Go back to login page
        return redirect(url_for("login"))


# ---------------- RUN APPLICATION ----------------

if __name__ == "__main__":

    app.run(debug=True)

