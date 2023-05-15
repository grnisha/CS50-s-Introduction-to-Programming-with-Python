def main():
    percentage = -1
    while percentage < 0:
        try:
            percentage = convert(input("Fraction: "))
        except (ValueError, ZeroDivisionError):
            pass

    print(gauge(percentage))

#read lines from file po.txt and check if each like start with "po"
def read_po():
    with open("po.txt") as f:
        for line in f:
            if line.startswith("po"):
                print(line)


def convert(fraction):
    try:
        x, y = map(int, fraction.split("/"))
        if x / y > 1:
            raise ValueError
        return int(round(x / y * 100, 0))
    except ValueError:
        raise
    except ZeroDivisionError:
        raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
