filename = "File Handling/student.txt"
destination_file = "backup.txt"

with open(filename , "r") as f:
    c =  f.read()
    print(c)
with open(destination_file,"w") as k:
    k.write(c)
    
# Write your logic here