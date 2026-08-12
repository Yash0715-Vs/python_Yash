import numpy as np

sales = np.arange(100, 130)

# 1. Reshape into 5 rows × 6 columns
sales = sales.reshape(5, 6)

# 2. Print the array
print("Sales array:")
print(sales)

# 3. Values greater than 115
print("\nValues greater than 115:")
print(sales[sales > 115])

# 4. Values between 105 and 120
print("\nValues between 105 and 120:")
print(sales[(sales >= 105) & (sales <= 120)])

# 5. Print shape
print("\nShape:", sales.shape)