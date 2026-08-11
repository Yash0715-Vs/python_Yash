name= input("enter your name: ")
age = int(input("enter your age: "))
city =input("enter your city: ")
cgpa = float(input("enter your cgpa: "))

student = {"name":name,"age":age,"city":city,"cgpa":cgpa}
print(student)
print(student.keys())
print(student.values())
student["cgpa"] =9.2 #update cgpa
del student["city"] #delete city
print(student)

