import numpy as np

marks = np.array([45, 67, 89, 32, 75, 95, 76])
print(marks[marks > 70])
print(marks[marks >= 75])
print(marks[marks < 35])    
result = marks[(marks >= 60) & (marks <= 85)] # &:--> AND
result2 = marks[(marks < 50) | (marks > 85)]  # |:--> OR
print(result)
print(result2)