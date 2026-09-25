class CreditCard:
    def pay(self):
        print("payment using credit card")
        pass


class UPI:
    def pay(self):
        print ("payment using UPI")
        pass

class Cash:
    def pay(self):
        print ("payment using Cash")

        pass

payments = [CreditCard(), UPI(), Cash()]

for payment in payments:
    payment.pay()

 