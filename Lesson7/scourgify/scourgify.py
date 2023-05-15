from sys import argv, exit
import csv

def main():
    if len(argv) < 3:
        exit("Too few command-line arguments")
    if len(argv) > 3:
        exit("Too many command-line arguments")

    scourgify(argv[1], argv[2])

def scourgify(before, after):
    try:
        with open(before) as f:
            reader = csv.DictReader(f)
            with open(after, 'w') as f2:
                writer = csv.DictWriter(f2, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for student in reader:
                    last, first = student["name"].split(", ")
                    house = student["house"]
                    writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        exit("File does not exist")
 
 
if __name__ == "__main__":
    main()