def main():
    inputTime = input("What time is it? ")
    time = convert(inputTime)
    if time >= 7.0 and time <= 8.0:
        print("breakfast time")
    elif time >= 12.0 and time <= 13.0 :
        print("lunch time")
    elif time >= 18.0 and time <= 19.0 :
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")

    if minutes.endswith("p.m."):
        hours = float(hours) + 12
        minutes = minutes.replace(" p.m.", "")
    elif minutes.endswith("a.m."):
        minutes = minutes.replace(" a.m.", "")

    return float(hours) + float(minutes)/60


if __name__ == "__main__":
    main()