
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return "This is About Page"
@app.route("/user", methods=["POST"])
def user():

    name = request.form.get("name")
    course = request.form.get("course")
    age = request.form.get("age")

    return f"Name: {name}, <br>Course: {course}, <br>Age: {age}"

# @app.route("/user")
# def user():
#     name = request.args.get("name")
#     course = request.args.get("course")

    # return f"Name: {name}, Course: {course}" 

if __name__ == "__main__":
    app.run(debug=True)