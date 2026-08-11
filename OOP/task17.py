class Delivery:

    def __init__(self, distance, weight):
        self.distance = distance
        self.weight = weight

   


class NormalDelivery(Delivery):

    def calculate_charge(self):
        return self.distance * 10


class ExpressDelivery(Delivery):

    def calculate_charge(self):
        return self.distance * 20


class InternationalDelivery(Delivery):

    def calculate_charge(self):
        return (self.distance * 50) + 1000


# Create delivery objects
deliveries = [
    NormalDelivery(100, 5),
    ExpressDelivery(100, 5),
    InternationalDelivery(100, 5)
]


# Calculate charges
for delivery in deliveries:
    print("Delivery Charge: ₹", delivery.calculate_charge())