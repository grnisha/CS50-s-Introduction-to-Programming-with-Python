def main():
    while True:
        try:
            date = input("Date:").strip()
            print(is_valid_date(date))
            break
        except ValueError:
            continue


#Function to test if date is formatted like 9/8/1636 or September 8, 1636
def is_valid_date(date):
    #months list 
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

    #split the date into components
    components = date.split(' ')
    if(len(components) != 3):
        components = date.split('/')

    #check if date contains ,
    if date.find(",") and components[0].title() in months and int((components[1])[:-1]) <=31 and int(components[2]) > 0:
        month = str(months.index(components[0].title()) + 1)
        day = components[1][:-1]
        yy = components[2]
    elif int(components[0]) <= 12 and int(components[1]) <= 31 and int(components[2]) > 0:
        month = components[0]
        day = components[1]
        yy = components[2]
    else:
        raise ValueError("Invalid date format")

    return yy.zfill(4) + "-" + month.zfill(2) + "-" + day.zfill(2)


if __name__ == "__main__":
    main()

    