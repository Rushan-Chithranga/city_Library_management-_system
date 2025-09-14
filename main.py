from auth import login
from books import add_book, display_books, search_book
from members import add_member, display_members, search_member
from borrow import borrow_book, return_book
from help_menu import help_section

def main_menu():
    while True:
        print("""
===== City Library Management System =====
1. Add Book
2. Display Books
3. Search Book
4. Add Member
5. Display Members
6. Search Member
7. Borrow Book
8. Return Book
9. Help
10. Logout & Exit
""")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            add_member()
        elif choice == "5":
            display_members()
        elif choice == "6":
            search_member()
        elif choice == "7":
            borrow_book()
        elif choice == "8":
            return_book()
        elif choice == "9":
            help_section()
        elif choice == "10":
            print("Logging out... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    print("===== Welcome to City Library Management System =====")
    if login():
        main_menu()
    else:
        print("Too many failed attempts. Exiting...")
