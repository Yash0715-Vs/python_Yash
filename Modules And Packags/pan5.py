import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"],
    "Price": [60000, 30000, 20000, 15000, 3000],
    "Quantity": [2, 5, 3, 4, 10]
}

# 1. Create DataFrame
df = pd.DataFrame(data)

# 2. Add Total column
df["Total"] = df["Price"] * df["Quantity"]

print("DataFrame:")
print(df)


# 3. Product with highest Total
print("\nProduct with highest Total:")
print(df.loc[df["Total"].idxmax()])


# 4. Products where Quantity > 3
print("\nProducts with Quantity > 3:")
print(df[df["Quantity"] > 3])


# 5. Total sales
print("\nTotal Sales:", df["Total"].sum())


# 6. Average product price
print("Average Product Price:", df["Price"].mean())


# 7. First 3 rows
print("\nFirst 3 rows:")
print(df.head(3))