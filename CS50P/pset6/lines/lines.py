import sys

file = sys.argv[1]
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif file[-3:] != ".py":
    sys.exit("Not a Python file")

with open(file, "r") as file:
    lines = file.readlines()

count_lines = 0
try:
    for line in lines:
        line = line.lstrip()
        if line.startswith("#") == False:
            if line != "":
                count_lines += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(count_lines)
