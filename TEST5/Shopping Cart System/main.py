from cart.cart import ShoppingCart


try:

    cart = ShoppingCart(
        "Laptop",
        "Mouse",
        "Keyboard",
        "Monitor",

        name="Yash",
        email="yash@example.com",
        city="Ahmedabad"
    )

    print("\n")

    # Add another product
    cart.add_item("Mouse")

    # Invalid product
    cart.add_item("Mobile")

    # Remove product
    cart.remove_item("Keyboard")

    # Try removing a product that doesn't exist
    cart.remove_item("TV")

    # Display final bill
    cart.display_bill()

except (ValueError, TypeError) as e:
    print(f"Error: {e}")