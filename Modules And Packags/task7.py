import numpy as np
temperatures = np.array([32, 35, 31, 38, 40, 36, 34])


print("max temp:", np.max(temperatures))
print("Low temp:", np.min(temperatures))
print("average:", np.sum(temperatures))
print("difference:", np.max(temperatures)- np.min(temperatures))
