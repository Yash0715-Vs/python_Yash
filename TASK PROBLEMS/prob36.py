code = open("prob35.py").read()

print("Total Lines:", len(code.splitlines())) #Splits a string into a list of lines
print("Blank Lines:", code.count("\n\n")) #count empty lines
print("Functions:", code.count("def ")) #count functions
print("Classes:", code.count("class ")) #count class
print("Comments:", code.count("#")) #count comments