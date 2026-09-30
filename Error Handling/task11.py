student = {
    "name": "Yash",
    "age": 21
}

key = "marks"

# Write your logic here
try:
    print(student["name"])
except KeyError:
    print("key errot")