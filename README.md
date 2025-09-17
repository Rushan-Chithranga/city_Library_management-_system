# 📚 City Library Management System

A simple **Python-based console application** for managing a library. It allows users to login, add/search/display books and members, borrow/return books, and view help instructions. Data is stored in **CSV files** for persistence.

---

## 🚀 Features
- 🔑 **Login System** – Secure login with username/password (stored in `users.csv`)
- 📘 **Book Management** – Add, display, and search books (`books.csv`)
- 👥 **Member Management** – Register, display, and search members (`members.csv`)
- 📖 **Borrow & Return** – Borrow books for 14 days, return them, and update status (`borrow.csv`)
- ℹ️ **Help Section** – Quick guide on how to use the system
- 📂 **CSV Storage** – All records are stored in CSV files for easy management

---

## 📂 Project Structure
```
city_library/
├── main.py
├── auth.py
├── books.py
├── members.py
├── borrow.py
├── help_menu.py
├── helpers.py
├── users.csv
├── books.csv
├── members.csv
├── borrow.csv
```

---

## 🛠️ Requirements
- Python 3.x installed on your computer
- No external libraries required (uses only Python built-in modules: `csv`, `os`, `datetime`)

---

## ▶️ How to Run
1. Clone or download this project folder.
2. Open a terminal or command prompt.
3. Navigate to the folder:
   ```bash
   cd city_library
   ```
4. Run the program:
   ```bash
   python main.py
   ```
5. Login using credentials from `users.csv` (e.g., `admin,1234`).

---

## 📖 Usage Guide
Once logged in, you will see this menu:
```
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
```

- **1. Add Book** → Add new books into `books.csv`
- **2. Display Books** → Show all books in the library
- **3. Search Book** → Search by title or author
- **4. Add Member** → Register new library members into `members.csv`
- **5. Display Members** → View all members
- **6. Search Member** → Find a member by name
- **7. Borrow Book** → Borrow a book for 14 days (updates `books.csv` and `borrow.csv`)
- **8. Return Book** → Return a borrowed book (updates records to Available/Returned)
- **9. Help** → View usage instructions
- **10. Logout & Exit** → Safely log out and exit the system

---

## 📂 Data Storage
- `users.csv` → Stores login credentials
- `books.csv` → Stores book records (Book ID, Title, Author, Category, Status)
- `members.csv` → Stores member records (ID, Name, DOB, Contact)
- `borrow.csv` → Stores borrow/return records (Member ID, Book ID, Dates, Status)

---

## 👨‍💻 Example Login
```
Username: admin
Password: 1234
```

---

## ✅ Future Enhancements
- Add **update/delete** options for books and members
- Implement **overdue fine system** for late returns
- Create a **GUI version** for easier interaction
