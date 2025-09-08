from helpers import read_file, append_file

def add_member():
    member_id = input("Enter Member ID: ")
    fname = input("First Name: ")
    lname = input("Last Name: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    contact = input("Contact Number: ")
    line = f"{member_id},{fname},{lname},{dob},{contact}"
    append_file("members.txt", line)
    print("✅ Member registered.\n")

def display_members():
    members = read_file("members.txt")
    print("\n--- Members List ---")
    for m in members:
        print(m)
    print()

def search_member():
    keyword = input("Enter member name to search: ").lower()
    members = read_file("members.txt")
    results = [m for m in members if keyword in m.lower()]
    print("\n--- Search Results ---")
    for r in results:
        print(r)
    if not results:
        print("No members found.")
    print()
