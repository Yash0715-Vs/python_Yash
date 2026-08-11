class shape:
    def area(self):
        print("shape area: ")

class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        print(f"the circle area is: {3.14 * self.radius * self.radius}")

class rectangle(shape):
    def __init__(self,length,width):
        self.length = length 
        self.width = width 

    def area(self):
        print(f"the rect area is: {self.length * self.width}")

c = circle(5)
r = rectangle(10,5)
c.area()
r.area()