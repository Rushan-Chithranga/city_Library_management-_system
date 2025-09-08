from helpers import read_file

def login():
    users = read_file("users.txt")
    creds = {u.split(",")[0]: u.split(",")[1] for u in users if "," in u}
    for _ in range(3):
        uname = input("Enter username: ")
        pwd = input("Enter password: ")
        if creds.get(uname) == pwd:
            print("✅ Login successful!\n")
            return True
        else:
            print("❌ Invalid credentials.")
    return False
