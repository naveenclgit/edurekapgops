import sys
import requests

if len(sys.argv) < 2:
    print ("Missing command-line argument")
    sys.exit(1)
else:
    try:
        bitc = float(sys.argv[1])
    except ValueError:
        print ("Command-line argument is not a number")
        sys.exit(1)

try:
    mydata = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    #print(f"{mydata.json()}")
    bitcusd = mydata.json()
    #print(f"{bitcusd['bpi']['USD']['rate_float']}")
    btcrate = bitcusd['bpi']['USD']['rate_float']
    #print(f"{btcrate}")
    print(f"${(bitc * btcrate):,.4f}")

except requests.RequestException:
    print("Request Not Done, Try again later!")