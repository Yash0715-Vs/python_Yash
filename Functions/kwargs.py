# def employee(**details):
#     for key, value in details.items():
#         print(f"{key}:{value}")

# employee(name= "yash",salary= 50000,dipartment= "IT")


def order(customer_name, *items, **details):
    print(f"Customer Name : {customer_name}")

    for item in items: #args
        print(item)

    for key, value in details.items(): #kwargs
        print(f"{key}:{value}")

order("Yash",
    "Pizza",
    "Burger",
    "Cold Drink",
    address="Ahmedabad",
    payment="UPI",
    phone="9876")


# def order(customer_name, *items, **details):
    
#     print(f"Customer Name : {customer_name}")

    
#     for item in items:
#         print(item)

#     print("\nAdditional Details:")
#     for key, value in details.items():
#         print(f"{key} : {value}")


# # Function call
# order(
#     "Yash",
#     "Pizza",
#     "Burger",
#     "Cold Drink",
#     address="Ahmedabad",
#     payment="UPI",
#     phone="9876543210"
# )
            

