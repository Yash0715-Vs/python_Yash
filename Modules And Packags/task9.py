import numpy as np
sales = np.array([
    [100, 150, 200, 250],
    [120, 180, 220, 300],
    [90, 140, 190, 210]
])



print("Highest:", np.max(sales))
print("Lowest:", np.min(sales))
print("Total:", np.sum(sales))
print("Average:", np.mean(sales))
print(sales.shape)
print(sales * 1.10)
print(sales[0])
print(np.sum(sales, axis=1)) # axis: means add across each rows
                             # Product 1:
                             # 100 + 150 + 200 + 250 = 700

                             # Product 2:
                             # 120 + 180 + 220 + 300 = 820

                             