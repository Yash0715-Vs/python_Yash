class MaxLimitExceeded(Exception):
    pass


class HDFC:
    def __init__(self):
        self.transaction_limit = 3
        self.amount_limit = 20000

    def withdraw(self, amount):
        if amount > self.amount_limit:
            raise MaxLimitExceeded("Max Amount exceeds the limit")

        if self.transaction_limit <= 0:
            raise MaxLimitExceeded("Max Transaction limit exceeded")

        self.amount_limit -= amount
        self.transaction_limit -= 1

        print("HDFC withdrawal successful")
        print(f"Amount withdrawn: {amount}")
        print(f"Remaining amount limit: {self.amount_limit}")
        print(f"Remaining transactions: {self.transaction_limit}")

class AXIS:
    def __init__(self):
        self.transaction_limit = 5
        self.amount_limit = 50000

    def withdraw(self, amount):
        if amount > self.amount_limit:
            raise MaxLimitExceeded("Max Amount exceeds the limit")

        if self.transaction_limit <= 0:
            raise MaxLimitExceeded("Max Transaction limit exceeded")

        self.amount_limit -= amount
        self.transaction_limit -= 1

        print("AXIS withdrawal successful")
        print(f"Amount withdrawn: {amount}")
        print(f"Remaining amount limit: {self.amount_limit}")
        print(f"Remaining transactions: {self.transaction_limit}")

class ATM:
    def inputamount(self):

        choice = (input("enter your choice: "))

        if choice.upper() == 'HDFC':
            bank = HDFC()
        elif choice.upper() == 'AXIS':
            bank = AXIS()   
        else:
            return "invalid choice"

        while True:
            try:
                amount = int(input("Enter amount to withdraw: "))

                bank.withdraw(amount)

                next_transaction = input(
                    "Do you want next transaction? (yes/no): "
                )
                
                if next_transaction != "yes" and next_transaction != "no":
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    continue

                if next_transaction.lower() == "no":
                    print("Transaction process terminated")
                    break

            except MaxLimitExceeded as e:
                print("Error:", e)
                print("Transaction process terminated")
                break


atm = ATM()
atm.inputamount()