class vehical:
    def __init__(self,name,speed):
        self.name=name
        self.speed=speed

    def discribe(self):
        return (f"{self.name} is at {self.speed}")
        pass

class electric_vehical(vehical):
    def __init__(self,name,speed,battery_percentage):
        super().__init__(name,speed)
        self.battery_percentage=battery_percentage

    def discribe(self):
        return (f"{self.name} is at {self.speed} speed with {self.battery_percentage} % ")
        pass

E= electric_vehical("BYD",180,80)
print(E.discribe())
