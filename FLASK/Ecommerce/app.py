
from flask import Flask, render_template, request, redirect, flash
from database import get_connection
from decimal import Decimal
import pymysql

app = Flask(__name__)
app.secret_key = "mysecretkey"


# HOME PAGE + SEARCH
@app.route("/")
def home():

    search_text = request.args.get("search", "")
    search = search_text.lower().replace("-", "").replace(" ", "")

    connection = get_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    try:
        if search:
            cursor.execute(
                """
                SELECT *
                FROM products
                WHERE REPLACE(
                    REPLACE(LOWER(name), '-', ''),
                    ' ',
                    ''
                ) LIKE %s
                """,
                ("%" + search + "%",)
            )
        else:
            cursor.execute("SELECT * FROM products")

        products = cursor.fetchall()

    finally:
        cursor.close()
        connection.close()

    return render_template(
        "home.html",
        products=products,
        search=search_text
    )


# PRODUCT DETAILS
@app.route("/product/<int:product_id>")
def product_details(product_id):

    connection = get_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    try:
        cursor.execute(
            "SELECT * FROM products WHERE id = %s",
            (product_id,)
        )
        product = cursor.fetchone()

    finally:
        cursor.close()
        connection.close()

    return render_template(
        "product_details.html",
        product=product
    )


# ADD TO CART
@app.route("/add-to-cart", methods=["POST"])
def add_to_cart():

    product_id = request.form.get("product_id", type=int)

    if product_id is None:
        flash("Invalid product ID.", "error")
        return redirect("/")

    connection = get_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    try:
        cursor.execute(
            "SELECT * FROM products WHERE id = %s",
            (product_id,)
        )
        product = cursor.fetchone()

        if not product:
            flash("Product not found.", "error")

        elif product["stock"] <= 0:
            flash(product["name"] + " is out of stock.", "error")

        else:
            cursor.execute(
                """
                INSERT INTO cart (product_id, product_name, quantity)
                VALUES (%s, %s, %s)
                """,
                (product["id"], product["name"], 1)
            )

            connection.commit()
            flash(product["name"] + " added to cart!", "success")

    except Exception:
        connection.rollback()
        flash("Could not add the product to cart.", "error")

    finally:
        cursor.close()
        connection.close()

    return redirect("/")


# CART PAGE
@app.route("/cart")
def cart():

    connection = get_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)

    try:
        cursor.execute(
            """
            SELECT
                cart.id AS cart_id,
                cart.product_id,
                cart.product_name,
                cart.quantity,
                products.price
            FROM cart
            JOIN products ON cart.product_id = products.id
            ORDER BY cart.id DESC
            """
        )

        cart_items = cursor.fetchall()
        total = Decimal("0.00")

        for item in cart_items:
            item["subtotal"] = item["price"] * item["quantity"]
            total += item["subtotal"]

    finally:
        cursor.close()
        connection.close()

    return render_template(
        "cart.html",
        cart_items=cart_items,
        total=total
    )


# REMOVE ITEM FROM CART
@app.route("/remove-from-cart", methods=["POST"])
def remove_from_cart():

    cart_id = request.form.get("cart_id", type=int)

    if cart_id is None:
        flash("Invalid cart item.", "error")
        return redirect("/cart")

    connection = get_connection()
    cursor = connection.cursor()

    try:
        # Delete only the selected cart record
        cursor.execute(
            "DELETE FROM cart WHERE id = %s",
            (cart_id,)
        )

        if cursor.rowcount > 0:
            connection.commit()
            flash("Item removed from cart.", "success")
        else:
            flash("Cart item not found.", "error")

    except Exception:
        connection.rollback()
        flash("Could not remove the item.", "error")

    finally:
        cursor.close()
        connection.close()

    return redirect("/cart")


# RUN APPLICATION
if __name__ == "__main__":
    app.run(debug=True)
