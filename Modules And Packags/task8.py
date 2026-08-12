import numpy as np
marks = np.array([
    [80, 75, 90],
    [65, 88, 72],
    [95, 91, 89],
    [70, 68, 76]
])

print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Average:", np.mean(marks))
print(marks.shape)
print(marks[0])