


square = {i:i**2 for i in range(1,11)}
print(square)

even = {i: i**2 for i in range(1,11) if i%2==0}
print(even)

# list= ["yash","sahil"]
# lst2 = [10,30]

# dict1 = {list[i]: lst2[i] for i in range(len(list))}
# print(dict1)

students = ["Yash","Rahul","Amit"]

marks = [80,90,75]

result = {
    name:marks
    for name, marks in zip(students, marks)
}

print(result)




employee = {
    "Yash":85000,
    "Rahul":30000,
    "Amit":70000,
    "Riya":25000
}

greater = {name:salary for name, salary in employee.items() if salary >= 40000}

print(greater)