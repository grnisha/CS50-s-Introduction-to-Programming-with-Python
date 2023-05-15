import csv
from tabulate import tabulate
from sys import argv, exit

def main():
    if len(argv) < 2:
        exit("Too few command-line arguments")
    if len(argv) > 2:
        exit("Too many command-line arguments")
    if not(argv[1].endswith(".csv")):
        exit("Not a CSV file ")

    print(tabulize(argv[1]))

def tabulize(file):
    try:
        with open(file) as f:
            reader = csv.reader(f)
            table = tabulate(reader, headers="firstrow", tablefmt="grid")
    except FileNotFoundError:
        exit("File does not exist")
    return table

if __name__ == "__main__":
    main()


