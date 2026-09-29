# # 🔴 Advanced Q22 — Product Inventory

# Calculate total inventory value for `{'Laptop':{'price':70000,'stock':2}, 'Mouse':{'price':1000,'stock':5}, 'Keyboard':{'price':2000,'stock':3}}`.

# **Expected Output:** `Total Inventory Value: 149000`
# Write your solution here
datas = {'Laptop':{'price':70000,'stock':2}, 
        'Mouse':{'price':1000,'stock':5}, 
        'Keyboard':{'price':2000,'stock':3}}

total = 0
for data in datas.values():
    total+= data["price"] * data["stock"]

print(f"total inventory value: {total}")

    