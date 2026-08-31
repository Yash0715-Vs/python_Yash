def get_positive_number(message):
    """Get a valid non-negative number from the user."""
    while True:
        try:
            value = float(input(message))

            if value < 0:
                print("Please enter a non-negative number.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a number.")


def demonstrate_data_types():
    """Demonstrate the required Python data types."""

    print("\n" + "=" * 50)
    print("             DATA TYPE DEMONSTRATION")
    print("=" * 50)

    integer_value = 21
    float_value = 50000.50
    string_value = "Personal Finance"
    boolean_value = True
    complex_value = 2 + 3j

    print(f"Integer : {integer_value} -> {type(integer_value)}")
    print(f"Float   : {float_value} -> {type(float_value)}")
    print(f"String  : {string_value} -> {type(string_value)}")
    print(f"Boolean : {boolean_value} -> {type(boolean_value)}")
    print(f"Complex : {complex_value} -> {type(complex_value)}")


def demonstrate_operators():
    """Demonstrate the required Python operators."""

    print("\n" + "=" * 50)
    print("             OPERATOR DEMONSTRATION")
    print("=" * 50)

    income = 50000
    expenses = 30000

    # Arithmetic operators
    print("\n1. Arithmetic Operators")
    print("Income + Expenses:", income + expenses)
    print("Income - Expenses:", income - expenses)
    print("Income * 2:", income * 2)
    print("Income / 2:", income / 2)
    print("Income % 3000:", income % 3000)

    # Comparison operators
    print("\n2. Comparison Operators")
    print("Income > Expenses :", income > expenses)
    print("Income < Expenses :", income < expenses)
    print("Income == Expenses:", income == expenses)
    print("Income != Expenses:", income != expenses)
    print("Income >= Expenses:", income >= expenses)
    print("Income <= Expenses:", income <= expenses)

    # Logical operators
    print("\n3. Logical Operators")
    print(
        "Income > 0 and Expenses >= 0:",
        income > 0 and expenses >= 0
    )
    print(
        "Income == 0 or Expenses > income:",
        income == 0 or expenses > income
    )
    print(
        "Not income > expenses:",
        not (income > expenses)
    )

    # Assignment operators
    print("\n4. Assignment Operators")
    total = 0

    total += income
    print("After += income:", total)

    total -= expenses
    print("After -= expenses:", total)

    # Identity operators
    print("\n5. Identity Operators")
    value = None

    print("value is None:", value is None)
    print("value is not None:", value is not None)

    # Membership operators
    print("\n6. Membership Operators")

    categories = [
        "Rent",
        "Food",
        "Transport",
        "Utilities"
    ]

    print("'Food' in categories:", "Food" in categories)
    print(
        "'Shopping' not in categories:",
        "Shopping" not in categories
    )

    # Bitwise operators
    print("\n7. Bitwise Operators")

    a = 5
    b = 3

    print("a & b:", a & b)
    print("a | b:", a | b)
    print("a ^ b:", a ^ b)


def calculate_finance(income, expenses):
    """Calculate the user's financial summary."""

    total_expenses = sum(expenses.values())

    savings = income - total_expenses

    if income > 0:
        savings_percentage = (savings / income) * 100
    else:
        savings_percentage = 0

    affordable = total_expenses <= income

    return (
        total_expenses,
        savings,
        savings_percentage,
        affordable
    )


def display_report(
    name,
    income,
    expenses,
    total_expenses,
    savings,
    savings_percentage,
    affordable
):
    """Display a clean personal finance report."""

    print("\n" + "=" * 50)
    print("             PERSONAL FINANCE REPORT")
    print("=" * 50)

    print(f"\nName           : {name}")
    print(f"Monthly Income : ₹{income:,.2f}")

    print("\nEXPENSES")
    print("-" * 50)

    for category, amount in expenses.items():
        print(f"{category:<18}: ₹{amount:,.2f}")

    print("-" * 50)

    print(f"Total Expenses     : ₹{total_expenses:,.2f}")

    print("\nFINANCIAL SUMMARY")
    print("-" * 50)

    print(f"Savings            : ₹{savings:,.2f}")
    print(f"Savings Percentage : {savings_percentage:.2f}%")

    if affordable:
        affordability = "Affordable"
    else:
        affordability = "Not Affordable"

    print(f"Affordability      : {affordability}")

    print("=" * 50)


def main():
    """Run the Personal Finance Calculator."""

    # Demonstrate required Python concepts.
    demonstrate_data_types()
    demonstrate_operators()

    print("\n" + "=" * 50)
    print("          PERSONAL FINANCE CALCULATOR")
    print("=" * 50)

    # Get basic user information.
    name = input("\nEnter your name: ")

    income = get_positive_number(
        "Enter your monthly income: ₹"
    )

    # Define the expense categories.
    expense_categories = [
        "Rent",
        "Food",
        "Transport",
        "Utilities",
        "Entertainment"
    ]

    expenses = {}

    print("\nEnter your monthly expenses:")

    # Collect expense values from the user.
    for category in expense_categories:
        expenses[category] = get_positive_number(
            f"{category}: ₹"
        )

    # Perform financial calculations.
    (
        total_expenses,
        savings,
        savings_percentage,
        affordable
    ) = calculate_finance(
        income,
        expenses
    )

    # Display the final report.
    display_report(
        name,
        income,
        expenses,
        total_expenses,
        savings,
        savings_percentage,
        affordable
    )


if __name__ == "__main__":
    main()