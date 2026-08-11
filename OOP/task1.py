class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print(f"Balance: ₹{self.balance}")


account = BankAccount(1000)
account.show_balance()

account.deposit(500)
account.show_balance()

account.withdraw(200)
account.show_balance()