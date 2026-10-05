import sys
import os

# 1. Get filename and location from command-line arguments
filename = sys.argv[1]
location = sys.argv[2]

# 2. Create complete file path
file_path = os.path.join(location, filename)

# 3. Ask user for number of lines
number_of_lines = int(input("Enter number of lines: "))

# 4. Create/write data into the file
with open(file_path, "w") as file:

    for i in range(number_of_lines):
        data = input(f"Enter line {i + 1}: ")
        file.write(data + "\n")


# 5. Read data from the file
with open(file_path, "r") as file:
    data = file.read()


# 6. Count lines
lines = data.splitlines()
line_count = len(lines)

# 7. Count words
words = data.split()
word_count = len(words)

# 8. Count characters WITH spaces
characters_with_spaces = len(data)


characters_without_spaces = len(data.replace(" ", "").replace("\n", ""))



print("\n----- File Information -----")
print("Number of lines:", line_count)
print("Number of words:", word_count)
print("Characters with spaces:", characters_with_spaces)
print("Characters without spaces:", characters_without_spaces)