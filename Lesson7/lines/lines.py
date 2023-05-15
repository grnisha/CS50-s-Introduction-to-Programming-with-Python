from sys import argv

def main():
    if len(argv) < 2:
        exit("Too few command-line arguments")
    elif len(argv) > 2:
        exit("Too many command-line arguments")

    if not(argv[1].endswith(".py")):
        exit("Not a Python file ")

    print(get_lines(argv[1]))


def get_lines(file):
    total = 0
    try:
        with open(file, "r") as file:
            for line in file:
                if not(line.strip().startswith("#") or line.strip() == ""):
                    total += 1
    except FileNotFoundError:
        exit("File does not exist")

    return total

if __name__ == "__main__":
    main()

