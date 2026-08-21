from datetime import datetime


expenses = []


def add_expense():
    try:
        amount = float(input("Enter amount: "))
        
        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        category = input("Enter category: ")
        description = input("Enter description: ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d")
        }

        expenses.append(expense)

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount.")


def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n===== ALL EXPENSES =====")

    for index, expense in enumerate(expenses, start=1):
        print(f"\nExpense {index}")
        print(f"Amount      : ₹{expense['amount']:.2f}")
        print(f"Category    : {expense['category']}")
        print(f"Description : {expense['description']}")
        print(f"Date        : {expense['date']}")


def total_spending():
    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal Spending: ₹{total:.2f}")


def category_summary():
    if not expenses:
        print("No expenses found.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    print("\n===== CATEGORY SUMMARY =====")

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")


def highest_expense():
    if not expenses:
        print("No expenses found.")
        return

    highest = max(expenses, key=lambda expense: expense["amount"])

    print("\n===== HIGHEST EXPENSE =====")
    print(f"Amount      : ₹{highest['amount']:.2f}")
    print(f"Category    : {highest['category']}")
    print(f"Description : {highest['description']}")
    print(f"Date        : {highest['date']}")


def delete_expense():
    if not expenses:
        print("No expenses found.")
        return

    view_expenses()

    try:
        number = int(input("\nEnter expense number to delete: "))

        if 1 <= number <= len(expenses):
            removed = expenses.pop(number - 1)
            print(f"{removed['description']} deleted successfully.")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


def sort_by_amount():
    if not expenses:
        print("No expenses found.")
        return

    sorted_expenses = sorted(
        expenses,
        key=lambda expense: expense["amount"],
        reverse=True
    )

    print("\n===== EXPENSES BY AMOUNT =====")

    for expense in sorted_expenses:
        print(
            f"₹{expense['amount']:.2f} - "
            f"{expense['category']} - "
            f"{expense['description']}"
        )


def main():

    while True:

        print("\n========== EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Category Summary")
        print("5. Highest Expense")
        print("6. Delete Expense")
        print("7. Sort by Amount")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_spending()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            highest_expense()

        elif choice == "6":
            delete_expense()

        elif choice == "7":
            sort_by_amount()

        elif choice == "8":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


main()