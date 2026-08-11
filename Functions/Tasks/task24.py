def order(customer, *products, **details):

    prices = {
        "Laptop": 50000,
        "Mouse": 800,
        "Keyboard": 1200,
        "Monitor": 15000
    }

    total = 0

    # Calculate total bill
    for product in products:
        total += prices[product]

    # Calculate discount
    if total > 50000:
        discount = total * 10 / 100

    elif total > 30000:
        discount = total * 5 / 100

    else:
        discount = 0

    final_bill = total - discount

    # Print order details
    print("\n===== ORDER DETAILS =====")
    print(f"Customer       : {customer}")

    print("Products       :")
    for product in products:
        print(f"- {product} : ₹{prices[product]}")

    print(f"Address        : {details['address']}")
    print(f"Payment Method : {details['payment']}")
    print(f"Total Bill     : ₹{total}")
    print(f"Discount       : ₹{discount}")
    print(f"Final Bill     : ₹{final_bill}")

    return final_bill


# Function Call
bill = order(
    "Yash",
    "Laptop",
    "Mouse",
    "Keyboard",
    address="Ahmedabad",
    payment="UPI"
)

print(f"\nReturned Final Bill: ₹{bill}")