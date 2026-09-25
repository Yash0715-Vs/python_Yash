class delivary:
    def __init__(self,distance):
        self.distance = distance

    def delivary_time(self):
        return 0

class bike(delivary):
    def delivary_time(self):
        return self.distance * 5

class car(delivary):
    def delivary_time(self):
        return self.distance * 3

class drone(delivary):
    def delivary_time(self):
        return self.distance * 1 


deliveries = [
    bike(4),
    car(5),
    drone(1)
]

for delivary in deliveries:
    print(f"delivary time: {delivary.delivary_time()} munites!")

