class Library:
    def __init__(self):
        """
        Initialize the Library with an empty dictionary for books.
        """
        self.books = {}

    def add_book(self, title):
        """
        Add a new book to the library. Set availability to True.
        """
        if title not in self.books:
            self.books[title] = True
            print(f"Book '{title}' added to the library.")
        else:
            print(f"Book '{title}' is already in the library.")

    def borrow_book(self, title):
        """
        Borrow a book from the library if it’s available.
        """
        if title in self.books:
            if self.books[title]:
                self.books[title] = False
                print(f"You have borrowed '{title}'.")
            else:
                print(f"Sorry, '{title}' is already borrowed.")
        else:
            print(f"Sorry, '{title}' is not available in the library.")

    def return_book(self, title):
        """
        Return a borrowed book to the library.
        """
        if title in self.books:
            if not self.books[title]:
                self.books[title] = True
                print(f"Book '{title}' has been returned.")
            else:
                print(f"Book '{title}' was not borrowed.")
        else:
            print(f"Sorry, '{title}' is not in the library.")

    def view_books(self):
        """
        Display all books in the library with their availability status.
        """
        print("\nBooks in Library:")
        for title, available in self.books.items():
            status = "Available" if available else "Borrowed"
            print(f" - {title}: {status}")


# Example Usage
library = Library()

# Add books
library.add_book("Python Programming")
library.add_book("Data Science Essentials")
library.add_book("Machine Learning Guide")

# View books
library.view_books()

# Borrow books
library.borrow_book("Python Programming")
library.borrow_book("Data Science Essentials")

# View books after borrowing
library.view_books()

# Return a book
library.return_book("Python Programming")

# View books after returning
library.view_books()
