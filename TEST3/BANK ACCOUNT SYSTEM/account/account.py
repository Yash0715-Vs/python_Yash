class BankAccount:

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        try:
            amount = float(amount)

            if amount <= 0:
                print("Deposit amount must be greater than 0.")
                return

            self.balance += amount
            print(f"₹{amount} deposited successfully.")

        except ValueError:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        try:
            amount = float(amount)

            if amount <= 0:
                print("Withdrawal amount must be greater than 0.")
                return

            if amount > self.balance:
                print("Insufficient balance.")
                return

            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

        except ValueError:
            print("Invalid withdrawal amount.")

    def show_balance(self):
        print(f"Account Holder : {self.account_holder}")
        print(f"Balance        : ₹{self.balance}")