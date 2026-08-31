def get_numbers(message):
    while True:
        try:
            value = float(input(message))
            if value < 0:
                print("please enter the positive number")
                continue

            return value
        except ValueError:
            print("Error: invalid number")


name = input("enter your name: ")
income = get_numbers("Enter your monthly income: ₹")
rent = get_numbers("Enter your rent: ₹")
food = get_numbers("Enter your food expense: ₹")
transport = get_numbers("Enter your transport expense: ₹")

print("\nInput received successfully!")

print(f"Name: {name}")
print(f"Income: {income}")
print(f"Rent: {rent}")
print(f"Food: {food}")
print(f"Transport: {transport}")
