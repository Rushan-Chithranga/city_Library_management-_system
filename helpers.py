import csv
import os

def read_csv(filename):
    if not os.path.exists(filename):
        open(filename, "w").close()
    with open(filename, newline="") as f:
        return list(csv.reader(f))

def write_csv(filename, rows):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def append_csv(filename, row):
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)
