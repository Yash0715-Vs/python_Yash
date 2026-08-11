import keyword

code = """
def add():
    x = 10
    return x
"""

print("Keywords:", sum(word in keyword.kwlist for word in code.split()))
print("Functions:", code.count("def "))
print("Comments:", code.count("#"))