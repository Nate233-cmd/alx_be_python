# Base Class
class Book:
    """Represents a generic book with title and author."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# Derived Class - EBook
class EBook(Book):
    """Represents an electronic book with file size."""

    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call base class initializer
        self.file_size = file_size  # in KB

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived Class - PrintBook
class PrintBook(Book):
    """Represents a printed book with page count."""

    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call base class initializer
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Composition - Library
class Library:
    """Represents a library that holds a collection of books."""

    def __init__(self):
        self.books = []  # List to store Book, EBook, PrintBook instances

    def add_book(self, book):
        """Add a book to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of all books in the library."""
        for book in self.books:
            print(book)
