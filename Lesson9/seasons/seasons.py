from datetime import date
import re
import inflect

p = inflect.engine()

def main():
    dob = input("Date of Birth: ")
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", dob):
        exit("Invalid date")


    today = date.today()
    mins = get_minutes(dob, today)

    print(f"{get_text(mins)} minutes")


def get_minutes(dob, today):
    date_of_birth = date.fromisoformat(dob)
    delta = today - date_of_birth
    return int(delta.total_seconds()/60)


def get_text(mins):
    return p.number_to_words(mins, andword="").capitalize()


if __name__ == "__main__":
    main()

