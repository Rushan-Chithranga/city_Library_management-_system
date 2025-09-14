from helpers import read_csv, append_csv, write_csv

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    category = input("Enter Category: ")
    row = [book_id, title, author, category, "Available"]
    append_csv("books.csv", row)
    print("Book added successfully.\n")

def display_books():
    books = read_csv("books.csv")
    print("\n--- Book List ---")
    for b in books:
        print(b)
    print()

def search_book():
    keyword = input("Enter book title or author to search: ").lower()
    books = read_csv("books.csv")
    results = [b for b in books if any(keyword in str(x).lower() for x in b)]
    print("\n--- Search Results ---")
    for r in results:
        print(r)
    if not results:
        print("No books found.")
    print()
