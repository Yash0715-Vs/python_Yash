class ShoppingCart:

    products = {
        "Laptop": 50000,
        "Mouse": 800,
        "Keyboard": 1200,
        "Monitor": 15000
    }

    def __init__(self, *args, **kwargs):
        self.items = []
        self.customer_details = kwargs

        # Add products passed through *args
        for product in args:
            self.add_item(product)

    def add_item(self, product):
        try:
            if product not in self.products:
                raise ValueError(f"Invalid product: {product}")

            self.items.append(product)
            print(f"{product} added to cart.")

        except ValueError as e:
            print(e)

    def remove_item(self, product):
        try:
            if product not in self.items:
                raise ValueError(f"{product} is not in the cart.")

            self.items.remove(product)
            print(f"{product} removed from cart.")

        except ValueError as e:
            print(e)

    def show_items(self):
        print("\nCART ITEMS")
        print("-" * 35)

        if not self.items:
            print("Cart is empty.")
            return

        for item in self.items:
            print(f"{item} : ₹{self.products[item]}")

    def calculate_total(self):
        total = 0

        for item in self.items:
            total += self.products[item]

        return total

    def apply_discount(self):
        total = self.calculate_total()

        if total > 50000:
            discount = total * 0.10

        elif total > 30000:
            discount = total * 0.05

        else:
            discount = 0

        final_amount = total - discount

        return discount, final_amount

    def display_bill(self):

        print("\n" + "=" * 40)
        print("FINAL BILL")
        print("=" * 40)

        print("\nCUSTOMER DETAILS")

        for key, value in self.customer_details.items():
            print(f"{key.capitalize()} : {value}")

        self.show_items()

        total = self.calculate_total()
        discount, final_amount = self.apply_discount()

        print("\n" + "-" * 35)
        print(f"Total       : ₹{total:.2f}")
        print(f"Discount    : ₹{discount:.2f}")
        print(f"Final Amount: ₹{final_amount:.2f}")
        print("=" * 40)