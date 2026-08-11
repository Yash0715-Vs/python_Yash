class Payment:

    def pay(self, amount):
        pass


class UPIPayment(Payment):

    def pay(self, amount):
        print(f"UPI payment of ₹{amount} successful")


class CardPayment(Payment):

    def pay(self, amount):
        print(f"Card payment of ₹{amount} successful")


class CashPayment(Payment):

    def pay(self, amount):
        print(f"Cash payment of ₹{amount} received")


# Create objects
payments = [UPIPayment(), CardPayment(), CashPayment()]


# Polymorphism
for payment in payments:
    payment.pay(500)