class Vehical:
    def start(self):
        return "it starts"

class Car(Vehical):
    def start(Self):
        return "BMW"

class Bike(Vehical):
    def start(self):
        return "spllender"

vehical = Vehical()
car =  Car()
bike = Bike()

for vehical in [Car(), Bike()]:
    print(vehical.start())