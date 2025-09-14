import datetime
from helpers import read_file, write_file, append_file

def borrow_book():
    member_id = input("Enter Member ID: ")
    book_id = input("Enter Book ID: ")

    books = read_file("books.txt")
    updated_books = []
    found = False
    for b in books:
        parts = b.split(",")
        if parts[0] == book_id and parts[-1] == "Available":
            found = True
            parts[-1] = "Borrowed"
            borrow_date = datetime.date.today()
            due_date = borrow_date + datetime.timedelta(days=14)
            append_file("borrow.txt", f"{member_id},{book_id},{borrow_date},{due_date},Borrowed")
            print(f"Book borrowed successfully! Due on {due_date}")
        updated_books.append(",".join(parts))
    write_file("books.txt", updated_books)
    if not found:
        print("Book not available.\n")

def return_book():
    member_id = input("Enter Member ID: ")
    book_id = input("Enter Book ID: ")

    borrowings = read_file("borrow.txt")
    updated_borrows = []
    returned = False
    for br in borrowings:
        parts = br.split(",")
        if parts[0] == member_id and parts[1] == book_id and parts[-1] == "Borrowed":
            parts[-1] = "Returned"
            returned = True
        updated_borrows.append(",".join(parts))
    write_file("borrow.txt", updated_borrows)

    books = read_file("books.txt")
    updated_books = []
    for b in books:
        parts = b.split(",")
        if parts[0] == book_id:
            parts[-1] = "Available"
        updated_books.append(",".join(parts))
    write_file("books.txt", updated_books)

    if returned:
        print("Book returned successfully.\n")
    else:
        print("No active borrowing found.\n")
