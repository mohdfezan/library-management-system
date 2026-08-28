"""
Library Management System
A simple command-line library management system built with Python OOP concepts:
classes, objects, encapsulation, and composition.
"""


class Book:
    """Represents a single book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "[Unavailable]" if self.is_borrowed else "[Available]"
        return f"{self.title} by {self.author} {status}"


class Member:
    """Represents a library member who can borrow and return books."""

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        if self.borrowed_books:
            titles = ", ".join(book.title for book in self.borrowed_books)
        else:
            titles = "No books borrowed"
        return f"{self.name} -> {titles}"


class Library:
    """Manages a collection of books and members."""

    def __init__(self):
        self.books = []
        self.members = []

    # ---------- Book management ----------
    def add_book(self, book_object):
        self.books.append(book_object)
        print(f"Added: {book_object.title}")

    def show_all_books(self):
        if not self.books:
            print("No books in the library yet.")
            return
        print("\n--- Library Catalog ---")
        for book in self.books:
            print(book)

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"Found: {book}")
                return book
        print("Book not found in library")
        return None

    # ---------- Member management ----------
    def add_member(self, member_object):
        self.members.append(member_object)
        print(f"New member added: {member_object.name}")

    def find_member(self, name):
        for member in self.members:
            if member.name.lower() == name.lower():
                return member
        print("Member not found")
        return None

    def show_all_members(self):
        if not self.members:
            print("No members registered yet.")
            return
        print("\n--- Members ---")
        for member in self.members:
            print(member)

    # ---------- Borrow / Return ----------
    def borrow_book(self, member_name, title):
        member = self.find_member(member_name)
        if member is None:
            return

        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_borrowed:
                    print(f"'{book.title}' is already borrowed")
                else:
                    book.is_borrowed = True
                    member.borrowed_books.append(book)
                    print(f"{member.name} borrowed '{book.title}'")
                return
        print("Book not found in library")

    def return_book(self, member_name, title):
        member = self.find_member(member_name)
        if member is None:
            return

        for book in member.borrowed_books:
            if book.title.lower() == title.lower():
                book.is_borrowed = False
                member.borrowed_books.remove(book)
                print(f"{member.name} returned '{book.title}'")
                return
        print(f"{member_name} has not borrowed '{title}'")


# =========================================================
# Simple CLI menu
# =========================================================
def run_cli():
    lib = Library()

    # Some starter data so the menu isn't empty on first run
    lib.add_book(Book("1984", "George Orwell"))
    lib.add_book(Book("Atomic Habits", "James Clear"))
    lib.add_book(Book("The Alchemist", "Paulo Coelho"))

    menu = """
========== Library Management System ==========
1. Show all books
2. Add a book
3. Add a member
4. Borrow a book
5. Return a book
6. Search for a book
7. Show all members
8. Exit
=================================================
"""

    while True:
        print(menu)
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            lib.show_all_books()

        elif choice == "2":
            title = input("Book title: ").strip()
            author = input("Author: ").strip()
            lib.add_book(Book(title, author))

        elif choice == "3":
            name = input("Member name: ").strip()
            lib.add_member(Member(name))

        elif choice == "4":
            name = input("Member name: ").strip()
            title = input("Book title to borrow: ").strip()
            lib.borrow_book(name, title)

        elif choice == "5":
            name = input("Member name: ").strip()
            title = input("Book title to return: ").strip()
            lib.return_book(name, title)

        elif choice == "6":
            title = input("Book title to search: ").strip()
            lib.search_book(title)

        elif choice == "7":
            lib.show_all_members()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    run_cli()
