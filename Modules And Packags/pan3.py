import pandas as pd
data = {
    "Name": ["Yash", "Rahul", "Amit", "Jay"],
    "Age": [21, 22, 20, 23],
    "Marks": [85, 91, 76, 55]
}

df = pd.DataFrame(data)
print(df[df["Marks"]>80])
print(df[df["Marks"]<60])
print(df[(df["Marks"] >= 70) & (df["Marks"] <= 90)])
print(df["Marks"].max())
print(df["Marks"].min())
print(df["Marks"].sum())
print(df["Marks"].mean())
df["pass"]= df["Marks"]>=60
print(df)