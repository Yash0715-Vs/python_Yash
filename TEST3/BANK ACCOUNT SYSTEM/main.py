from account.account import BankAccount


accounts = []

try:
    acc_1 = BankAccount("Yash", 50000)
    acc_2 = BankAccount("Rahul", 30000)
    acc_3 = BankAccount("Amit", 75000)

    accounts.append(acc_1)
    accounts.append(acc_2)
    accounts.append(acc_3)

except ValueError:
    print("Invalid account information.")


print("BANK ACCOUNT SYSTEM")
print("=" * 35)


# Deposit
acc_1.deposit(5000)


# Withdrawal
acc_2.withdraw(10000)


# Invalid withdrawal
acc_3.withdraw(100000)


print("\nACCOUNT DETAILS")
print("=" * 35)

for account in accounts:
    account.show_balance()
    print("-" * 35)


# Sort accounts by balance
accounts.sort(
    key=lambda account: account.balance,
    reverse=True
)

print("\nACCOUNTS SORTED BY BALANCE")
print("=" * 35)

for account in accounts:
    print(
        f"{account.account_holder} -> "
        f"₹{account.balance}"
    )


# Find account with highest balance
highest_account = max(
    accounts,
    key=lambda account: account.balance
)

print("\nHIGHEST BALANCE")
print("=" * 35)

print(f"Account Holder : {highest_account.account_holder}")
print(f"Balance        : ₹{highest_account.balance}")