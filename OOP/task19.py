class loan:
    def __init__(self,amount,years):
        self.amount= amount
        self.years= years

class Homeloan(loan):
    def calculate_interest(self):
        rate = 7
        interest= (self.amount * rate * self.years)/100
        return interest

class Carloan(loan):
    def calculate_interest(self):
        rate = 9
        interest= (self.amount * rate * self.years)/100
        return interest

class Educationloan(loan):
    def calculate_interest(self):
        rate = 5
        interest= (self.amount * rate * self.years)/100
        return interest

loans = [Homeloan(100000,3),
      Carloan(300000,4),
      Educationloan(4000000,5)
      ]

for loan in loans:
    interest = loan.calculate_interest()
    total = loan.amount + interest

    print("Loan Amount:", loan.amount)
    print("Interest:", interest)
    print("Total Amount:", total)
    print("----------------------")