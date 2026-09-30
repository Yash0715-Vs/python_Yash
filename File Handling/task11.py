filename = "File Handling/lines.txt"
with open(filename, "r") as f:
    data = f.read()
    words = len(data.split())
print(f"no. of words in {filename} is: {words}")
# Write your logic here