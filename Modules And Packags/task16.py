import numpy as np
import pandas as pd
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard", "Mouse"],
    "Price": [60000, 30000, 20000, 15000, 3000, 1500],
    "Quantity": [2, 5, 3, 4, 10, 15]
}

df = pd.DataFrame(data)
print(df)

df["total"] = df["Price"] * df["Quantity"]

print(f"\nproduct with highest revenue: \n{df.loc[df["total"].idxmax()]}")
print(f"\nproduct with highest revenue: \n{df.loc[df["total"].idxmin()]}")
print("\nThe average:", df["total"].sum())
print(f"\nthe average of product price : \n{df["Price"].mean()}")
print(f"\nthe product quantity: \n{df[df["Quantity"]>5]}")
df["Price"]= np.array(df["Price"])*1.10
print(f"\nthe price after 10% increase: \n{df[["Product","Price"]]}")
df["total"] = df["Price"] * df["Quantity"]
print("-"*30)
print(df)
print(f"\nthe product after revenue > 50000: \n{df[df["Price"]>50000]}")