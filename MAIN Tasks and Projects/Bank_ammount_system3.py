class InsufficientFundsError(Exception):
    pass


class BankAccount:

    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):

        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return

        self.balance += amount

        self.transactions.append(
            f"Deposited ₹{amount:.2f}"
        )

        print(f"₹{amount:.2f} deposited successfully.")

    def withdraw(self, amount):

        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return

        if amount > self.balance:
            raise InsufficientFundsError(
                "Insufficient balance!"
            )

        self.balance -= amount

        self.transactions.append(
            f"Withdrawn ₹{amount:.2f}"
        )

        print(f"₹{amount:.2f} withdrawn successfully.")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance:.2f}")

    def display_details(self):

        print("\n===== ACCOUNT DETAILS =====")
        print(f"Name           : {self.name}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance        : ₹{self.balance:.2f}")

    def show_transactions(self):

        print("\n===== TRANSACTION HISTORY =====")

        if not self.transactions:
            print("No transactions yet.")
            return

        for transaction in self.transactions:
            print("-", transaction)

    def account_type(self):
        return "Bank Account"


class SavingsAccount(BankAccount):

    def __init__(
        self,
        name,
        account_number,
        balance=0,
        interest_rate=4
    ):
        super().__init__(name, account_number, balance)
        self.interest_rate = interest_rate

    def account_type(self):
        return "Savings Account"

    def calculate_interest(self):

        interest = self.balance * self.interest_rate / 100

        print(
            f"Interest at {self.interest_rate}%: "
            f"₹{interest:.2f}"
        )


class CurrentAccount(BankAccount):

    def __init__(
        self,
        name,
        account_number,
        balance=0,
        overdraft_limit=5000
    ):
        super().__init__(name, account_number, balance)
        self.overdraft_limit = overdraft_limit

    def account_type(self):
        return "Current Account"

    def withdraw(self, amount):

        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return

        if amount > self.balance + self.overdraft_limit:
            raise InsufficientFundsError(
                "Amount exceeds overdraft limit!"
            )

        self.balance -= amount

        self.transactions.append(
            f"Withdrawn ₹{amount:.2f}"
        )

        print(f"₹{amount:.2f} withdrawn successfully.")


savings = SavingsAccount(
    "Yash",
    "SAV1001",
    10000
)

current = CurrentAccount(
    "Rahul",
    "CUR2001",
    5000
)

savings.display_details()

savings.deposit(2000)

savings.withdraw(1500)

savings.check_balance()

savings.calculate_interest()

savings.show_transactions()
current.display_details()

current.deposit(3000)

current.withdraw(10000)

current.check_balance()

current.show_transactions()
try:
    savings.withdraw(50000)

except InsufficientFundsError as e:
    print("Error:", e)