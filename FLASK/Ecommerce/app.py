from flask import Flask, render_template, request, redirect, flash
from database import get_connection
import pymysql


app = Flask(__name__)

# Required for flash messages
app.secret_key = "mysecretkey"


# =========================================================
# HOME PAGE + PRODUCT SEARCH
# =========================================================

@app.route("/")
def home():

    # Get search text from URL
    search = request.args.get("search", "")

    # Convert search text to lowercase
    # Remove spaces and hyphens
    search = search.lower().replace("-", "").replace(" ", "")

    # Connect to MySQL
    connection = get_connection()

    # Use dictionary cursor
    cursor = connection.cursor(
        pymysql.cursors.DictCursor
    )

    # If user searched something
    if search:

        cursor.execute(
            """
            SELECT *
            FROM products
            WHERE REPLACE(
                    REPLACE(
                        LOWER(name),
                        '-',
                        ''
                    ),
                    ' ',
                    ''
                  ) LIKE %s
            """,
            ("%" + search + "%",)
        )

    # If no search
    else:

        cursor.execute(
            "SELECT * FROM products"
        )

    # Get all products
    products = cursor.fetchall()

    # Close connection
    cursor.close()
    connection.close()

    # Send products to HTML
    return render_template(
        "home.html",
        products=products,
        search=search
    )


# =========================================================
# PRODUCT DETAILS
# =========================================================

@app.route("/product/<int:product_id>")
def product_details(product_id):

    # Connect to MySQL
    connection = get_connection()

    # Dictionary cursor
    cursor = connection.cursor(
        pymysql.cursors.DictCursor
    )

    # Get product using ID
    cursor.execute(
        """
        SELECT *
        FROM products
        WHERE id = %s
        """,
        (product_id,)
    )

    # Get one product
    product = cursor.fetchone()

    # Close connection
    cursor.close()
    connection.close()

    # Send product to HTML
    return render_template(
        "product_details.html",
        product=product
    )


# =========================================================
# ADD TO CART
# =========================================================

@app.route("/add-to-cart", methods=["POST"])
def add_to_cart():

    # Get product ID from HTML form
    product_id = request.form.get("product_id")

    # Connect to MySQL
    connection = get_connection()

    # Dictionary cursor
    cursor = connection.cursor(
        pymysql.cursors.DictCursor
    )

    # Get product information
    cursor.execute(
        """
        SELECT *
        FROM products
        WHERE id = %s
        """,
        (product_id,)
    )

    product = cursor.fetchone()

    # Check if product exists
    if product:

        # Check stock
        if product["stock"] > 0:

            # Insert product into cart
            cursor.execute(
                """
                INSERT INTO cart
                (product_id, product_name, quantity)
                VALUES (%s, %s, %s)
                """,
                (
                    product["id"],
                    product["name"],
                    1
                )
            )

            # Save changes
            connection.commit()

            # Show success message
            flash(
                product["name"] + " added to cart!",
                "success"
            )

        else:

            # Product is out of stock
            flash(
                product["name"] + " is out of stock.",
                "error"
            )

    else:

        # Product doesn't exist
        flash(
            "Product not found.",
            "error"
        )

    # Close connection
    cursor.close()
    connection.close()

    # Go back to home page
    return redirect("/")


# =========================================================
# RUN FLASK
# =========================================================

if __name__ == "__main__":

    app.run(debug=True)