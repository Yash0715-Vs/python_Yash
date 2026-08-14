with open("File Handling/lines.txt", "r") as file:
    data= file.read()
print(data)

char= len(data)
word= len(data.split())
line= len(data.splitlines())

print(f"the no. of chars: {char}")
print(f"the no. of words: {word}")
print(f"the no. of lines: {line}")