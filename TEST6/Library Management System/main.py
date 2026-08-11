from library.book import Book
from library.library import Library


library = Library()


try:

    book1 = Book("Python Basics", "John Smith", 450)
    book2 = Book("Data Structures", "Robert Martin", 750)
    book3 = Book("Clean Code", "Robert Martin", 900)
    book4 = Book("HTML & CSS", "David Lee", 350)

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)


except ValueError as e:
    print(f"Error: {e}")


# Display all books
library.display_books()


# Search book
library.search_book("Python Basics")


# Search unavailable book
library.search_book("Java Programming")


# Remove book
library.remove_book("HTML & CSS")


# Try removing unavailable book
library.remove_book("Java Programming")


# Sort books by price
sorted_books = sorted(
    library.books,
    key=lambda book: book.price
)

print("\nBOOKS SORTED BY PRICE")
print("=" * 35)

for book in sorted_books:
    print(f"{book.title} -> ₹{book.price}")


# Find most expensive book
try:

    expensive_book = max(
        library.books,
        key=lambda book: book.price
    )

    print("\nMOST EXPENSIVE BOOK")
    print("=" * 35)

    expensive_book.display()

except ValueError:
    print("No books available.")


# Filter books below ₹500
cheap_books = list(
    filter(
        lambda book: book.price < 500,
        library.books
    )
)

print("\nBOOKS BELOW ₹500")
print("=" * 35)

for book in cheap_books:
    print(f"{book.title} -> ₹{book.price}")