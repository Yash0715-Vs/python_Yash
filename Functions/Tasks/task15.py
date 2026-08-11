def employee(**details):
    for key, value in details.items():
        print(f"{key}:{value}")


employee(
    name="Yash",
    age=21,
    department="IT",
    salary=40000,
    city="Ahmedabad"
)
