class Payment:
    def pay(self):
        print("making a payment")

class UPI(Payment):
    def pay(self):
        print("payment using UPI")

class Cash(Payment):
    def pay(self):
        print("payment using Cash")

class Card(Payment):
    def pay(self):
        print("payment using Card")

Payments = [UPI(),Card(),Cash()]
for payment in Payments:
    payment.pay()