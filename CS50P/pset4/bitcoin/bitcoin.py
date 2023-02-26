import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    try:
        float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    buy_amount = float(sys.argv[1])
    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = request.json()
    price = data["bpi"]["USD"]["rate"]
    price = float(price.replace(",", ""))
    buy_price = price * buy_amount
    print(f"${buy_price:,.4f}")
