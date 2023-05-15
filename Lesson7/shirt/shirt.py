from PIL import Image, ImageOps
from sys import argv, exit


def main():
    """The program should instead exit via sys.exit:

    if the user does not specify exactly two command-line arguments,
    if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
    if the input’s name does not have the same extension as the output’s name, or
    if the specified input does not exist."""
    if len(argv) != 3:
        exit("Incorect number of arguments")
    if not argv[1].endswith((".jpg", ".jpeg", ".png")) or not argv[2].endswith(
        (".jpg", ".jpeg", ".png")
    ):
        exit("Incorect file type")
    if argv[1][-3:] != argv[2][-3:]:
        exit("Incorect file extension")

    overlap(argv[1], argv[2])


def overlap(before, after):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(before) as input:
            input_cropped = ImageOps.fit(input, shirt.size)
            input_cropped.paste(shirt, mask=shirt)
            input_cropped.save(after)
    except FileNotFoundError:
        exit(f"Input does not exist")


if __name__ == "__main__":
    main()
