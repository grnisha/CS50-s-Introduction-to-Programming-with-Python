from validators import email

def main():
   print(validate_email(input(email("What's your email address? "))))


def validate_email(s):
    if email(s):
        return f"Valid"
    else:
        return f"Invalid"


if __name__ == '__main__':
    main()