data = {
    "students":[{
        "name":"Yash",
        "age": 22,
        "marks": 70
        },
        {"name":"Sahil",
        "age": 22,
        "marks": 22
        },
        {"name":"Harshil",
        "age": 22,
        "marks": 55
        },
        {"name":"Preet",
        "age": 22,
        "marks": 59
        },
        {"name":"Aryan",
        "age": 22,
        "marks": 60
}]
}

for student in data["students"]:
    print(student["name"],student["marks"])