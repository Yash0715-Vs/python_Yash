# # 🔴 Advanced Q24 — Tuple Data to Dictionary

# Convert `(('Laptop',70000),('Phone',50000),('Tablet',30000))` to a dictionary and find the most expensive product.

# **Expected Output:** `{'Laptop': 70000, 'Phone': 50000, 'Tablet': 30000}`; `Most Expensive: Laptop`; `Price: 70000`
# Write your solution here
A = (('Laptop',70000),('Phone',50000),('Tablet',30000))
result = dict(A)
print(result)
expensive = max(result, key=result.get)
print(f"most expensive: {expensive}")
print(f"Price: {result[expensive]}")