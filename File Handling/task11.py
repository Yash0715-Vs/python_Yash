filename = "File Handling/ans.txt"
with open(filename, "r") as f:
    data = f.read()
    words = len(data.split())
print(f"no. of words in {filename} is: {words}")
# Write your logic here
# data = "the name is yash"
# with open (filename , "w") as f:
#     f.write(data)
# with open(filename, "r") as f:
#     data = f.read()
# words = data.split()
# word_count = len(words)
# characters_with_spaces = len(data)
# characters_without_spaces = len(data.replace(" ", ""))
# lines = data.splitlines()
# line_count = len(lines)