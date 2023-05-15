import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    # return bool(re.match(regex, ip))
    pattern = "([0-1]?([0-9]?){2}|2[0-4]?[0-9]?|25[0-5]?)"
    return bool(
        re.match(
            r"^" + pattern + "\." + pattern + "\." + pattern + "\." + pattern + "$", ip
        )
    )


if __name__ == "__main__":
    main()
