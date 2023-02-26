from tabulate import tabulate
import sys
import csv


original_menu = sys.argv[1]
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif original_menu[-4:] != ".csv":
    sys.exit("Not a CSV file")


try:
    menu = []
    with open(original_menu, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            menu_line = []
            menu_line.append(row[0])
            menu_line.append(row[1])
            menu_line.append(row[2])
            menu.append(menu_line)


except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(menu, headers="firstrow", tablefmt="grid"))
