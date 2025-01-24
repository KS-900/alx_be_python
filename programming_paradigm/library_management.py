class Book:
    def __init__(self, title, author):
        self.title = title  # Public attribute for the book title
        self.author = author  # Public attribute for the book author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True  # Successfully checked out
        return False  # Book already checked out

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True  # Successfully returned
        return False  # Book was not checked out

    def is_available(self):
        return not self._is_checked_out  # Returns True if the book is available


class Library:
    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, title, author):
        new_book = Book(title, author)  # Create a new Book instance
        self._books.append(new_book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f"Book '{title}' has been checked out."
        return f"Book '{title}' is not available."

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f"Book '{title}' has been returned."
        return f"Book '{title}' was not checked out."

    def list_available_books(self):
        available_books = [f"{book.title} by {book.author}" for book in self._books if book.is_available()]
        return available_books