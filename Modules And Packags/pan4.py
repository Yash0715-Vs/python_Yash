import pandas as pd

data = {
    "Name": ["Raj", "Amit", "Neha", "Priya", "Karan"],
    "Department": ["IT", "HR", "IT", "Finance", "IT"],
    "Salary": [50000, 45000, 65000, 55000, 70000]
}

df = pd.DataFrame(data)

# 1. Employees from IT
print("Employees from IT:")
print(df[df["Department"] == "IT"])

# 2. Employees with salary greater than 60000
print("\nSalary greater than 60000:")
print(df[df["Salary"] > 60000])

# 3. Average salary
print("\nAverage Salary:", df["Salary"].mean())

# 4. Highest salary
print("Highest Salary:", df["Salary"].max())

# 5. Add Bonus column
df["Bonus"] = df["Salary"] * 0.10

print("\nDataFrame with Bonus:")
print(df)