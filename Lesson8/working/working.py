import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    regex = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    match = re.search(r"^" + regex + " to " + regex + "$", s)
    if match:
        start = convert_time(match.group(1), match.group(2), match.group(3))
        end = convert_time(match.group(4), match.group(5), match.group(6))
        return f"{start} to {end}"
    else:
        raise ValueError


def convert_time(hour, minute, ampm):
    # Check hour
    if ampm == "AM":
        if hour == "12":
            hour = "00"
    else:
        if hour != "12":
            hour = f"{int(hour) + 12}"
    # Check minute
    if minute == None:
        minute = "00"
    # format & return in HH:mm format
    return f"{int(hour):02}:{int(minute):02}"


if __name__ == "__main__":
    main()
