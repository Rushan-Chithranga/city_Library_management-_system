import datetime
from helpers import read_csv, write_csv, append_csv

def borrow_book():
    member_id = input("Enter Member ID: ")
    book_id = input("Enter Book ID: ")

    books = read_csv("books.csv")
    updated_books = []
    found = False

    for b in books:
        if b[0] == book_id and b[-1] == "Available":
            found = True
            b[-1] = "Borrowed"
            borrow_date = datetime.date.today()
            due_date = borrow_date + datetime.timedelta(days=14)
            append_csv("borrow.csv", [member_id, book_id, str(borrow_date), str(due_date), "Borrowed"])
            print(f"Book borrowed successfully! Due on {due_date}")
        updated_books.append(b)

    write_csv("books.csv", updated_books)
    if not found:
        print("Book not available.\n")

def return_book():
    member_id = input("Enter Member ID: ")
    book_id = input("Enter Book ID: ")

    borrowings = read_csv("borrow.csv")
    updated_borrows = []
    returned = False

    for br in borrowings:
        if br[0] == member_id and br[1] == book_id and br[-1] == "Borrowed":
            br[-1] = "Returned"
            returned = True
        updated_borrows.append(br)
    write_csv("borrow.csv", updated_borrows)

    books = read_csv("books.csv")
    updated_books = []
    for b in books:
        if b[0] == book_id:
            b[-1] = "Available"
        updated_books.append(b)
    write_csv("books.csv", updated_books)

    if returned:
        print("Book returned successfully.\n")
    else:
        print("No active borrowing found.\n")
