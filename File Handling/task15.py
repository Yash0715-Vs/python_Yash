filename = "File Handling/student.txt"
passes = "pass.txt"
fail = "fail.txt"
passed_student = []
fail_student= []


with open(filename,"r") as file:
    for line in file:
        name,marks = line.strip().split(",")
        # print(name,marks)
        marks = int(marks)
        
        if marks>= 40:
            passed_student.append(f"{name}: {marks}\n")
        else:
            fail_student.append(f"{name}: {marks}\n")
            
with open(passes,"w")as file:
    file.writelines(passed_student)

with open(fail,"w")as file:
    file.writelines(fail_student)

print("report updated succesfully")