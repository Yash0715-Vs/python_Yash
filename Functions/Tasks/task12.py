def bank_transaction(balance, amount, transaction_type):
    if transaction_type == "deposit":
        return balance + amount

    elif transaction_type == "withdraw":
        if amount <= balance:
            return balance - amount
        else:
            return "Insufficient Balance"

    else:
        return "Invalid Transaction Type"


# Function calls
print(bank_transaction(5000, 2000, "deposit"))
print(bank_transaction(5000, 1500, "withdraw"))
print(bank_transaction(5000, 7000, "withdraw"))