import requests
import sys

# check if the arguments given by the user are correct
if len(sys.argv) == 1:
    sys.exit("Missing command-line argument!")
# the correct input is one number next to the command
elif len(sys.argv) == 2:
    try:
      bitcoinJson = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=42db4378d4e3f4aa4c32ad5984b20e3b050642d5699d39be0fade34cd6cfbc30")
      #currentprice.json
    # in case that an error with request occured, close the program safely
    except requests.RequestException:
      sys.exit("Invalid Request")
    else:
      pass

    # get the price of the bitcoin from the request link
    price = float(bitcoinJson.json()["data"]["priceUsd"].replace(",", ""))
    try:
      amount = price * float(sys.argv[1])
    # to check for if the input is a float number
    except:
       sys.exit("Command-line argument is not a number")
    else:
      print(f"${amount:,.4f}")
