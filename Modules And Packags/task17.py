
import pandas as pd
data = {
    "Name": ["Dharmik", "Sahil", "Neel", "Preet", "Aryan", "Yash"],
    "Department": ["IT", "HR", "IT", "Finance", "IT", "HR"],
    "Salary": [50000, 45000, 65000, 55000, 70000, 48000],
    "Experience": [2, 3, 5, 4, 6, 2]
}
df= pd.DataFrame(data)
print(df)
print("-"*40)
df["bonus"] = df["Salary"]* 1.10
print(df)
print("-"*40)
df["final salary"] =  df["bonus"]
print(df)
print("-"*40)
print(f"\nEmployee with salary greater than 60000: \n{df[df["Salary"] > 60000]}")
print("-"*40)
print(f"\nEmployee with experience >= 5 years. \n{df[df["Experience"] >= 5]}")
print("-"*40)
print(f"\nhighest-paid employee: \n{df.loc[df["Salary"].idxmax()]}")
print("-"*40)
print(f"the average salary is: \n{df["Salary"].mean()}")
print("-"*40)
print(f"the total salary expance is: \n{df["Salary"].sum()}")
print("-"*40)
df["Additional Bonus"] = 0

df.loc[df["Experience"] >= 5, "Additional Bonus"] = 10000

df["New final salary"]= (df["Salary"] + df["bonus"] + df["Additional Bonus"])
print("-"*40)
print(df)
print("-"*40)
print("\nEmployees with New Final Salary > ₹75,000:")
print(df[df["New final salary"] >= 75000])