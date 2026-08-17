import json

collage = {
        "name":"Indus",
        "location": "Ahmedabad",
        "students":[
        {
            "name":"Yash",
            "age": 22,
            "marks": 70
        },
        {
            "name":"Sahil",
            "age": 22,
            "marks": 22
        },
        {
            "name":"Harshil",
            "age": 22,
            "marks": 55
        }]
}

with open("stu_data.json","w")as f:
    json.dump(collage, f, indent=4)

with open("stu_data.json","r")as f:
    data= json.load(f)

print("College:", data["name"])
print("Location:", data["location"])

print("\nStudents:")

for student in data["students"]:
    print(student["name"], "-", student["marks"])