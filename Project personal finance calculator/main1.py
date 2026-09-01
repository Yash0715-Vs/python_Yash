import json

def get_amount(message):

    while True:
        try:
            value = float(input(message))

            if value <= 0:
                print("Please enter a positive number.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a number.")


def save_to_json(name, income, expenses):

    data = {
        "name": name,
        "income": income,
        "expenses": expenses
    }

    with open("finance_data.json", "w") as file:
        json.dump(data, file, indent=4)

    print("\nData saved successfully to finance_data.json")


def main():

    print("Personal Finance Calculator")

    name = input("Enter your name: ")

    income = [] # THIS IS FOR INCOME DATA

    print("\nINCOME")

    while len(income) < 10:

        category = input("Enter income category: ")

        amount = get_amount("Enter income amount: ")

        income.append({
            "category": category,
            "amount": amount
        })

        choice = input("Do you want to add another income? (y/n): ").lower()

        if choice != "y":
            break

    expenses = [] # THIS IS FOR EXPENSE SDATA

    print("\nEXPENSES ")

    while len(expenses) < 10:

        category = input("Enter expense category: ")

        amount = get_amount("Enter expense amount: ")

        expenses.append({
            "category": category,
            "amount": amount
        })

        choice = input("Do you want to add another expense? (y/n): ").lower()

        if choice != "y":
            break

# FOR CALCULATIONS
    total_income = 0

    for item in income:
        total_income += item["amount"]

    total_expenses = 0

    for item in expenses:
        total_expenses += item["amount"]

    savings = total_income - total_expenses

    if total_income > 0:
        percent_saved = savings / total_income * 100
    else:
        percent_saved = 0

    save_to_json(name, income, expenses)


#PRINTING THE REPORT
    print("\n" + "=" * 50)
    print("             PERSONAL FINANCE REPORT")
    print("=" * 50)

    print("Name:", name)

    print("\nIncome:")

    for item in income:
        print(item["category"], ": ₹", item["amount"])

    print("\nExpenses:")

    for item in expenses:
        print(item["category"], ": ₹", item["amount"])

    print("\n" + "=" * 50)

    print(f"Total Income: ₹{total_income}")
    print(f"Total Expenses: ₹{total_expenses}")
    print(f"Savings: ₹{savings}")
    print(f"Percent Saved: {percent_saved:.2f}%")

    if total_expenses <= total_income:
        print("Affordable: Yes")
    else:
        print("Affordable: No")


main()

