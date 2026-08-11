class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"₹{amount} withdrawn successfully.")

    def display_balance(self):
        print(f"{self.account_holder}'s balance: ₹{self.balance}")


class SavingsAccount(BankAccount):

    def withdraw(self, amount):
        if self.balance - amount >= 500:
            self.balance -= amount
            print(f"₹{amount} withdrawn from Savings Account.")
        else:
            print("Withdrawal denied! Minimum balance of ₹500 is required.")


class CurrentAccount(BankAccount):

    def withdraw(self, amount):
        if self.balance - amount >= -5000:
            self.balance -= amount
            print(f"₹{amount} withdrawn from Current Account.")
        else:
            print("Withdrawal denied! Overdraft limit is ₹5000.")


# Savings Account
savings = SavingsAccount("Yash", 2000)

savings.display_balance()

savings.deposit(1000)
savings.display_balance()

savings.withdraw(2000)
savings.display_balance()

savings.withdraw(1000)
savings.display_balance()


print("\n----------------------\n")


# Current Account
current = CurrentAccount("Rahul", 2000)

current.display_balance()

current.deposit(1000)
current.display_balance()

current.withdraw(7000)
current.display_balance()

current.withdraw(2000)
current.display_balance()