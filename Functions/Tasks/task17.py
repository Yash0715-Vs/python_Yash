def cart(customer_name, *items, **details):

    print(f"Customer Name : {customer_name}")

    for item in items: #args
        print(item)

    for key, value in details.items(): #kwargs
        print(f"{key}:{value}")

cart("Yash",
    "Pizza",
    "Burger",
    "Cold Drink",
    address="Ahmedabad",
    payment="UPI",
    phone="9876")
