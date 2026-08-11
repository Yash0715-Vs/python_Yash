
students = {
    "Yash": 85,
    "Sahil": 92,
    "ANUP": 78,
    "PREET": 92,
    "ARYAN": 88
}


print(f"Student Names: {(students.keys())}") # shows key 


print(f"Marks: {(students.values())}") # showes values


unique_marks = set(students.values()) # set has unique 
print(f"Unique Marks: {unique_marks}")
