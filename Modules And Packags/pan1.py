import pandas as pd

data = {
    "Name": ["Yash", "Rahul", "Amit"],
    "Age": [21, 22, 20],
    "Marks": [85, 91, 76]
}

df = pd.DataFrame(data)

print(df)
print("--------")
print(df["Marks"])
print("--------")
print(df["Age"])
print("--------")
print(df["Name"])