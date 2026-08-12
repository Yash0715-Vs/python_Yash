import numpy as np

marks = np.array([
    [45, 78, 90],
    [88, 56, 72],
    [95, 91, 89],
    [40, 65, 55]
])

# Marks greater than 75
print("Marks greater than 75:")
print(marks[marks > 75])

# Marks less than 60
print("Marks less than 60:")
print(marks[marks < 60])