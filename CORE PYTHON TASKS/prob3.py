class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    

    def deposit(self, amount):
            self.__balance+= amount
            print(f"₹{amount} deposited successfully.")
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
             print("insufficiant balance")
             
    def get_balance(self):
        return self.__balance

account = BankAccount(10000)

account.deposit(5000)
account.withdraw(3000)

print(account.get_balance())