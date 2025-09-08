import os

def read_file(filename):
    if not os.path.exists(filename):
        open(filename, "w").close()
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def write_file(filename, lines):
    with open(filename, "w") as f:
        f.write("\n".join(lines) + ("\n" if lines else ""))

def append_file(filename, line):
    with open(filename, "a") as f:
        f.write(line + "\n")
