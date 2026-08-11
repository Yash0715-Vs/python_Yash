class Vehicle:

    def __init__(self, brand, model, rent_per_day):
        self.brand = brand
        self.model = model
        self.rent_per_day = rent_per_day

    def calculate_rent(self, days):
        return self.rent_per_day * days


class Car(Vehicle):

    def calculate_rent(self, days):
        normal_rent = self.rent_per_day * days
        insurance = 500
        return normal_rent + insurance


class Bike(Vehicle):

    def calculate_rent(self, days):
        normal_rent = self.rent_per_day * days
        insurance = 200
        return normal_rent + insurance


# Create Car object
car = Car("Toyota", "Fortuner", 1000)

# Create Bike object
bike = Bike("Honda", "Shine", 500)


# Calculate rent for 2 days
print("Car Rent:", car.calculate_rent(3))
print("Bike Rent:", bike.calculate_rent(2))