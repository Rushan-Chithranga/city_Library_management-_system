from helpers import read_csv, append_csv

def add_member():
    member_id = input("Enter Member ID: ")
    fname = input("First Name: ")
    lname = input("Last Name: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    contact = input("Contact Number: ")
    row = [member_id, fname, lname, dob, contact]
    append_csv("members.csv", row)
    print("Member registered.\n")

def display_members():
    members = read_csv("members.csv")
    print("\n--- Members List ---")
    for m in members:
        print(m)
    print()

def search_member():
    keyword = input("Enter member name to search: ").lower()
    members = read_csv("members.csv")
    results = [m for m in members if any(keyword in str(x).lower() for x in m)]
    print("\n--- Search Results ---")
    for r in results:
        print(r)
    if not results:
        print("No members found.")
    print()
