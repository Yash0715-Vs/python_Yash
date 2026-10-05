import os

folder = "Information Test 1"

# Check if folder exists
if not os.path.exists(folder):
    os.mkdir(folder) #create the folder

# Create file path
file_path = os.path.join(folder, "student.txt")

# Create file
with open(file_path, "w") as file:
    file.write("Yash\n")
    file.write("Python Student")

# Check file
if os.path.isfile(file_path):
    print("File created successfully")

# Get file size
print("File size:", os.path.getsize(file_path), "bytes")

# Show complete path
print("File path:", os.path.abspath(file_path))