from pyfiglet import Figlet
from sys import argv

figlet = Figlet()

# Check number of arguments
if len(argv) not in [1, 3]:
    exit("Incorrect Argument List")

# Check if valid font is specified
if len(argv) == 3:
    if argv[1] not in ["-f", "--font"] and argv[2] not in figlet.FONTS:
        exit("Invalid Font Specified")
    else:
        figlet.setFont(font=argv[2])

print("Output: ", figlet.renderText(input("Input: ")))
