from helpers import read_file, append_file, write_file

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    category = input("Enter Category: ")
    line = f"{book_id},{title},{author},{category},Available"
    append_file("books.txt", line)
    print("Book added successfully.\n")

def display_books():
    books = read_file("books.txt")
    print("\n--- Book List ---")
    for b in books:
        print(b)
    print()

def search_book():
    keyword = input("Enter book title or author to search: ").lower()
    books = read_file("books.txt")
    results = [b for b in books if keyword in b.lower()]
    print("\n--- Search Results ---")
    for r in results:
        print(r)
    if not results:
        print("No books found.")
    print()
