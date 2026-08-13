import pandas as pd
import numpy as np

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard", "Mouse"],
    "Stock": [5, 20, 8, 15, 50, 100],
    "Price": [60000, 30000, 20000, 15000, 3000, 1500]
}
df = pd.DataFrame(data)
df["InventoryValue"] = df["Stock"]* df["Price"]
print(df)
print(f"\nthe product with stock <10: \n{df[df["Stock"]<10]}")
print(f"\nthe product with stock >20: \n{df[df["Stock"]>20]}")
print(f"\nthe total InventoryValue is: \n{df["InventoryValue"].sum()}")
print(f"\nproduct with the highest inventory value: \n{df.loc[df["InventoryValue"].idxmax()]}")
df["Price"] = np.array(df["Price"])*1.10
print("-"*40)
print(df[["Product", "Price"]])
print("-"*40)
df["Stock"] = df["Stock"] + 10
df["InventoryValue"] = df["Stock"]* df["Price"]
print(df)
print(f"\nthe total InventoryValue is: \n{df["InventoryValue"].sum()}")
print(f"\nthe product with InventoryValue >100000  : \n{df[df["InventoryValue"]>100000]}")
