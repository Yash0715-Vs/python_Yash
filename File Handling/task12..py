filename = "File Handling/lines.txt"
search_word = "Service-Oriented Architecture (SOA)"

with open (filename, "r")as file:
    data = file.read()
    if search_word in data:
        print("word found")
    else:
        print("word not found!")
# Write your logic here