class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Create object
rectangle1 = Rectangle(10, 5)

# Display results
print(f"Area: {rectangle1.area()}")
print(f"Perimeter: {rectangle1.perimeter()}")