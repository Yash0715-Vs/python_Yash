#1
def multiple_name(*names):
    for name in names:
        print(type(name))
multiple_name("yash","Sahil","Preet")

#2
def count_arguments(*args):
    print(f"Total arguments = {len(args)}")

# Function calls
count_arguments(10, 20, 30)
count_arguments("Yash", "Rahul")
count_arguments(1, 2, 3, 4, 5)

#3
def largest_number(*args):
    print(f"Largest number = {max(args)}")

# Function calls
largest_number(10, 25, 5, 40, 18)
largest_number(100, 250, 75)
largest_number(8, 3, 12, 6)

#4
def student(name, *marks):
    print(f"name: {name}")
    print(f"marks: {marks}")
    print(f"the sum is: {sum(marks)}")
    print(f"the avg is: {sum(marks)/len(marks)}")

student("yash",85, 90, 78, 88, 95)