class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    

class Electronics(Product):

    def calculate_discount(self):
        discount = self.price * 10 / 100
        return self.price - discount


class Clothing(Product):

    def calculate_discount(self):
        discount = self.price * 20 / 100
        return self.price - discount


class Food(Product):

    def calculate_discount(self):
        discount = self.price * 5 / 100
        return self.price - discount


# Create products
products = [
    Electronics("Laptop", 50000),
    Clothing("Jacket", 2000),
    Food("Pizza", 500)
]


# Calculate final price
for product in products:
    final_price = product.calculate_discount()

    print(product.name, "→ Final Price: ₹", final_price)