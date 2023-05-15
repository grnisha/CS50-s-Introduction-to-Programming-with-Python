from sys import argv, exit
import requests


def main():
    if len(argv) == 2:
        try:
            num = float(argv[1])
        except ValueError:
            exit("Command-line argument is not a number")
    else:
        exit("Missing command-line argument")

    try:
        print(get_price(num))
    except requests.RequestException as e:
        exit(e)



def get_price(num):
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    try:
        response = requests.get(url)
    except requests.RequestException:
        raise requests.RequestException("API Error")

    data = response.json()
    amount = data["bpi"]["USD"]["rate_float"] * num

    return f"${amount:,.4f}"


if __name__ == "__main__":
    main()
