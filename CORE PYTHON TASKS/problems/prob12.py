from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance+= amount
        print("deposite succecful")
        pass

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance-= amount
        else:
            print("Insufficient balance")

        pass

    def get_balance(self):
        return self.__balance
        pass

    @abstractmethod
    def calculate_interest(self):
        
        pass

class SavingsAccount(BankAccount):
    def calculate_interest(self):
            l = self.get_balance()
            m = l * 0.05
            return m
        

class CurrentAccount(BankAccount):
    def calculate_interest(self):
        l = self.get_balance()
        m = l * 0.02
        return m
        pass

accounts = [SavingsAccount("Yash", 100000), CurrentAccount("Rahul", 100000)]

for account in accounts:
    print(account.name)
    print("Interest:", account.calculate_interest())

# INPUT: Yash Savings=100000; Rahul Current=100000
# EXPECTED OUTPUT:
# Yash
# Interest: 5000.0
# Rahul
# Interest: 2000.