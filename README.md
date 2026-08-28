# 📚 Library Management System

A simple command-line **Library Management System** built in Python to practice
Object-Oriented Programming (OOP) concepts — classes, objects, encapsulation, and
composition.

## Features

- Add new books to the library
- Register new members
- Borrow a book (tracks which member has which book)
- Return a book
- Search for a book by title
- View the full book catalog
- View all registered members
- Simple menu-based CLI — no external libraries required

## Project Structure

```
library-management-system/
├── library.py     # All classes + CLI menu
└── README.md
```

## Classes

| Class     | Responsibility                                              |
|-----------|---------------------------------------------------------------|
| `Book`    | Represents a single book (`title`, `author`, `is_borrowed`)   |
| `Member`  | Represents a library member and the books they've borrowed    |
| `Library` | Manages the collection of books and members; handles borrow/return/search logic |

## How to Run

Requires Python 3.

```bash
python3 library.py
```

You'll see a menu like this:

```
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
```

Just enter the number of the option you want and follow the prompts.

## Example Usage

```
Enter your choice (1-8): 3
Member name: Fezan
New member added: Fezan

Enter your choice (1-8): 4
Member name: Fezan
Book title to borrow: 1984
Fezan borrowed '1984'

Enter your choice (1-8): 1

--- Library Catalog ---
1984 by George Orwell [Unavailable]
Atomic Habits by James Clear [Available]
The Alchemist by Paulo Coelho [Available]
```

## Possible Future Improvements

- Persist data to a file/database so the library isn't reset every run
- Add due dates and late-return fines
- Add a search-by-author feature

## Author

Built while learning Python OOP concepts (classes, `__init__`, encapsulation,
composition of `Library` + `Book` + `Member`).
