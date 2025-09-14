from helpers import read_csv

def login():
    users = read_csv("users.csv")
    creds = {row[0]: row[1] for row in users if len(row) >= 2}
    for _ in range(3):
        uname = input("Enter username: ")
        pwd = input("Enter password: ")
        if creds.get(uname) == pwd:
            print("Login successful!\n")
            return True
        else:
            print("Invalid credentials.")
    return False
