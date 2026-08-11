# def employee(name, salary, department):

#     print(f"Name       : {name}")
#     print(f"Salary     : {salary}")
#     print(f"Department : {department}")
    

# # Function calls
# employee("Yash", 50000, "IT")
# employee("Rahul", 45000, "HR")
# employee("Priya", 60000, "Finance")

def employee(name, department="IT", salary=30000):
    
    print(f"Name       : {name}")
    print(f"Department : {department}")
    print(f"Salary     : {salary}")
    print()

# 1. Using only the required argument
employee("Yash")

# 2. Changing the department only
employee("Rahul", "HR")

# 3. Changing both department and salary
employee("Priya", "Finance", 50000)

# 4. Using keyword arguments
employee(name="Amit", salary=60000, department="Marketing")