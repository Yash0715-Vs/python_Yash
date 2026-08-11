class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append((name, price))
        print(f"{name} added to cart.")

    def remove_item(self, name):
        for item in self.items:
            if item[0] == name:
                self.items.remove(item)
                print(f"{name} removed from cart.")
                return

        print(f"{name} not found in cart.")

    def show_items(self):
        print("\n===== SHOPPING CART =====")

        if len(self.items) == 0:
            print("Cart is empty.")
        else:
            for item in self.items:
                print(f"{item[0]} - ₹{item[1]}")

    def total_price(self):
        total = 0

        for item in self.items:
            total += item[1]

        return total


# Create object
cart = ShoppingCart()

# Add items
cart.add_item("Laptop", 50000)
cart.add_item("Mouse", 800)
cart.add_item("Keyboard", 1200)

# Show items
cart.show_items()

# Show total
print(f"\nTotal Price: ₹{cart.total_price()}")

# Remove item
cart.remove_item("Mouse")

# Show updated cart
cart.show_items()

print(f"\nTotal Price: ₹{cart.total_price()}")