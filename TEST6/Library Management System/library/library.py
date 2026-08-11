from .book import Book


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        try:
            if not isinstance(book, Book):
                raise ValueError("Invalid book.")

            self.books.append(book)
            print(f"'{book.title}' added successfully.")

        except ValueError as e:
            print(e)

    def remove_book(self, title):
        try:
            for book in self.books:

                if book.title.lower() == title.lower():
                    self.books.remove(book)
                    print(f"'{title}' removed successfully.")
                    return

            raise ValueError(f"Book '{title}' not found.")

        except ValueError as e:
            print(e)

    def search_book(self, title):
        try:
            for book in self.books:

                if book.title.lower() == title.lower():
                    print("\nBOOK FOUND")
                    print("-" * 30)
                    book.display()
                    return book

            raise ValueError(f"Book '{title}' not found.")

        except ValueError as e:
            print(e)

    def display_books(self):
        try:
            if not self.books:
                raise ValueError("Library is empty.")

            print("\nALL BOOKS")
            print("=" * 35)

            for book in self.books:
                book.display()
                print("-" * 35)

        except ValueError as e:
            print(e)