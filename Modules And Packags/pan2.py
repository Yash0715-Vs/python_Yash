import pandas as pd
data = {
    "Name": ["Yash", "Rahul", "Amit", "Jay"],
    "Age": [21, 22, 20, 23],
    "Marks": [85, 91, 76, 55]
}

df = pd.DataFrame(data)
print(df)
print(df["Name"])
print(df["Marks"])
print(df.head(2))
print(df.shape)
