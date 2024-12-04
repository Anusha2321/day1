class Member:
    def __init__(self, name, membership_id):
        """
        Initialize a library member with name, membership ID, and an empty list of borrowed books.
        """
        self.name = name
        self.membership_id = membership_id
        self.borrowed_books = []

    def borrow_book(self, book):
        """
        Add a book to the borrowed books list if not already borrowed.
        """
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
            print(f"'{book}' has been borrowed by {self.name}.")
        else:
            print(f"'{book}' is already borrowed by {self.name}.")

    def return_book(self, book):
        """
        Remove a book from the borrowed books list.
        """
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"'{book}' has been returned by {self.name}.")
        else:
            print(f"'{book}' is not in the borrowed list for {self.name}.")

    def display_borrowed_books(self):
        """
        Display the list of books currently borrowed by the member.
        """
        if self.borrowed_books:
            print(f"{self.name} has borrowed the following books:")
            for book in self.borrowed_books:
                print(f" - {book}")
        else:
            print(f"{self.name} has not borrowed any books.")

# Example Usage
# Create a library member
member = Member("John Doe", "M001")

# Borrow books
member.borrow_book("The Great Gatsby")
member.borrow_book("1984")
member.borrow_book("The Great Gatsby")  # Duplicate borrow attempt

# Display borrowed books
member.display_borrowed_books()

# Return a book
member.return_book("1984")

# Display borrowed books again
member.display_borrowed_books()

# Return a non-borrowed book
member.return_book("To Kill a Mockingbird")
