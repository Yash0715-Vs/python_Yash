class rectangle:
    def __init__(self,length, width):
        self.length=length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle1 = rectangle(10, 5)

# Display results
print(f"Area: {rectangle1.area()}")